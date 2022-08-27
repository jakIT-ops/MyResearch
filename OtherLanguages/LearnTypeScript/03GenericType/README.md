# 1. Generic 

Generic allows for improved reusability by parameterizing a type with another one. A popular front-end framework named React can have an unlimited number of components. They all have properties that are unique to their components. It would be tedious to have to inherit a base class or alter the framework to accommodate all potentials possibilities. Hence, the properties of these React components use a generic.

```ts
// Generic Component that has properties that can change depending of the implementation
interface MyComponent<TProps> {
  name: string;
  id: number;
  props: TProps;
}

// First property that has a string
interface Props1 {
  color: string;
}

// Second property that has a number
interface Props2 {
  size: number;
}

// First component that has color in property because it is generic with Props1
const component1: MyComponent<Props1> = {
  name: "My Component One",
  id: 1,
  props: { color: "red" }
};

// Second component that has size in property because it is generic with Props2
const component2: MyComponent<Props2> = {
  name: "My Component Two",
  id: 2,
  props: { size: 100 }
};

console.log(component1);
console.log(component2);
```

### Generic and list

```ts
let list1: number[] = [1, 2, 3];
list1.push(4); // Can only push number
console.log(list1);

let list2: any[] = [1, 2, 3];
list2.push("Here_is_a_string");
console.log(list2); // You can push any type of value
```

### Generic vs any

```ts
const a: Array<string> = new Array("abc", "def"); 
const s: string = a[0]; // No cast required 
console.log(s.substr(0,1)); // Access to string members 
// a
```

```ts
const a2: Array<any> = new Array("abc", "def");
const s2 = a2[0]; // No cast required 
console.log(s2.substringg(0, 1)); // TypeScript does not safe guard
// 
```

# 2. Generic and Classes

Engineers with an object-oriented background may associate the concept of generic with classes. It is a mechanism to generalize a class, to avoid duplicating the definition for each flavor of a class.

```ts
// Three classes
class Human {
    public greeting: string = "Hello";
}
class Lion {
    public greeting: string = "Grrrrrr";
}
class Tulip {
    public greeting: string = "...";
}

// The class needs to use a specifies but is limited to Human
class LivingSpecies_1 {
    public species: Human; // Human only :(

    constructor(species: Human) {// Human only :(
        this.species = species;
    }
    public sayHello(): void {
        console.log(this.species.greeting);
    }
}
const species1 = new LivingSpecies_1(new Human());
species1.sayHello();
```

### Adding an <code>interface</code> to our <code>classs</code>

```ts
// Three classes that inherit a common one
interface Greeter {
    greeting: string;
}
class Human implements Greeter { // Implement the common interface
    public greeting: string = "Hello";
}
class Lion implements Greeter {// Implement the common interface
    public greeting: string = "Grrrrrr";
}
class Tulip { // Does not implement the common interface
    public greeting: string = "...";
}

// Not limited to Human! Now any type that inherits Greeter
class LivingSpecies {
    public species: Greeter;

    constructor(species: Greeter) {
        this.species = species;
    }
    public sayHello(): void {
        console.log(this.species.greeting);
    }
}
const species1 = new LivingSpecies(new Human());
species1.sayHello();
const species2 = new LivingSpecies(new Lion());
species2.sayHello();
const species3 = new LivingSpecies(new Tulip());
species3.sayHello();
```

### Generic to the rescue

```ts
interface Greeter {
    greeting: string;
}
class Human implements Greeter {
    public humanFunction() {
        console.log("Executing a human function");
    }
    public greeting: string = "Hello";
}
class Lion implements Greeter {
    public greeting: string = "Grrrrrr";
    public lionAttack() {
        console.log("Attacking like a lion");
    }
}
class Tulip {
    public greeting: string = "...";
    public lookingGood() {
        console.log("Snazzy Flower am I");
    }
}
class LivingSpecies<T> {
    public species: T;

    constructor(species: T) {
        this.species = species;
    }
    public getSpecies() {
        return this.species;
    }
}
const species1 = new LivingSpecies(new Human());
species1.getSpecies().humanFunction();
const species2 = new LivingSpecies(new Lion());
species2.getSpecies().lionAttack();
const species3 = new LivingSpecies(new Tulip());
species3.getSpecies().lookingGood();
```

# 3. Generic Outside Class

### Generic with function

```ts
function countElementInArray<T>(elements: T[]): number {
    return elements.length;
}

function returnFirstElementInArray<T>(elements: T[]): T | undefined {
    if (elements.length > 0) {
        return elements[0];
    }
    return undefined;
}
const arr = [1, 2, 3];
console.log(countElementInArray(arr));
console.log(returnFirstElementInArray(arr));
```

### The <code>unknown</code> type as an alternative

```ts
function countElementInArray(elements: unknown[]): number {
    return elements.length;
}

function returnFirstElementInArray(elements: unknown[]): unknown | undefined {
    if (elements.length > 0) {
        return elements[0];
    }
    return undefined;
}
const arr = [1, 2, 3];
console.log(countElementInArray(arr));
console.log(returnFirstElementInArray(arr));
```

### Generic to the rescue

```ts
function returnFirstElementInArray<T>(elements: T[]): T {
    return elements[0];
}
const arr = [1, 2, 3];
const bigger = returnFirstElementInArray(arr) * 10;
console.log(bigger);

const arr2 = ["Test", "is", "good"];
const first = returnFirstElementInArray(arr2);
console.log(arr2.indexOf(first))
```
























































