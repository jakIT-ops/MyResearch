# 1. Declaring a Variable

### Declaring with <code>var</code>

```ts
function varFunction(){     
    var x = "111";    
    if(true){             
        var x = "999"; // Variable x redefined   
    }     
    console.log(x); 
}
varFunction()
```

```ts
var x;
function varFunction(){     
    var x = "111";    
    if(true){             
        var x = "999";    
    }     
    console.log(x); 
}
varFunction()
console.log(x)
```

### Declaring with <code>let</code>

```ts
function letFunction() {
    let x = "111";
    if (true) {
        let x = 999;
    }
    console.log(x); 
}
letFunction();
```
```ts
var myVarVariableOutSide = "I am outside";
let myLetVariableOutSide = "I am outside too";
function letOutsideFunction() {
    console.log(myVarVariableOutSide);
    console.log(myLetVariableOutSide);
}
letOutsideFunction();
```

### Declaring with <code>const</code>

```ts
const x = "111";
x = "this won't compile"; 
```

```ts
function constChangeObject() {
    let obj1 = { p1: "p1value" };
    obj1 = { p1: "p1value changed" };

    const obj2 = { p2: "p2value" };
    obj2 = { p2: "Does not compile" };
    obj2.p2 = "Work!";
}
```

# 2. Declaring Types in Untyped Code

The keyword declare can be used before one of the previous three declaration types (var, let, const). As the name suggests, it declares to TypeScript that the variable is somewhere but not saying where. This is not used frequently but can be useful if you need to tell the transpiler that the variable is present, just not in the current project (or loaded module), and may not be visible.

```ts
declare let variableDefinedSomewhereElse: number; 
let newVariable = variableDefinedSomewhereElse + 1; 
```

```ts
declare function ambientFunction(i: number):void;

function myFunction(i: number){
    ambientFunction(1);
}
```

# Hoisting Variables 

Before moving on, let’s talk about the concept of hoisting. It is a quirk of JavaScript that brings all declarations made with <code>var</code> to the top of the function (or into the global scope if declared outside a function).

```ts
var x: string | undefined = undefined;
x = "not declared before assignment"; 
x = "declared after assignment and all fine"; 
console.log(x);
```

# 3. Switch Scope

```ts
function switchFunction(a: number): void {
    switch (a) {
        case 1:
            let variableInCase1 = "test";
            console.log(variableInCase1);
            break;
        case 2:
            let variableInCase2 = "test2";
            console.log(variableInCase2);
            break;
        default:
          console.log("Default");    
    }
}
switchFunction(1);
switchFunction(2);
switchFunction(3);
```

# 4. The Multiple Methods of Declaring a String

### Strings on a single line

```ts
let w = "Value1";
let x = "this is a string with the value " + w;
let y = 'this is a string with the value ' + w;
let z = `this is a string ${w}`;
console.log(w,x,y,z)
```

### Strings on multiple lines

```ts
let multiline1 = "Line1\n" + "Line2\n" + "Line3\n";

let multiline2 = `Line1 
Line2 
Line3`;

console.log(multiline1);
console.log(multiline2);
```

### Strings interpolation for formatting

```ts
let numberBook = 10;
let storeName = "Amazon";
let title = `My favorite ${numberBook} books on ${storeName}`
console.log(title);
```

# 5. String-Tagged Templates

```ts
const number = 84;
const number2 = 100;
const endResult = analyzeString`The number is ${number} which is not like the second number ${number2}`;
```

#6.  What is a Number in TypeScript?

### number base

```ts
let dec: number = 10;
let hex: number = 0x10;
let octo: number = 0o10;
let bin: number = 0b10;
console.log("Here are 4 numbers", dec, hex, octo, bin);
```

```ts
let dec2 = 10; 
let hex2 = 0x10; 
let octo2 = 0o10; 
let bin2 = 0b10; 
console.log("Here is 4 numbers", dec2,hex2,octo2,bin2);
```

### The <code>number</code>: integer, decimal, and signed

```ts
let int: number = 1;
let float: number = 1.1;
let negative: number = -100;
console.log(typeof(int));
console.log(typeof(float));
console.log(typeof(negative));
```

### Not a Number (NaN)

```ts
let myNumberIsNotANumber: number = NaN;
console.log(myNumberIsNotANumber);
console.log(typeof(myNumberIsNotANumber));
```

### Separator

