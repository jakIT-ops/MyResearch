# 1. Intersecing with Types, Interfaces, and Generics

TypeScript can manipulate types by combining any of them in one of several ways. The first way is to specify a type to be an intersection type, using an ampersand &. In the end, the type will have the sum of all members.

```ts
type T1 = { x: string };
type T2 = { y: number };
type T3 = { z: boolean };
type IntersectType1 = T1 & T2 & T3;
type IntersectType2 = T1 & T2;
type IntersectType3 = T3 & T1;
const inter1: T1 = { x: "x1", y: 2 }; // Won't compile: y does not exist in T1
const inter2: T1 & T2 = { x: "x1", y: 2 }; // Compile 
const inter3: IntersectType2 = { x: "x1", y: 2 }; // Compile
```

interfacs work well with intersections as well

```ts
interface I1 {
    x: string;
}
interface I2 {
    y: number;
}
interface I3 {
    z: boolean;
}
type IntersectWithInterface = I1 & I2 & I3;
const with3Interfaces: IntersectWithInterface = { x: "1", y: 1, z: true };
```

# 2. Literal Type, Narrowing, and Const

### Literal type

```ts
let x : "test"; 
let y : 123; 
let z : true; 
```

example 

```ts
interface Cat {
  kind: "cat", // Discriminant because shared with Dog
  name: string
}

interface Dog {
  kind: "dog", // Discriminant because shared with Dog
  nickname: string
}

function callMeBy(p: Cat | Dog): string {
  if (p.kind === "cat") { // In the IF, p is Cat
    return p.name;
  } else if (p.kind === "dog") { // In the IF, p is Dog
    return p.nickname
  }
  return "unknown";
}

const c: Cat = { kind: "cat", name: "Hello Kitty" }
const d: Dog = { kind: "dog", nickname: "Snoopy" }

console.log(callMeBy(c));
console.log(callMeBy(d));
```

### A second example

```ts
interface Success {
    success: true;
    httpCode: string;
    payload: string;
}
interface Failure {
    success: false;
    errorMessage: string;
}

function ajax(url: string): Success | Failure {
    return { success: false, errorMessage: "Error!" }; // Hardcoded failure
}
function ajaxCall(): string {
    const ajaxResult = ajax("http://blablac.com");
    if (ajaxResult.success === true) {
        return ajaxResult.payload; // Access to all Success  interface members
    } else {
        return ajaxResult.errorMessage; // Access to all Failure
    }
}
const result = ajaxCall();
```

### Literal type with <code>const</code>

```ts
const literalType1 = "c";    // Type is not string, but "c" 
const literalType2: "c" = "c";  // Same as above 
let literalType3 = "c";    // Type is string 
let literalType4: "c" = "c";    // Type is not string, but "c" 
```

# 3. Union with Types and Tagged Union

### Union type

```ts
let u1: string | boolean = true; 
type UStringBoolean = string | boolean; 
let u2: UStringBoolean = true; 
```

### The tagged union

```ts
interface InterfaceA {
    discriminant: "InterfaceA"; // This is not a string type, but InterfaceA type
    m0: number;
}
interface InterfaceB {
    discriminant: "InterfaceB"; // This is not a string type, but InterfaceB type
    m1: string;
}
interface InterfaceC {
    discriminant: "InterfaceC"; // This is not a string type, but InterfaceC type
    m2: string;
}
function unionWithDiscriminant(p: InterfaceA | InterfaceB | InterfaceC) {
    switch (
        p.discriminant // Only common members available
    ) {
        case "InterfaceA":
            console.log(p.m0); // Only InterfaceA members available
            break;
        case "InterfaceB":
            console.log(p.m1); // Only InterfaceB members available
            break;
        case "InterfaceC":
            console.log(p.m2); // Only InterfaceC members available
            break;
    }
}
```

# 4. Const Assertion for Literal Values

### const vs as const

```ts
const v1 = 10;
// v1 = 10; // Does not compile
let v2 = 10 as const;
v2 = 10;
```

### Array as const

```ts
// Const
const myArr1 = [1, 2, 3];
myArr1.push(4);
console.log(myArr1);

// myArr1 = []; // Doest not compile because const

```

### Object with <code>as const</code>

```ts
let immutable1 = { id: "1" } as const; 
// immutable1.id = 2; // Does not compile
// immutable1["newprop"] = 2; // Does not compile
console.log(immutable1);
```

```ts
let person = {
  id: 1,
  name: {
    first: "Patrick",
    last: "Desjardins",
    middleName: null
  },
  location: {
    country: "USA",
    state: "CA"
  },
  relatives: [
    {
      id: 2,
      name: {
        first: "Person2",
        last: "Person22",
        middle: "Mid"
      }
    }
  ]
} as const;

// Doest not compile:
// person.relatives.push({ id: 2, name: { first: "New", last: "New", middle: "" } });
// person.id = 4; 
```

# 5. Tuple For Type and Length Arrays

### Tuple syntax

```ts
let numberTuple: [number, number, number];
```

```ts
let myTuple: [number, string] = [0, "1"];
myTuple = [1, "test"];
const numberVariable: number = myTuple[0];
const stringVariable: string = myTuple[1];
```

### Transpilation effect

```ts
let myTuple: [number, string];
myTuple = [1, "test"];
myTuple[3] = "one more"; // Won't compile TS >= 2.7
myTuple[4] = 2; // Won't compile TS >= 2.7
myTuple[5] = true; // Won't compile (number|string only)
```

### Tuple length validation 

