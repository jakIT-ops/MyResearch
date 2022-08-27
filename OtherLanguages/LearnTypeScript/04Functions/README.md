# 1. Definition 

### Functions and TypeScript

Functions are at the core of JavaScript. The language is function-scoped. TypeScript doesn’t make any changes in this regard and embraces the use of a class to delimit scope, which is also a feature of ECMAScript 2015.

* Review how you can define functions in TypeScript and draw parallels to JavaScript.
* See how TypeScript enhances functions by providing strong signatures that define parameters and return types.
* Explore the outline of the this pointer which is often confusing but simplified with TypeScript.


### Functions and Keyword 

```ts
function fctNamedFunction1() { // Named Function
  console.log("Named Function 1");
}

let f1 = function fctNamedFunction2() { // Named Function
  console.log("Named Function 2");
};

let f2 = function () { // Anonymous Function
  console.log("Anonymous Function 1");
};

(function () { // Anonymous Function + Automatically invoked
  console.log("Anonymous Function 2");
})();

fctNamedFunction1();
// fctNamedFunction2(); // Cannot call by name
f1();
f2();
```

### Functions and scope

```ts
var function1 = () => { // Example of "fat arrow function"
  let variable1 = 1;
  var function2 = () => {
    let variable2 = 2;
    console.log(variable1 + variable2); // Access variable from function 1
  };
  function2();
};
function1();
```

# 2. Named and Anonymous Functions

### Expressions and declarations

```ts
// Named Function
function functionName1(){}
functionName1(); // Invocation

// Anonymous Function 1
const pointerToFunction1 = function(){}
pointerToFunction1(); // Invocation

// Anonymous Function 2 + Invocation A.K.A. IIFE
(function(){})();
``` 

### Function arguments

```ts
function functionWithParameters(arg1: string, arg2: number){}
```

### Function's retur type

```ts
function functionWithAReturnType(): boolean {
    return true;
}

function functionWithTwoReturnType(): boolean | number {
    return 1;
}
```

### Ingerence of void or never 


```ts
class BaseClass {
    defineMeLater(): never { // Infer void, uncomment never to see the consequence
        throw new Error("Define me in a subclass");
    }
}

class SubClass extends BaseClass {
    defineMeLater() {
        console.log("SubClass code");
    }
}

let c = new SubClass();
c.defineMeLater();
```

### Short version

```ts
const fatarrow = (p: number): number => { return p * 100; } 
```

# 3. Function and Inference Variables

TypeScript can infer the type of a variable, hence, it is possible to avoid using the colon for anonymous functions by simply setting the variable to an unnamed function that has type parameters and a return type. In the example below, all the myAnonymous… functions (lines 5, 8, 11, 12) have no type defined but they are all strongly typed by inference.

```ts
const inc = 1;
function myNamedFunction(p: number): number {
    return p + inc;
}
const myAnonymousFunc = function(p: number): number {
    return p + inc;
};
const myAnonymousFunc2 = (p: number): number => {
    return p + inc;
};
const myAnonymousFunc3 = (p: number): number => p + inc;
const myAnonymousFunc4 = (p: number) => p + inc;
```

```ts
interface MyInterface {
  myFunction: (p1: number) => void;
}

let myInterfaceWithDiffParams: MyInterface = {
  myFunction: (anotherNameForP1: number) => { 
    console.log(`The parameter is ${anotherNameForP1}`);
  }
};

myInterfaceWithDiffParams.myFunction(100);
```

```ts
const infHello: "hello" = "hello"; // Explicit
const infWord = "world"; // Implicit using inference to "world"

let infHello2: "hello" = "hello"; // Explicit
let infWord2 = "world"; // Implicit using inference to string

let worldString: string = "world";

let windeningToString: string = infHello; // Compile
```

# 4. Generic Return Type, Optional Parameter and Default Value

### Function's generic return type

```ts
function arrayMap<T, U>(f: (x: T) => U): (a: T[]) => U[] {     
  return a => a.map(f); 
} 
const lengths: (a: string[]) => number[] = arrayMap(s => s.length); 
```

### Function's optional parameters

```ts
function undefinedOptional1(a: number | undefined, b: number) {}
undefinedOptional1(undefined, 1);
```

### Function with a default value 

```ts
function funcWithDefault(p1: string = "v1", p2?: number, p3 = true) {
    console.log("P1", p1); // v1 since undefined
    console.log("P2", p2); // undefined
    console.log("P3", p3); //boolean by inference
}

funcWithDefault(undefined);
```

# 5. Functions in Classes

### Functions and <code>class</code> in a nutsell

```ts
class MyClass{
    private myFunction1(){}
    public myFunction2(){}
    protected myFunction3(){}
}
```

### Private functions

