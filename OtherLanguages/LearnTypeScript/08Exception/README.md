# 1. Creating an Exception

### Throwing exceptions

```ts
function throw1() {
    throw "error in string";
}

function throw2() {
    throw Error("Message Here");
}

function throw3() {
    const err: Error = new Error("Message Here");
    throw err;
}

// throw1();
// throw2();
// throw3();
```

### Custom typed error

```ts
class MySpecificError extends Error {
    public data: string;
    constructor(data: string, message: string) {
        super(message);
        Object.setPrototypeOf(this, MySpecificError.prototype); // Restore prototype chain
        // OR: 
        // Object.setPrototypeOf(this, new.target.prototype); // Restore prototype chain
        this.data = data;
    }
}

throw new MySpecificError("dataHere", "My Message");
```

# 2. Catching Synchronous Exceptions

### Synchronous code: an exception

Synchronous code is a traditional piece of code that is executed in the order that the lines are written. Asynchronous is when a piece of code is executed while the main thread (where the synchronous code is executed) occurs. In this lesson, we will focus on the exception that occurs in the main thread: synchronous exception

```ts
function throw1() {
  throw "error in string";
}

function throw2() {
  throw Error("Message Here");
}

function throw3() {
  const err: Error = { name: "Error", message: "Message" };
  throw err;
}

try {
  throw1();
} catch (e) {
  console.log("Exception 1", e); // String
}
try {
  throw2();
} catch (e) {
  console.log("Exception 2", e); // Full stack
}
try {
  throw3();
} catch (e) {
  console.log("Exception 2", e); // Object
}
```

### Narrowing exceptions with <code>instanceof</code>

```ts
class ArgumentNullException extends Error {
    constructor(public name: string) {
        super("Argument was undefined");
        Object.setPrototypeOf(this, ArgumentNullException.prototype);
    }
}
class ReferenceException extends Error {
    constructor(public x: number, public y: number) {
        super("Reference was undefined");
        Object.setPrototypeOf(this, ReferenceException.prototype);
    }
}
function throwTwoExceptions(switcher: boolean) {
    if (switcher) {
        throw new ArgumentNullException("Switcher");
    }
    throw new ReferenceException(1, 2);
}
try {
    throw new ArgumentNullException("Switcher");
} catch (ex) {
    if (ex instanceof ArgumentNullException) {
        console.log("I can access name:" + ex.name);
    } else if (ex instanceof ReferenceException) {
        console.log("I can access x and y:" + ex.x + " and " + ex.y);
    }
}
```

### Bubble up

```ts
function method1() { // Calls method2 which call method3 which throw an error
  method2();
}

function method2() { // Calls method3 which throw an error
  method3();
}

function method3() { // Calling this method will throw an error
  throw Error("Msg from method 3");
}
try {
  method1(); // Call method 1 that call method 2 that call method 3 that throw an error
} catch (e) {
  console.log(e.message);
}
```

# 3. Catching Asynchronous Exceptions

# Asynchronous code

An asynchronous exception occurs when an asynchronous code throws an exception. Asynchronous code is often associated with the concept of Promise that is defined in the next section. In TypeScript (as well as JavaScript), asynchronous code is a piece of code that executes aside from the main thread of execution. The goal is to have a task running while another task is executed. For example, you can click buttons and write inside inputs while a response to a server is fetching information.

# Promises

A Promise is the creation of asynchronous code. The mechanism allows calling the following function when a problem occurs or when there is a successful promise completed. In the following code, line 3 throws an error. The problem is that no code handles the error, hence it will get an unhandled exception.

```ts
Promise.resolve("value to be in the argument of then")
    .then((response: string) => {
        throw new Error("Error message");
        return "Test";
    })
    .then((response: string) => {
        console.log("Second then", response);
        return Promise.resolve(response);
    })
    .catch((err: Error) => {
        console.log("Error Message#2", err.message);
    })
    .then((response: string | void) => {
        console.log("Always called", response);
    });
```

### The await/async alternative

```ts
function returnPromise(): Promise<string> {
  const p = Promise.resolve("value to be in the argument of then");
  throw new Error("Error Message");
  return p;
}

async function functionHandlePromise() {
  try {
    await returnPromise();
  }
  catch (err) {
    console.log("Error Message #2", err.message);
  }
  finally {
    console.log("Always called");
  }
}
functionHandlePromise();
```

# 4. Assertion Functions

### Asserting untyped code

```ts
function showLandArea(address, x, y) { // No typê
    assert(typeof address === "string");
    assert(typeof x === "number");
    assert(typeof y === "number");

    console.log(`The house ${address.substr(10)} as an area of ${x * y} meters`)
}
showLandArea("1234 Street ABCDE", 10, 5);
// showLandArea("1234 Street ABCDE", "10", "5"); // Assertion will catch the 10 and 5 as string
```

### Custom assertions

```ts
function assertAddress(address: any): asserts address is string {
    if (typeof address !== "string") {
        throw new Error("Not a string!");
    }
    if(address.length < 3){
      throw new Error("Address must be above 3 characters");
    }
}

function createAddress(newAddress: any): void{
   assertAddress(newAddress);
   // newAddress is a string from that point if a string with 4+ characters
}
```