```ts
const numericSeparator1 = 560000067;
const numericSeparator2 = 560_000_067;
const numericSeparator3 = 5_6_0_000_0_6_7;
const numericSeparator4 = Number(5_000);
const numericSeparator5 = Number("5_000"); // Nan 
const numericSeparator6 = parseInt("5_000");  
const numericSeparator7 =  0xFAB_F00D; 
const numericSeparator8 =  0b1111_11111000_11110000_00001100;
console.log(numericSeparator1)
console.log(numericSeparator2)
console.log(numericSeparator3)
console.log(numericSeparator4)
console.log(numericSeparator5)
console.log(numericSeparator6)
console.log(numericSeparator7)
console.log(numericSeparator8)
```

# 7. Avoiding `any` at Any Time Possible

```ts
let x: any = "string";
x = true;
x = { title: "Object with a string member" };
x = [1, 2, 3];
x = 1;
```

> Move your cursor above <code>req.response</code> in the following code (line 8) to see the type of <code>any</code>

```ts
function get(url: string) {
    return new Promise(function(resolve, reject) {
        var req = new XMLHttpRequest();
        req.open("GET", url);

        req.onload = function() {
            if (req.status == 200) {
                resolve(req.response);
            } else {
                reject(Error(req.statusText));
            }
        };
    });
}
```

# 8. Mutable and Immutable Arrays

### Mutable arrays

Arrays in TypeScript are exactly like the ones in JavaScript in terms of features. The difference is that TypeScript assigns a type to the list.

```ts
let a: number[];
```

```ts
let arrayOfNumber = [1, 2, 3]; 

let arrayOfString = ["string", "array", "only"];
```

```ts
let usingArraySyntax: Array<number> = [1, 2, 3]; 
```

### Immutable arrays

While the two syntaxes presented above refer to mutable collections, there is also the possibility of creating a list that is immutable. The <code>ReadonlyArray</code> is a generic array that only allows you to read from the array once it’s constructed. As with the mutable array, there are two ways to write a read-only collection.

```ts
let list: ReadonlyArray<number> = [1, 2];
list.push(3);
console.log(list);
```

# 9. Returning nothing with Void

Void means nothing. However, undefined can be assigned to void. The operation of setting undefined to void is not useful per se. However, a function that returns nothing should be marked with the reserved void keyword.

```ts
function executeFunctionWithoutReturnType(): void {
    return undefined;
}
let returnType = executeFunctionWithoutReturnType(); // Hover the variable to see "void"
console.log(returnType);
```

```ts
function leaveEarly(leaveFast: boolean): void {
  console.log("Hello");
  if(leaveFast){
    console.log("Quick bye!")
    return;
  }
  console.log("Later good bye");
}

console.log("-- With true --");
let voidVar1: void = leaveEarly(true);
console.log("-- With false --");
let voidVar2: void = leaveEarly(false);
```

# 10. The Primitive Type never

```ts
enum EnumWithChoices {
    ChoiceA,
    ChoiceB,
    ChoiceC,
}

function functionReturnStringFromEnum(c: EnumWithChoices): string {
    switch (c) {
        case EnumWithChoices.ChoiceA:
            return "A";
        case EnumWithChoices.ChoiceB:
            return "B";
        default:
            return unhandledChoiceFromEnum(c);
    }
}

function unhandledChoiceFromEnum(x: never): never {
    throw new Error("Choice not defined");
}
```

# 11. Literal Type to Narrow Primitive Type

### Literal type

A literal type means that the value is an exact one. For example, a string literal of “test” would mean that the value of the variable can only be “test”.

A literal type can be made up of multiple types or values from primitive JavaScript types.

### String literals

```ts
let direction: string = "no-where" // We desired to be "north", "south", "east", "west".
```

```ts
type Direction = "north" | "south" | "east" | "west";
let myDirection:Direction = "north";
// let yourDirection:Direction = "no-where"; // Does not compile
```

### Number literals

```ts
type Column = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12;
let menuSize: Column = 4;
let mainContent: Column = 100; // Does not compile because only accept 1 to 12
```

### Literal mixed type

```ts
type OptionOpen = true | false | "true" | "false"; // Actuall : boolean | "true" | "false"

function openWindow(option: OptionOpen): void {
   if(option === "true" || option === true){

   } else if (option === "false" /* || option === false*/){

   } else{
     const c: never = option;
   }
}
```

# 12. Casting to Change Type

### Casting constraints

```ts
const str: string = "123";
const bool: boolean = true;
const castFromString:number = str as number;
const castFromBoolean:number = bool as number;
console.log(castFromString)
console.log(castFromBoolean)
```

### Type assertion

```ts
interface YourType {
  m1: string;
}

let v1 = {m1: "ValueOfM1"} as YourType;
console.log(v1);
```

```ts
interface IMyType {
  m1: string;
  m2: number;
}

let myVariable = {} as IMyType; // 
```















































