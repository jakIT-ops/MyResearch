# 1. Creating a Braintree Gateway

### Braintree gateway

The first step is to connect our server with the Braintree gateway. In the code below, we use the `braintree.BraintreeGateway()` method on lines 3–10 to achieve this task. The method takes all the API keys (i.e., Merchant ID, Public Key, and Private Key) associated with the Braintree sandbox account (lines 6–8). The API keys allow Braintree to uniquely identify the Braintree account linked with the server.

The `braintree.BraintreeGateway()` method returns a gateway object specific to that server. The server then uses this gateway object to securely interact with the Braintree server.

```js
import braintree

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="{{merchant_id}}",
        public_key="{{public_key}}",
        private_key="{{private_key}}"
    )
)

print ("Gateway has been created successfully!")
print(gateway)
```

# 2. Generating a Client Token

When a customer arrives on our application, our server is responsible for generating a client token that contains all the authorization and configuration information. The application needs the client token to initialize the client SDK to communicate with Braintree.

The process of generating a client token at the server consists of two steps:

1. Create a new customer.

2. Generate a client token.

### Create a customer

To create a new customer, we call the `customer.create()` method in lines 12–20. This method returns a `customer` object. We print the id of that customer in line 22.

```js
import braintree

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="merchant_id",
        public_key="public_key",
        private_key="private_key"
    )
)

newCustomer = gateway.customer.create({
    "first_name": "Jen",
    "last_name": "Smith",
    "company": "Braintree",
    "email": "jen@example.com",
    "phone": "312.555.1234",
    "fax": "614.555.5678",
    "website": "www.example.com"
})

print("customer_id: {}".format(newCustomer.customer.id))
```

### Generate a client token

After creating a customer, we generate the client token by calling the `client_token.generate()` method in lines 12–14. This method takes the customer ID as a parameter. In line 16, we print the value of the generated client token.

```js
import braintree

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="merchant_id",
        public_key="public_key",
        private_key="private_key"
    )
)

client_token = gateway.client_token.generate({
    "customer_id": "{{customer_id}}"
})

print("client_token: {}".format(client_token))
```

# 3. Receiving the Payment Method Nonce

### POST request handler

The client sends the payment method nonce to our server using a POST request. The implementation of the POST request handler for receiving the payment method nonce from the client is shown in the code below

### Fake valid nonce

However, to proceed with our implementation, we have used fake-valid-nonce in line 19, which is a valid payment method nonce provided by Braintree that can be used to create transactions.

```js
import braintree

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="merchant_id",
        public_key="public_key",
        private_key="private_key"
    )
)

"""
@app.route("/checkout", methods=["POST"])
def create_purchase():
    nonce_from_the_client = request.form["payment_method_nonce"]
    # Use payment method nonce here...
"""

nonce = "fake-valid-nonce"

print("payment_method_nonce: {}".format(nonce))
```

# 4. Creating a Transaction

To create a transaction, we use the `transaction.sale()` method from the Braintree gateway. This method requires, at least, the following two parameters:

1. Amount

2. Payment method nonce

```js
import braintree

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="merchant_id",
        public_key="public_key",
        private_key="private_key"
    )
)

result = gateway.transaction.sale({
    "amount": "20.0",
    "order_id": "{{order_id}}",
    "payment_method_nonce": "{{payment_method_nonce}}",
    "options": {
        "submit_for_settlement": True,
    }
})

if result.is_success:
    print("Transaction has been created successfully!")
else:
    print("Creating transaction failed")
```

# 5. Creating a Transaction

### Create a transaction

To create a transaction, we use the transaction.sale() method from the Braintree gateway. This method requires, at least, the following two parameters:

1. Amount

2. Payment method nonce

```js
import braintree

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="merchant_id",
        public_key="public_key",
        private_key="private_key"
    )
)

result = gateway.transaction.sale({
    "amount": "20.0",
    "order_id": "{{order_id}}",
    "payment_method_nonce": "{{payment_method_nonce}}",
    "options": {
        "submit_for_settlement": True,
    }
})

if result.is_success:
    print("Transaction has been created successfully!")
else:
    print("Creating transaction failed")
```

### Search transactions

In the example above, we specified an order_id while making a transaction. Now, we can use this order_id to search for transactions using the transaction.search() method. This method returns a collection of transaction response objects against a given order_id.

In the code below, in lines 12–14, we are using the transaction.search() method to retrieve all the transactions specified by order_id. Please note that we have used order_id as a text field. Braintree supports the following three types of search fields:

1. Text fields

2. Multiple value fields

3. Range fields

Details about these fields can be found here.

Apart from order_id, we can use several other parameters to search for transactions (e.g., credit card type, credit cardholder name, customer location, amount, and many more). A list of these parameters can be found here.

After retrieving the transactions against an order_id, we printed all transaction response objects in lines 16–17. Instead of printing the whole object, you can print some specific data related to a transaction. For example:

* Transaction amount using transaction.amount

* Date/time (when the transaction object was created) using transaction.created_at

* Details of the card used for the transaction using transaction.credit_card_details

```js
import braintree

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="merchant_id",
        public_key="public_key",
        private_key="private_key"
    )
)

transactions = gateway.transaction.search(
        braintree.TransactionSearch.order_id == "{{order_id}}"
    )

for transaction in transactions.items:
    print(transaction)
```


