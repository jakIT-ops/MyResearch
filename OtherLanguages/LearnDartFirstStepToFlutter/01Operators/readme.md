# 1. Arithmetic Operators

```dart
main() {
  var operand1 = 10;
  var operand2 = 7;

  print(operand1 + operand2);
  print(operand1 - operand2);
  print(- operand1);
  print(operand1 * operand2);
  print(operand1 / operand2);
  print(operand1 ~/ operand2);
  print(operand1 % operand2);
}
```

### Prefix and Postfix Operators

```dart
main() {
  var prefixIncrement = 5;

  print(++prefixIncrement);
```
}

# 2. Equality and Relational Operators

### Relational Operators

```dart
main() {
  var operand1 = 10;
  var operand2 = 7;

  print(operand1 > operand2);
  print(operand1 < operand2);
  print(operand1 >= operand2);
  print(operand1 <= operand2);
}
```

###  Equality Operators

```dart
main() {
  var operand1 = 10;
  var operand2 = 7;

  print(operand1 == operand2);
  print(operand1 != operand2);
}
```

# Type Test Operators

```dart
main() {
  double type1 = 5.0;
  int type2 = 87;
  String type3 = "educative";
  bool type4 = true;

  print(type1 is int);
  print(type2 is int);
  print(type3 is String);
  print(type4 is double);
  print(type4 is! double);
}
```

# Assignment Operators

```dart
main() {
  var A = 10;
  var B = 7;

  print("Before using a compound assignment operator:");
  print(A);

  A += B;

  print("After using a compound assignment operator:");
  print(A);
}
```
`&=`, `~=`, .etc

# Logical Operators

```dart
main() {
  var A = true;
  var B = false;
  var expr = A && B; //false

  print(!A); // !true --> false
  print(!B); // !false --> true
  print(true || expr); // true || expr --> true
  print(false || expr); // false || expr --> expr
  print(true && expr); // true && expr --> expr
  print(false && expr); // false && expr --> false
}
```

# Bitwise and Shift Operators

```dart
main() {
  var A = 12;
  var B = 5;

  print(~A); // A complement
  print(~B); // B complement
  print(A & B); // A AND B
  print(A | B); // A OR B
  print(A ^ B); // A XOR B
  print(B << 2); // B Shift Left 2
  print(A >> 2); // A Shift Right 2
}
```
