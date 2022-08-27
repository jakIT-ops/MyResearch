# 1. Defining a Function

### Parameterized Functions

```DART
num sum(num x, num y){
  return x+y;
}

// Driver Code
main() {
  print(sum(1,2));
}  
```

### Syntactic Suga

```DART
num sum(num x, num y) => x+y;

// Driver Code
main() {
    print(sum(1,2));
}
```

# 2. Calling a Function

### A Simple Function Call

```dart
// Print the statement "Function Called"
void newPrint(){
  print("Function Called");
}

// Return the sum of two numbers
num sum(num x, num y){
  return x+y;
}

main() {
  // Calling newPrint
  newPrint();

  //Calling sum
  var result = sum(5,3);
  print(result);
}
```

### Calling Functions within Functions

```dart
num square(num x) {
  return x * x;
}

main() {
  // Driver Code
  var result = square(5);
  print(result);
}
```

# 3. Optional Parameters

### Named Parameters

```dart
printer(num n,{String s1, String s2}) {
  print(n);
  print(s1);
  print(s2);
}
```

### Positional Parameters

```dart
String mysteryMessage(String who, [String what, String where]){
  var message = '$who';
  if(what != null && where == null){
    message = '$message said $what';
  } else if (where != null){
    message = '$message said $what at $where';
  }
  return message;
}
```
```dart
String mysteryMessage(String who, [String what, String where]){
  var message = '$who';
  if(what != null && where == null){
    message = '$message said $what';
  } else if (where != null){
    message = '$message said $what at $where';
  }
  return message;
}

main() {
  var result = mysteryMessage('Billy', 'howdy');
  print(result);
}
```

# 4. Recursive Functions

### Dart’s Implementation

```dart
int factorial(int x) {
  if (x == 1) { // Base Case
    return 1;
  } else {
    return x*factorial(x-1); // Recursive Call
  }
}

main() {
  // Driver Code
  var result = factorial(5);
  print(result);
}
```

# 5. Higher-Order Functions

```dart
List<int> forAll(Function f, List<int> intList){
  var newList = List<int>();
  for(var i = 0; i < intList.length; i ++){
    newList.add(f(intList[i]));
  }
  return newList;
}
```

# 6. Anonymous Functions

```dart
main() {
  var list = [1,2,3];
  list.forEach((item) {
   print(item*item*item);
  });
}
```

# 7. Nested Functions

```dart
void outerFunction(){
    print("Outer Function");
    void nestedFunction(){
      print("Nested Function");
    }
    nestedFunction();
}

main() {
  outerFunction();
}
```

# 8. Scope

```dart
int square(int x){
  return x * x;
}

main() {
  var amIVisible = 0;

  void result() {
    var amIVisible = square(3);
    print("Variable Inside Block: $amIVisible");
  }

  result();
  print("Variable Outside Block: $amIVisible");
}
```
