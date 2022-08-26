from django.shortcuts import redirect, render, get_object_or_404
from estore.models import Category, Product, Cart
from datetime import datetime
import requests
import decimal
import base64
import json


tokens = '{{APPLICATION_TOKEN}}:{{ADMIN_ACCESS_TOKEN}}'
encoded = base64.b64encode(tokens.encode('ascii'))
headers = {
     'Content-Type': 'application/json',
     'Authorization': 'Basic ' + encoded.decode('utf-8')
}

def home(request):
    categories = Category.objects.filter()[:3]
    products = Product.objects.filter()[:8]
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'estore/index.html', context)

def category_products(request, url_slug):
    category = get_object_or_404(Category, url_slug=url_slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        'category': category,
        'products': products,
        'categories': categories,
    }
    return render(request, 'estore/category_products.html', context)

def cart(request):
    cart_products = Cart.objects.all()

    amount = cart_total()
    shipping_amount = decimal.Decimal(0)

    context = {
        'cart_products': cart_products,
        'amount': amount,
        'shipping_amount': shipping_amount,
        'total_amount': amount + shipping_amount
    }
    return render(request, 'estore/cart.html', context)

def cart_total():
    amount = decimal.Decimal(0)
    cart_items = [item for item in Cart.objects.all()]
    if cart_items:
        for item in cart_items:
            temp_amount = (item.quantity * item.product.price)
            amount += temp_amount

    return amount

def add_to_cart(request):
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(Product, id=product_id)

    item_already_in_cart = Cart.objects.filter(product=product_id)
    if item_already_in_cart:
        cart_item = get_object_or_404(Cart, product=product_id)
        cart_item.quantity += 1
        cart_item.save()
    else:
        Cart(product=product).save()

    return redirect('estore:cart')

def remove_from_cart(request, cart_id):
    if request.method == 'GET':
        c = get_object_or_404(Cart, id=cart_id)
        c.delete()
    return redirect('estore:cart')

def increment_cart(request, cart_id):
    if request.method == 'GET':
        cart_item = get_object_or_404(Cart, id=cart_id)
        cart_item.quantity += 1
        cart_item.save()        
    return redirect('estore:cart')

def decrement_cart(request, cart_id):
    if request.method == 'GET':
        cart_item = get_object_or_404(Cart, id=cart_id)
        if cart_item.quantity == 1:
            cart_item.delete()
        else:
            cart_item.quantity -= 1
            cart_item.save()
    return redirect('estore:cart')

def verifyBalance(token, amount):
    url = '{{BASE_URL}}balances/' + token
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        res = json.loads(response.text)
        if float(res['gpa']['ledger_balance']) >= float(amount):
            return True, ""
        return False, "Insufficient balance!"
    return False, 'Your transaction can not be processed at this time!'

def verify(card_token, name, expiration, amount):
    url = '{{BASE_URL}}cards/' + card_token

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        res = json.loads(response.text)
        if expiration == res['expiration'] and name == res['fulfillment']['card_personalization']['text']['name_line_1']['value']:
            return verifyBalance(res['user_token'], amount)
        return False, 'Invalid card details!'
    return False, 'Your transaction can not be processed at this time!'

def getCardToken(pan, name, cvv_number, expiration, amount):
    url = '{{BASE_URL}}cards/getbypan'

    data = json.dumps({
        "pan": pan,
        "cvv_number": cvv_number
    })

    resp = requests.post(url, headers=headers, data=data)

    if resp.status_code == 200:
        res = json.loads(resp.text)
        isSuccess, message = verify(res['card_token'], name, expiration, amount)
        if isSuccess:
            return isSuccess, res['card_token']
        return isSuccess, message
    return False, 'Your transaction can not be processed at this time!'

def transaction(pan, name, cvv_number, expiration, amount):
    url = '{{BASE_URL}}simulate/authorization'

    isSuccess, data = getCardToken(pan, name, cvv_number, expiration, amount)

    if isSuccess:
        data = json.dumps({
            "amount": amount,
            "mid": '123456890',
            "card_token": data,
        })

        resp = requests.post(url, headers=headers, data=data)

        if resp.status_code == 201:
            return True, "Your transaction was successfully completed!"
        return False, 'Your transaction can not be processed at this time!'
    
    return isSuccess, data

def checkout(request):
    if request.method == 'POST':
        pan = request.POST.get("pan")
        name = request.POST.get("name")
        cvv_number = request.POST.get("cvvNumber")
        expiration =  request.POST.get("expiration")
        amount = request.POST.get("amount")

        isSuccess, message = transaction(pan, name, cvv_number, expiration, amount)

        context = {
            'isSuccess': isSuccess,
            'message': message,
            'date': datetime.now().strftime("%A, %B %d, %Y"),
            'name': name,
            'pan': pan,
            'cart_total': amount
        }

        if isSuccess:
            Cart.objects.all().delete()
            return render(request, 'estore/invoice.html', context)
        else:
            context['cvvNumber'] = cvv_number
            context['expiration'] = expiration
            return render(request, 'estore/checkout.html', context)

    context = {
        'cart_total': cart_total(),
        'isSuccess': True
    }
    return render(request, 'estore/checkout.html', context)