```ts
let firstTuple: [number, number] = [1, 2];
let secondTuple: [number, number, number] = [3, 4, 5];
secondTuple = firstTuple; // Doesn't compile type mismatch
firstTuple = secondTuple; // Doesn't compile length incompatible
```

### Readonly tuple 

```ts
let firstTuple: [number, number] = [1, 2];
let secondTuple: readonly [number, number,] = [3, 4];

firstTuple[0] = 100;
// secondTuple[0] = 1000; //Error! Read-only Tuple

console.log(firstTuple);
console.log(secondTuple);
```

# 6. Casting to Change Type

### Two ways to cast

```ts
const cast1: number = <number>1; 
```

```ts
const cast2: number = 1 as number;  
```

### The danger of casting

```ts
interface ICast1 {
    m1: string;
}
interface ICast2 {
    m1: string;
    m2: string;
}
let icast1: ICast1 = { m1: "m1" };
let icast2: ICast2 = { m1: "m1", m2: "m2" };
let icast3: ICast1 = icast2; // work without cast because of the structure
//icast2 = icast1; // doesn't work, miss a member
let icast4: ICast2 = icast1 as ICast2; // work but m2 undefined
console.log(icast4); // m2 is missing even if not optional
```

### Casting restrictions

```ts
interface ITypeA {
    m1: string;
}
interface ITypeB extends ITypeA {
    m2: string;
}
interface ITypeC extends ITypeB {
    m3: string;
}
const typea: ITypeA = { m1: "m1" };
const typeb: ITypeB = { m1: "m1", m2: "m2" };
let typeb2: ITypeB = typea as ITypeB; // Work (m2 will be missing!!!)
console.log(typeb2); // No m2
```

### Casting coercion

```ts
let aNumberToCast: number = 1; 
// let aString: string = aNumberToCast as string; // Doesn't work 
let aString: string = aNumberToCast as any as string; 
```

# 7. keyof to Validate a Member's Name

### Definition and goals

```ts
// Interface's members
interface InterfaceWithMembers {
    id: number;
    title: string;
    createdBy: Date;
}

const members: keyof InterfaceWithMembers = "id"; // Only accept id, title or createdBy

// Type's values
type TypeToKeyOf = "north" | "south" | "east" | "west";
function fKeyOfParameter(direction: TypeToKeyOf) {}
//fKeyOfParameter("no"); // Doesn't compile 
fKeyOfParameter("north");
```

### Use of generic

```ts
// Interface's members
interface InterfaceWithMembers {
    id: number;
    title: string;
    createdBy: Date;
}
const iWithMembersForKeyOf: InterfaceWithMembers = { id: 1, title: "1", createdBy: new Date() };
function prop<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}
const id = prop(iWithMembersForKeyOf, "id"); //the value 1 of type number
```

# 8. What is a Conditional Type?

TypeScript 2.8 brings the possibility of the conditional type. The conditional type creates a type by checking if an interface or an existing type extends a type or not. It uses the ternary operator (?:) to get the final type

### Using the conditional type with the dynamic number type

```ts
interface TypeA {
  kind: "TypeA";
  m1: string;
}
interface TypeB {
  kind: "TypeB";
  m2: number;
}

function fct<T extends TypeA | TypeB>(obj: T): T extends TypeA ? TypeB : TypeA {
  return obj as any; // Won't be any
}


let typeA: TypeA = { kind: "TypeA", m1: "abc" };
let returnA: TypeB = fct(typeA);
```

### Using the conditional type with generic

```ts
interface InterfaceBase {
    method1(): void;
}
interface InterfaceChild extends InterfaceBase {
    method2(): void;
}

type DynamicTypeFromCond = InterfaceChild extends InterfaceBase ? number : string;

let x: DynamicTypeFromCond = 3;
// let y: DynamicTypeFromCond = "123"; // Does not transpile
```

### Nested conditional type

```ts
type RemoveBoolean<T> = {
  [Key in keyof T]: boolean extends T[Key] ? never : Key
}[keyof T];

interface Inf1 {
  m1: string;
  m2: boolean;
  m3: number;
}

type NoBoolean1 = RemoveBoolean<Inf1>; // "m1" | "m3"
```

### Conditional type examples in TypeScript

```ts
type MyInclude<T, U> = T extends U ? T : never;
type MyExclude<T, U> = T extends U ? never : T;
```

# 9. Set and Dictionary

> Big O is a standard way to communicate the complexity of an algorithm. O(1) is the most efficient because it is constant regardless of how many elements you are manipulating.

### Index signatures

```ts
interface Person { id: number, name: string };

interface PersonDictionary {
  [id: number]: Person;
}

const dict: PersonDictionary = {
  [1]: { id: 1, name: "First" },
  [10]: { id: 10, name: "Tenth" },
};
console.log(dict[10].name);
```

```ts
interface Person { id: number, name: string };

interface MyDictionary<T> {
  [id: number]: T;
}

const dict: MyDictionary<Person> = {
  [1]: { id: 1, name: "First" },
  [10]: { id: 10, name: "Tenth" },
};
console.log(dict[10].name);
```

### Map

```ts
interface Person { id: number, name: string };
let myMap = new Map<number, Person>();
myMap.set(1, { id: 1, name: "First" });
myMap.set(10, { id: 10, name: "Tenth" });

if (myMap.has(10)) {
    console.log(myMap.get(10)!.name);
}
```

### The bang operator

```ts
if (myMap.has(10)) {
    console.log(myMap.get(10)!.name);
}
```


