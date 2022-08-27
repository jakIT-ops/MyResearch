# 1. Immutable Data with Readonly

### The <code>Object.freeze</code>  function

```ts
// The interface that we want to have readonly without defining another interface
interface OriginalInterface {
    x: number;
    y: string;
}

// The mapped type that map a generic type with the readonly constraint
type ReadonlyInterface<T> = { readonly [P in keyof T]: T[P] };
```

### Adding generic using mapped

```ts
// The interface that we want to have readonly without defining another interface
interface OriginalInterface {
    x: number;
    y: string;
}

// The mapped type that map a generic type with the readonly constraint
type ReadonlyInterface<T> = { readonly [P in keyof T]: T[P] };

// Function that convert the object from one type to another
function genericInterfaceToReadOnly<T>(o: T): ReadonlyInterface<T> {
    return Object.freeze(o);
}

const original: OriginalInterface = { x: 0, y: "1" };
const originalReadonly = genericInterfaceToReadOnly(original);
// originalReadonly.x = 3; // error TS2540: Cannot assign to 'x'
```

# 2. Partial

### The <code>Partial</code> mapped type and setting properties to optional

```ts
type Partial<T> = {
    [P in keyof T]?: T[P];
}
```

```ts
type ReadonlyInterface<T> = { readonly [P in keyof T]: T[P] };
```

# 3. Nullable 

### Nullable mapped type 

Another possibility with the mapped type is that it can handle null. Similar to the optional Partial<T>, you can create your own Nullable<T>. To create your own type, the first step is to build it with no generic (without <T>, a plain interface or type) and then adjust it by adapting with a generic parameter (e.g. <T>).

### Intermediary step: Two interfaces into a specific nullable type

intermediary step with the union of null

```ts
interface Cat {
  age: number;
  weight: number;
  numberOfKitty: number;
}

const cat1: Cat = { age:1, weight: 2, numberOfKitty: 0 };

// NullableCat1 have union with the null type. It allows to visualize the dual type.
interface NullableCat1 {
  age: number | null;
  weight: number | null;
  numberOfKitty: number | null;
}
```

mapped type strongly associated with the interface. Cat

```ts
interface Cat {
  age: number;
  weight: number;
  numberOfKitty: number;
}

const cat1: Cat = { age: 1, weight: 2, numberOfKitty: 0 };

// The nullable cat is now a mapped type.
type NullableCat = { [P in keyof Cat]: Cat[P] | null };

const cat2: NullableCat = { age: 1, weight: null, numberOfKitty: null };
```

### Generic nullable mapped type

Mapped type with generic

```ts
interface Cat {
  age: number;
  weight: number;
  numberOfKitty: number;
}

const cat1: Cat = { age: 1, weight: 2, numberOfKitty: 0 };

// The mapped type that goes beyond Cat with generic <T>
type Nullable<T> = { [P in keyof T]: T[P] | null };

const cat2: Nullable<T> = { age: 1, weight: null, numberOfKitty: null };
```

# 4. Pick

### Description of <code>Pick</code>

```ts
// An interface that defines fields for an Animal
interface Animal {
  age: number;
  numberOfLegs: number;
  canSwim: boolean;
  runningSpeed: number;
  name: string;
}

// An interface that defines fields for a Fish
interface Fish {
  age: number;
  name: string;
}
```

### The inheritance problem

```ts
// An Animal has all fields from Fish
interface Animal extends Fish{
  numberOfLegs: number;
  canSwim: boolean;
  runningSpeed: number;
}

// Fish schema
interface Fish {
  age: number;
  name: string;
}
```

### Improvement of the inheritance solution

An inheritance structured in a better way

```ts
interface Animal {
  age: number;
  name: string;
}

interface Fish extends Animal {
  maximumDeepness: number;
}

interface Felin extends Animal {
  numberOfLegs: number;
  canSwim: boolean;
  runningSpeed: number;
}
```

### <code>Pick</code> for a dynamic type creation

Getting a Fish without defining the fist interface

