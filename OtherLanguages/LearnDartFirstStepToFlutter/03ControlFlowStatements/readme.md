# 1. The if Statement

```dart
main() {
  var testList = [2,4,8,16,32];
  print(testList);

  if(testList.isNotEmpty){
    print("Emptying List");
    testList.clear();
  }

  print(testList);
}
```

# 2. else and else if

```dart
main() {
  var pointsA = 50;
  var pointsB = 64;

  if(pointsA > pointsB){
    print("Team A Wins!");
  } else {
    print("Team B Wins!");
  }
}
```

# 3. Ternary Operator

```dart
main() {
  var a = 5;
  var b = 2;

  var result = a > b ? a - b : b - a;
  print(result);
}
```

# 4. for Loops

```dart
main() {
  for(var i = 0; i < 5; i++){
    print(i);
  }
}``
```

### Conditions with Loops

```dart
main() {
  var intList = [6,7,3,9,2,5,4];

  for(var i in intList){
    if(i % 2 == 0){
      print(i);
    }
  }
}
```

# 5. while Loops

```dart
main() {
  var count = 1;
  while (count <= 10) {
    print(count);
    count += 1;
  }
}
```

```dart
main() {
  var alwaysOne = 1;
  do {
    print("Using do-while: $alwaysOne");
  } while (alwaysOne != 1);
}
```

# 6. break and continue

The `break` Statement

```dart
main() {
  var intList = [7,3,9,6,2,5,4];

  for(var element in intList){
    if(element % 2 == 0){
      print(element);
      break;
    }
  }
}
```

The `continue` Statement

```dart
main() {
  var experience = [5,1,9,7,2,4];

  for(var index = 0; index < experience.length; index++){
    var candidateExperience = experience[index];
    if(candidateExperience < 5){
      continue;
    }
    print("Call candidate $index for an interiew.");
  }
}
```

# 7. switch and case

```dart
main() {
  var command = 'OPEN';

  switch(command) {
    case 'CLOSED':
      print('closed');
      break;
    case 'PENDING':
      print('pending');
      break;
    case 'APPROVED':
      print('approved');
      break;
    case 'DENIED':
      print('denied');
      break;   
    case 'OPEN':
      print('open');
      break;
    default:
      print('command unknown');
  }
}
```
