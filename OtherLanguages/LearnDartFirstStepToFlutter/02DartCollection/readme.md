# 1. List: The Dart Array

```Dart
main() {
  var simpleList = [1,2,3];

  print(simpleList);
}
```


### Specifying the Type

```dart
main() {
  var listOfVegetables = List<String>();

  print(listOfVegetables is List<String>);
}
```

# 2. Working with Lists

### Accessing an Element

```dart
main() {
  var listOfVegetables = ['potato', 'carrot', 'cucumber'];

  print(listOfVegetables[1]);
}
```

### Finding the Length of a List

```dart
main() {
  var listOfVegetables = ['potato', 'carrot', 'cucumber'];

  print(listOfVegetables.length);
}
```

### Adding a Single Element

```dart
main() {
  var listOfVegetables = ['potato', 'carrot', 'cucumber'];

  listOfVegetables.add('cabbage');

  print(listOfVegetables);
}
```

### The `map()` Method

```dart
main() {
  var listOfVegetables = ['carrot', 'cucumber', 'zucchini'];
  var mappedVegetables = listOfVegetables.map((vegetable) => 'I love $vegetable');
  print(mappedVegetables);
}
```

# 3. Unordered Sets

```dart
main() {
  var setOfFruit = <String>{};
  print(setOfFruit);

  Set<String> anotherSetOfFruit = {};
  print(anotherSetOfFruit);
}
```

# 4. Working with Sets

```dart
main() {
  var setOfFruit = <String>{};

  setOfFruit.add('apples');
  setOfFruit.add('bananas');
  setOfFruit.add('oranges');

  print(setOfFruit);
}
```

### Finding the Length of a Set

```dart
main() {
  var setOfFruits = {'apples', 'bananas', 'oranges', 'watermelon', 'grapes'};

  print(setOfFruits.length);
}
```

### Removing Items from a Set

```Dart
main() {
  var setOfFruits = {'apples', 'bananas', 'oranges', 'watermelon', 'grapes'};

  // Remove 'bananas'
  setOfFruits.remove('bananas');

  print(setOfFruits);
}
```

# 5. Maps, Keys, Values

```dart
main() {
  var capitals = {
    'United States' : 'Washington D.C.',
    'England' : 'London',
    'China' : 'Beijing',
    'Germany' : 'Berlin',
    'Nigeria' : 'Abuja',
    'Egypt' : 'Cairo',
    'New Zealand' : 'Wellington'
  };

  // Driver Code
  print(capitals);
}
```

# 6. Working with Maps

```dart
main() {
  var numbers = Map<int, String>();

  numbers[1] = 'one';
  numbers[2] = 'two';
  numbers[3] = 'three';

  print(numbers);
}
```

### Finding the Number of Pairs in a Map

```Dart
main() {
  var numbers = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  };

  print(numbers.length);
}
```

### Removing a Key-Value Pair

```dart
main() {
  var capitals = {    
    'United States' : 'Washington D.C.',
    'England' : 'London',
    'China' : 'Beijing',
    'Germany' : 'Berlin',
    'Nigeria' : 'Abuja',
    'Egypt' : 'Cairo',
    'New Zealand' : 'Wellington'
  };   

  // Removing a key-value pair
  capitals.remove('China');

  print(capitals);  
}
```