```ts
interface Animal {
  age: number;
  name: string;

  maximumDeepness: number;

  numberOfLegs: number;
  canSwim: boolean;
  runningSpeed: number;
}

function buyAFish(fishEntity: Pick<Animal, "age" | "name" | "maximumDeepness">) {
  console.log(fishEntity);
}

buyAFish({
  age: 1,
  name: "Clown Fish",
  maximumDeepness: 10
})
```

### <code>Pick</code> usage with <code>KeyOf</code>

Defining the Fish Type without duplicating fields' name

```ts
// Interface with all Animal fields
interface Animal {
    age: number;
    name: string;

    maximumDeepness: number;

    numberOfLegs: number;
    canSwim: boolean;
    runningSpeed: number;
}

// Fish type built upon Animal
type Fish = Pick<Animal, "age" | "name" | "maximumDeepness">;

function buyAFish(fishEntity: Fish) {
    console.log(fishEntity);
}

buyAFish({
    age: 1,
    name: "Clown Fish",
    maximumDeepness: 10,
});
```

### A better solution with <code>Pick</code>

```ts
interface Animal {
    age: number;
    name: string;

    maximumDeepness: number;

    numberOfLegs: number;
    canSwim: boolean;
    runningSpeed: number;
}

function transformAnAnimationToAFish(fishEntity: Animal): Pick<Animal, "age" | "name" | "maximumDeepness"> {
    return fishEntity;
    // return { age: 1, name: "name", maximumDeepness: 123, otherStuff: "no too fast" };
}

console.log(
    transformAnAnimationToAFish({
        age: 1,
        name: "Clown Fish",
        maximumDeepness: 10,
        numberOfLegs: 0,
        canSwim: true,
        runningSpeed: 0,
    })
);
```

### An alternative with a big constraint

An alternative with a constraint

```ts
interface Animal {
    age: number;
    name: string;

    maximumDeepness: number;

    numberOfLegs: number;
    canSwim: boolean;
    runningSpeed: number;
}
interface Human {
    age: number;
    name: string;
}

// Create a Type from the intersection of Animal and HUman that will be of type string
type LivingThing = Record<Extract<keyof Animal, keyof Human>, string>;
const creature: LivingThing = {
    age: "1",
    name: "John",
};
console.log(creature);
```

# 5. Omit

```ts
interface Animal {
    age: number;
    name: string;

    maximumDeepness: number;

    numberOfLegs: number;
    canSwim: boolean;
    runningSpeed: number;
}

// Parameter using Omit to remove three fields
function buyAFish(fishEntity: Omit<Animal, "numberOfLegs" | "canSwim" | "runningSpeed" >) {
    console.log(fishEntity);
}

buyAFish({
    age: 1,
    name: "Clown Fish",
    maximumDeepness: 10,
});
```

# 6. Record

### Decription of <code>Record</code> 

```ts
// Create a type with three string fields
type RecordType1 = Record<"m1" | "m2" | "m3", string>;
// Instantiate a variable from the type
const x: RecordType1 = { m1: "s1", m2: "s2", m3: "s3"};
console.log(x);
```

### When to use <code>Record</code>

```ts
// An interface with many fields of many types
interface Animal {
    age: number;
    name: string;

    maximumDeepness: number;

    numberOfLegs: number;
    canSwim: boolean;
    runningSpeed: number;
}

// A function that need to take all the animal fields but from a string type
function receiveInputFromUser(dataIn: Record<keyof Animal, string>): Animal{
    const wellTypedObject: Animal = {
        age: Number(dataIn.age),
        name: dataIn.name,
        maximumDeepness: Number(dataIn.maximumDeepness),
        numberOfLegs: Number(dataIn.numberOfLegs),
        canSwim: Boolean(dataIn.age),
        runningSpeed: Number(dataIn.runningSpeed),
    }
    return wellTypedObject;
}
console.log(receiveInputFromUser({
    age: "13",
    name:"Fish",
    numberOfLegs: "2",
    maximumDeepness : "123",
    canSwim : "true",
    runningSpeed : "0"
}));
```

# 7. Extract 

### Description of <code>Extract</code>

