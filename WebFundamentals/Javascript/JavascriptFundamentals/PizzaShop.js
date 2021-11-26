function pizzaOven (crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheese = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

var pizza1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni","sausage"]);
console.log(pizza1);

var pizza2 = pizzaOven("hand tossed", "marinara", ["mozarella", "feta"], ["mushrooms", "ollives", "onions"])
console.log(pizza2);

var pizza3 = pizzaOven("thin crust", "marinara", ["feta"], ["mushrooms", "ollives", "onions","artichokes"])
console.log(pizza3);

var pizza4 = pizzaOven("thick crust", "traditional", ["mozarella", "cheddar"], ["ollives", "onions"])
console.log(pizza4);