```ts
class MyPrivateFunctionClass {
  constructor() {
    this.privateFunction();
  }
  private privateFunction(): void {
    console.log("From the private function");
  }
}

const c = new MyPrivateFunctionClass();
// c. // There is nothing to invoke because the function is private 
```

### Protected function

```ts
class ClassA {
  private a1: number = 1;
  protected a2fct(): void {
    console.log(this.a1);
  }
}

class ClassB extends ClassA {
  private b1: number = 2;
  protected b2(): void {
    super.a2fct(); // Call a protected function from a base class
  }
}

const cab = new ClassB();
// cab. // No access to b2 or a2fct
```

### Public funcion

```ts
class ClassA {
  private a1: number = 1;
  protected a2fct(): void {
    console.log(this.a1);
  }
}

class ClassB extends ClassA {
  private b1: number = 2;
  protected b2(): void {
    super.a2fct(); // Call a protected function from a base class
  }
}

const cab = new ClassB();
// cab. // No access to b2 or a2fct
```

# 5. Function Relationshit with "this"

### Function and <code>this</code>

```ts
    interface MyThisInterface {
        m1: string[];
        m2: number[];
        functionA(): () => string;
    }

    let vMyThisInterface: MyThisInterface = {
        m1: ["hearts", "spades", "clubs", "diamonds"],
        m2: [1, 2, 3],
        functionA: function() {
            return function() {
                return this.m1[0]; // This is any
            };
        },
    };

    vMyThisInterface.functionA();
```

### Defining a type to <code>this</code>

```ts
    interface MyThisInterface {
        m1: string[];
        m2: number[];
        functionA(): () => string;
    }

    let vMyThisInterface: MyThisInterface = {
        m1: ["hearts", "spades", "clubs", "diamonds"],
        m2: [1, 2, 3],
        functionA: function() {
            return function(this: MyThisInterface) {
                return this.m1[0]; 
            };
        },
    };

    vMyThisInterface.functionA();
```

### <code>this</code> with callback

```ts
const family = {
    names: ["Patrick", "Alicia", "Melodie"],
    emotion: "love",
    print: function() {
        console.log("print", this); // this = the family object
        return this.names.forEach(function(name: string) {
            console.log("forEach", this); // this = implicit any = won't transpile
        });
    },
};
family.print();
```

### Solving the callback <code>this</code>

```ts
interface Family {
    names: string[];
    emotion: string;
    print: () => void;
}
const family: Family = {
    names: ["Patrick", "Alicia", "Melodie"],
    emotion: "love",
    print: function() {
        console.log("print", this); // this = the family object
        return this.names.forEach(function(this: Family, name: string) {
            console.log("forEach", this);
        }, family);
    },
};
family.print();
```

# 7. Function and Inference Return Types

### Inference with many types

```ts
    function withImplicitReturnType(b: boolean) {
        if (b) {
            return 10;
        }
        return "test";
    }
    console.log(withImplicitReturnType(true));
```

```ts
    function withImplicitReturnType(b: boolean) {
        if (b) {
            return 10;
        } else {
            return true;
        }
        return "test";
    }
    console.log(withImplicitReturnType(true));
```

# 8. String Literal and Overload Function

### A parameter with a string literal

```ts
interface SuperHero {
    attackName: string;
}
interface Batman extends SuperHero {
    jumpLength: number;
}
interface SuperMan extends SuperHero {
    flyingSpeed: number;
}

function createSuperHero(name: "batman"): Batman;
function createSuperHero(name: "superman"): SuperMan;
function createSuperHero(name: string): Batman | SuperMan | SuperHero {
    if (name === "batman") {
        return {
            attackName: "Kick",
            jumpLength: 12,
        };
    } else if (name === "superman") {
        return {
            attackName: "Punch",
            flyingSpeed: 120,
        };
    }
    return {
        attackName: "Run",
    };
}
const hero1 = createSuperHero("batman");
console.log(`Batman can jump ${hero1.jumpLength} feet`);
const hero2 = createSuperHero("superman");
console.log(`Superman can fly ${hero2.flyingSpeed} miles per hour`);
```

# 9. Types of Function Headers

### Function with parameters

```ts
function functParams(p1: string, err: (e: Error) => void): void {}
functParams("test", () => {}); // Parameter e:Error not required
functParams("test", (whatEver: Error) => {}); // Name can be changed
functParams("test", (e: Error) => {});
```

### Function with infinite arguments

```ts
function functRest(p1: string, ...remaining: string[]): void {}
functRest("p1", "p2", "p3");

function functBefore(p1: string, remaining: string[]): void {}
functBefore("p1", ["p2", "p3"]);
``` 

### Function with a callbuack funcion

```ts
function functReturnVoid(f: () => void): void {
    const c: void = f(); // c is "void" but will store a string
    console.log(c); // Print the string from the return of the function in parameter
}
functReturnVoid(() => {
    return "I am a string, not void!"; // Call back return a string but defined to return void in the definition
}); 
```

















