```ts
type OnlyArrayType = Extract<string | string[] | number[], unknown[]>;

const var1: OnlyArrayType = ["Element1"];
const var2: OnlyArrayType = [1];
// const var3: OnlyArrayType = "No";
```

# 8. Exclude

###Exclude vs Extract

The <code>Exclude</code> mapped type is similar to <code>Extract</code> in the sense that it builds a type by selecting several properties. However, contrary to Extract, Exclude takes all the properties from a type and removes the specified one, instead of starting from nothing and adding the specified properties.

```ts
interface Animal {
    name: string;
    gender: string;
    sound: string;
}
interface Human {
    name: string;
    gender: string;
    nickname: string;
}

// type LivingThing = Extract<keyof Animal, keyof Human>;
type LivingThing = Exclude<keyof Animal, "sound">;
function sayMyName(who: Record<LivingThing, string>): void {
    console.log(who.name +" is of type " + who.gender);
}
const animal: Animal = { name: "Lion", sound: "Rawwwhhh", gender: "Male" };
const human: Human = { name: "Jacob", nickname: "Jaco-bee", gender: "Boy" };
sayMyName(animal);
sayMyName(human);
```

### Exclude vs Pick

While the examples of Extract and Exclude borrow the Record mapped type, it is not a necessity. For example, we can create a HumanWithoutNickname type by using Exclude and Pick.

```ts
interface Animal {
    name: string;
    gender: string;
    sound: string;
}
interface Human {
    name: string;
    gender: string;
    nickname: string;
}

interface NoisyLivingSpecies{
    sound: string;
}
type LivingThing = Exclude<keyof Animal, keyof NoisyLivingSpecies>;
type HumanWithoutNickname = Pick<Human, LivingThing>;
```

# 9. Return Type 

### Extracing thee return type of a function

```ts
function getName(): string {
    return "Name";
}
type FunctionType = ReturnType<typeof getName>;
const varX:FunctionType = "This is a string";
console.log(varX);
```

```ts
function getName(): { firstName: string, lastName: string } {
  return { firstName: "John", lastName: "Doe" };
}
type FunctionType = ReturnType<typeof getName>; // Not a string anymore
const varX: FunctionType = "This is a string"; // TypeScript won't compile
console.log(varX);
```

### ReturnType with many return types

```ts
function getSomething() {
    if (Math.random() < 0.5) {
        return {
            cond: "under 0.5",
            typeScript: true,
        };
    } else {
        return {
            cond: 1,
            typeScript: "3.7",
            moreField: true
        };
    }
}
type functionType2 = ReturnType<typeof getSomething>;
```

### <code>ReturnType</code> with asynchrounous functions

```ts
async function asyncFunction(){
    return await Math.random();
}
type functionType4 = ReturnType<typeof asyncFunction>; // Promise<number>
type functionType5 = ReturnTypeFromPromise<functionType4>; // number

type ReturnTypeFromPromise<T> = T extends Promise<infer U> ? U : T;
```

# 10. Custom Mapped Type

### Creating a "NonNullable" type

```ts
type NoNullValue<T> = T extends null | undefined
  ? never
  : T;

function print<T>(p: NoNullValue<T>): void {
    console.log(p);  
}

print("Test"); // Compile
// print(null); // Does not compile
```

### Adding a property conditionally

```ts
interface Person {
    name: string;
    dateCreated: Date;
}
interface Animal {
    name: string;
}

// Create a generic Type that add modifiedDate only if dateCreated is present
type Modified<T> = T extends { dateCreated: Date } ? T & { modifiedDate: Date } : never;

const p: Person = { name: "Pat", dateCreated: new Date() };
const a: Animal = { name: "Jack" };

// ModifiedDate present because "Person" has dateCreated
const p2: Modified<Person> = { ...p, modifiedDate: new Date() }; 
console.log(p2.modifiedDate)

// Following line do not transpile because Animal does not have dateCreated
// const a2: Modified<Animal> = { ...p, modifiedDate: new Date() };
// console.log(a2.modifiedDate)
```


