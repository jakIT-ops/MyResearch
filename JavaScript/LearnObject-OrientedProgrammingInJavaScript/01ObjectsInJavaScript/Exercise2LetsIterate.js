var product = {
    name: 'Cheese',
    price: 20,
    amount: 10,
    madeIn: 'USA'
}
function set(){
    for (x in product){
        if (x == "name"){
            product.name= 'Bottle'
        }
        else if(x == "madeIn"){
            product.madeIn = 'China'
        }
        
    }
}