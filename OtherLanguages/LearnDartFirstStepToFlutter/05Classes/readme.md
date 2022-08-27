# 1. Creating a Class in Dart

### Instance Variables

```dart
class Person{
  String name; // Declare name, initially null.
  String gender; // Declare gender, initially null.
  int age = 0; // Declare age, initially 0.
}
```

### Instance Methods

```Dart
class Person{
  String name; // Declare name, initially null.
  String gender; // Declare gender, initially null.
  int age = 0; // Declare age, initially 0.

  walking() => print('$name is walking');
  talking() => print('$name is talking');
}
```

# 2. Objects of a Class

```dart
class Person{
  String name;
  String gender;
  int age = 0;

  walking() => print('$name is walking');
  talking() => print('$name is talking');
}

int main() {
  // Creating an object of the Person class
  var firstPerson = Person();
}
```

### Using Class Members

```dart
class Person{
  String name;
  String gender;
  int age = 0;

  walking() => print('$name is walking');
  talking() => print('$name is talking');
}

int main() {
  var firstPerson = Person();

  firstPerson.name = "Sarah";
  firstPerson.gender = "female";
  firstPerson.age = 25;

  print(firstPerson.name);
  print(firstPerson.gender);
  print(firstPerson.age);
}
```

### Multiple Objects of the Same Class

```dart
class Person{
  String name;
  String gender;
  int age = 0;

  walking() => print('$name is walking');
  talking() => print('$name is talking');
}

int main() {
  var firstPerson = Person();

  firstPerson.name = "Sarah";
  firstPerson.gender = "female";
  firstPerson.age = 25;

  // Creating an object of the Person class
  var secondPerson = Person();
  secondPerson.name = "Ben";

  // Creating an object of the Person class
  var thirdPerson = Person();
  thirdPerson.name = "Martin";

  // Creating an object of the Person class
  var fourthPerson = Person();
  fourthPerson.name = "Hannah";

  // Driver Code
  print(firstPerson.name);
  print(secondPerson.name);
  print(thirdPerson.name);
  print(fourthPerson.name);
}
```

# 3. Constructors

### Generative Constructor

```dart
class Person{
  String name;
  String gender;
  int age;

  // Generative Constructor
  Person(String nameC, String genderC, int ageC){
    this.name = nameC;
    this.gender = genderC;
    this.age = ageC;
  }

  walking() => print('$name is walking');
  talking() => print('$name is talking');
}

int main() {
  var firstPerson = Person("Sarah","Female",25);
  print(firstPerson.name);
  print(firstPerson.gender);
  print(firstPerson.age);
}
```

### Syntactic Sugar

```dart
class Person{
  String name;
  String gender;
  int age;

  // Generative Constructor
  Person(this.name, this.gender, this.age);

  walking() => print('$name is walking');
  talking() => print('$name is talking');
}

int main() {
  var firstPerson = Person("Sarah","Female",25);
  print(firstPerson.name);
  print(firstPerson.gender);
  print(firstPerson.age);
}
```

### Named Constructor

```dart
class Person{
  String name;
  String gender;
  int age;

  // Generative Constructor
  Person(this.name, this.gender, this.age);

  // Named Constructor
  Person.newBorn(){
    this.age = 0;
  }

  walking() => print('$name is walking');
  talking() => print('$name is talking');
}

int main() {
  var firstPerson = Person("Sarah","Female",25);
  var secondPerson = Person.newBorn();
  print(secondPerson.age);
}
```

# 4. Getter and Setters

### Getters

```Dart
class Person{
  String name;
  String gender;
  int age;

  Person(this.name, this.gender, this.age);

  Person.newBorn(){
    this.age = 0;
  }

  // Getter function getting the value of name
  String get personName => name;

  walking() => print('$name is walking');
  talking() => print('$name is talking');
}

int main() {
  var firstPerson = Person("Sarah","Female",25);
  print(firstPerson.personName);
}
```

### Setters

```dart
class Person{
  String name;
  String gender;
  int age;

  String get personName => name;

  // Setter function for setting the value of age
  void set personAge(num val){
    if(val < 0){
      print("Age cannot be negative");
    } else {
      this.age = val;
    }
  }

  walking() => print('$name is walking');
  talking() => print('$name is talking');
}

int main() {
  var firstPerson = Person();
  firstPerson.personAge = -5;
  print(firstPerson.age);
}
```

# 5. Inheritance

```dart
class Product{
  String _name;
  num _price;
  String _expDate;

  Product(this._name, this._price, this._expDate);

  void printDetails(){
    print("Name: ${this._name}");
    print("Price: ${this._price}");
    print("Expiration Date: ${this._expDate}");
  }
}  

class Beverage extends Product{
  num _liters;
  String _type;

  Beverage(String name, num price, String expDate, this._liters, this._type) : super(name, price, expDate);

  void beverageDetails(){
    printDetails();
    print("Liters: ${this._liters}");
    print("Type: ${this._type}");
  }
}


int main() {
  var drink = Beverage("Minute Maid", 3.50, "01/01/2020", 1.75, "Orange Juice");
  drink.beverageDetails();
}
```
