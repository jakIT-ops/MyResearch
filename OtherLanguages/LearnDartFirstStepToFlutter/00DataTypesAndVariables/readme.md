# 1. Variables

```dart
main() {
  int myFirstDartVariable = 5;
}
```

### Printing Variables

```dart
main() {
  int myFirstDartVariable = 5;
  print(myFirstDartVariable);
}
```

# 2. Data Types

* Numbers
* Strings
* Booleans
* Lists
* Sets
* Maps
* Runes
* Symbols

# 3. Numbers

### The `num` Type

```DART
main() {
  num firstNumber = 5;
  num secondNumber = 5.1;
  num thirdNumber = firstNumber;

  // Driver Code
  print(firstNumber);
  print(secondNumber);
  print(thirdNumber);
}
```

### Integers

```DART
main() {
  int simpleInteger = 1;
  int hex = 0xDA34F;
  int integer = simpleInteger;

  // Driver Code
  print(simpleInteger);
  print(hex);
  print(integer);
}
```

### Doubles

```dart
main() {
  double simpleDouble = 1.1;
  double exponents = 1.42e5;

  // Driver Code
  print(simpleDouble);
  print(exponents);
}
```

# 4. Strings

## String Literals

```DART
main() {
  // Single Quotes
  print('Using single quotes');

  // Double Quotes
  print("Using double quotes");

  // Single quotes with escape character \
  print('It\'s possible with an escape character');

  // Double quotes
  print("It's better without an escape character");
}
```

# 5. String Interpolation

### String Concatenation

```dart
main() {
  String s1 = "First half of the string. ";
  String s2 = "Second half of the string";
  print(s1 + s2);
}
```

# 6. Boolean

```dart
main() {
  bool b1 = true;
  print(b1);
}
```

# 7. Type Inference and Annotation

### Syntax

```dart
main() {
  var bookTitle = "Lord of the Rings: The Fellowship of the Ring";
  var bookAuthor = "J. R. R. Tolkien";
  var bookNoOfPages = 423;

  // Driving Code
  print(bookTitle);
  print(bookAuthor);
  print(bookNoOfPages);
}
```

### Using Type Annotations

```dart
main() {
  var number = 3;
  print(number);

  number = 3.2;
  print(number);
}
```

### Dynamic Types

```dart
main() {
  dynamic dynamicVariable = 'A string'; // type String
  print(dynamicVariable);

  dynamicVariable = 5; // type int
  print(dynamicVariable);

  dynamicVariable = true; // type bool
  print(dynamicVariable);
}
```
