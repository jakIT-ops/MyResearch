# 1. Aliases with the Structureal Behavior of TypeScript

### The Sturctural nature of TypeScript

```ts
interface MyTypeA {
  name: string; // Same property name-type than line 4 and 6
}
type MyTypeB = { name: string }; // Notice the name property is the same as the anonymous at line 6

function ouputName(obj: { name: string }): void { // Anonymous type for first parameter
  console.log(obj.name);
}

let typeA: MyTypeA = { name: "A" }; // TypeA
let typeB: MyTypeB = { name: "B" }; // TypeB
ouputName(typeA);
ouputName(typeB);
ouputName({ name: "C" }); // Also anonymous
```

### Adding an additional field

```ts
interface InterfaceA {
  name: string;
}

interface InterfaceB {
  name: string;
  id: number;
}

let intA: InterfaceA = { name: "A" };
let intB: InterfaceB = { name: "B", id: 2 };

function outputName(obj: { name: string }): void {
  console.log(obj.name);
}

outputName(intA);
outputName(intB);
```

# 2. Aliases with Type

### Type aliases for primitives

```ts
type IP = string;

function giveLenght(ip: IP): void {
  console.log(ip.length);
}

giveLenght("127.0.0.1"); // Works with a string that is an IP
giveLenght("NotI"); // Works with a string that is not an IP
const localHost:IP = "127.0.0.1"; 
giveLenght(localHost); // Works with IP
```

### Type aliases for unions

```ts
type ID = number | string | null;
function setId(id: ID): void { }
function getId(): ID { return null; }
function validId(id: ID): void { }
```

### Alias with a function type

```ts
function execute(code: (id: number, name: string) => boolean, error: (message: string) => void): void {
  if (!code(1, "Name1")) {
    error("Does not work");
  }
}

const myAlgorithm: (id: number, name: string) => boolean = (id: number, name: string): boolean => {
  return false;
}

const errorHandling: (message: string) => void = (message: string): void => {
  console.log(message);
}

execute(myAlgorithm, (errorHandling));
```

# 3. Aliases with Generic Types and Recursivity

### Generic types and aliases

```ts
interface Car<TOption> {
  name: string;
  options: TOption
}


type Car2<TOption> = {
  name: string;
  options: TOption
};

let c1: Car<string> = { name: "Vroom", options: "fast" };
let c2: Car2<string> = { name: "Pouttt", options: "slow" };

// Interchangeable because it is the same structure:
c1 = c2
```

### Recursive type with aliases

```ts
type Group = {
  name: string;
  child?: Group; // Refer to itself
};

let g: Group = {
  name: "G1",
  child: {
    name: "Generation1",
    child: {
      name: "Generation2"
    }
  }
};
```

### Type intersect

```ts
type Group = {
  name: string;
}

type Person = {
  firstName: string;
  lastName: string;
}

type Child<T> = {
  child: T;
}

type PersonGroupWithChild = Group & Person & Child<Person>;

let p: PersonGroupWithChild = {
  name: "GroupName",
  firstName: "Fist",
  lastName: "Last",
  child: {
    firstName: "ChildFirst",
    lastName: "ChildLast"
  }
};

console.log(p);
```

# 3. The Differences between Tyoe Aliases and interfaces

### Difference with classes

```ts
type Person = { name: string };
interface Person2 {
  name: string;
}

class Mother implements Person {
  name: string = "";
}

class Father implements Person2 {
  name: string = "";
}
```

### Difference with interfaces

```ts
interface Person { name: string };
interface Father extends Person { numberOfChildren: number };
let f1: Father = { name: "MisterF1", numberOfChildren: 2 };
```

### Accumulative difference

```ts
interface Person { // This interface could be in a third party package
  firstName: string;
}

interface Person { // This interface could be in your first party
  lastName: string;
}

let c: Person = { firstName: "First", lastName: "Last" };
```

# 4. Branded Alias

### Limitations

One strength of TypeScript is that it relies on structure, similar to how JavaScript does not rely on type names. However, in some circumstances, it can be a limitation. The main case is when we want to know the type of a specific object, for example, in order to access specific type properties or to compare another object.

### Branded type with a unique field

```ts
interface BaseClass {
  id: number;
}
interface Type1 extends BaseClass {
  _type1Brand: void;
}
interface Type2 extends BaseClass {
  _type2Brand: void;
}

let t1: Type1 = { id: 1 } as Type1;
let t2: Type2 = { id: 1 } as Type2;;

if (t1 === t2) {
  console.log("Same");
} else {
  console.log("Different");
}
```

### Branded type with literal type

```ts
interface TypeA {
  kind: "TYPEA"
  name: string;
  id: number;
}

interface TypeB {
  kind: "TYPEB"
  error: boolean;
}

let var1: TypeA = {
  kind: "TYPEA",
  name: "Variable1",
  id: 1
};

let var2: TypeB = {
  kind: "TYPEB",
  error: true
};


if (var1 === var2) { // Always will be false 
}
```


