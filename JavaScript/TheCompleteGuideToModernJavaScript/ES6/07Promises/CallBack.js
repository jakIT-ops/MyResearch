const makePizza = (ingredients, callback) => {
    mixIngredients(ingredients, function(mixedIngredients)){
      bakePizza(mixedIngredients, function(bakedPizza)){
        console.log('finished!')
      }
    }
}
