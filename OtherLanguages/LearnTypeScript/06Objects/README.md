# 1. Introduction to TypeScript's Many Objects

TypeScript has many different object types.

In this section, we will see the difference between the two objects which are confusingly called Object and object – one that starts with an uppercase O and another with a lowercase o.

```ts
let o1: Object = "I am an Object";
let o2: object = { text: "I am an object" };
let o3: Object = { text: "I am also an Object" }
let o4: object = ["I", "am", "an", "object"];
let o5: Object = ["I", "am", "an", "Object"];

console.log(o1);
// console.log(o2.text); // Does not compile
// console.log(o3.text); // Does not compile
console.log(o4);
console.log(o5);
```

```ts
let curly1 = { text: "An object" };
let curly2: { text: string } = { text: "An object" };
let curly3: {} = { text: "An object" };

console.log(curly1.text);
console.log(curly2.text);
// console.log(curly3.text); // Does not not compile
```

```ts
let create1 = Object.create({ text: "I am a created object" });
let p = { text: "I am an object" };
let create2 = Object.create(p);

console.log(create1.text);
console.log(p.text);
console.log(create2.text);
```

# 2. The Curly Braces Object

TypeScript can create an object using the curly braces – it is an object literal like in JavaScript. The limitation is that you must define every member at initialization time.

The advantage is that it’s a quick way to organize data. It’s also a natural way to organize data coming from a JSON Payload. For example, executing a request to receive a payload will provide you with a literal object.

TypeScript is a structural language and does not need to have a name. This works great for cases where you do not need to map all the data to a type. With a structural type, you can cast the data and have the structure mapped for you without having to instantiate anything.

```ts
let x: { x: number; y: string } = { x: 1, y: "2" }; // Below code is similar, but reusable with a type (as interface)
interface MyTypeWithTwoMembers {
    x: number;
    y: string;
}
let x2: MyTypeWithTwoMembers = { x: 1, y: "2" };
```

# 3. Objects


### Instantiating a class into an object

```ts
class MyClass{
    private value: string;
    constructor(val:string){
        this.value = val;
    }
}
const c = new MyClass("ABC");
```

### Object-oriented possibilities

```ts
interface MyContract {
  id: number;
}

class ContractTypeA implements MyContract {
  constructor(public id: number){}
}

class ContractTypeB implements MyContract {
  constructor(public id: number){}
}

function showContractId(c: MyContract): void {
  console.log(c.id);
}

const c1 = new ContractTypeA(1);
const c2 = new ContractTypeB(2);
showContractId(c1);
showContractId(c2);
```

# 4. Lowercase vs UpperCase Object

### Lowercase <code>object</code>

```ts
let o: object;
o = 1; // Primitive = does not work
o = { a: "123" }; // Anonymous object = work
interface MySchema {
    val: string;
}
let interfaceObject: MySchema = { val: "Test" };
o = interfaceObject; // Typed object = work
o = null; // Does not work
o = undefined; // Does not work
let x = new Array();
o = x; // "new" object = work
```

### Uppercase <code>Object</code>

```ts
    let x = { y: 1 };
    let obj: Object = x;
    console.log(obj.toString());
```



