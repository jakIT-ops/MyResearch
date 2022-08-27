# 1. Iterating an Object's Keys with For-in 

### Iterating an objec's keys with for-in

```ts
let list1: (number | string)[] = [1, 2, 3, "a", "b", "c"];
for (let i in list1) { // Loop all indexes, not values
    console.log(i); // Print: 0, 1, 2, 3, 4, 5
}
```

### Iterating an objects keys with for-of

```ts
let list2: (number | string)[] = [1, 2, 3, "a", "b", "c"];
for (let i of list2) { // Loop all values
    console.log(i); // 1, 2, 3, "a", "b", "c"
}
```

### Iterating with <code>forEach</code>

```ts
let list3: (number | string)[] = [1, 2, 3, "a", "b", "c"];
list3.forEach((v: string | number, index: number, array: (string | number)[]) => {
    console.log("Value " + v + " at position " + index);
}); 
```

# 2. Iterating an Object with Standard For/While

### For loop

```ts
let listArrayPrimitive = { m1: "valuem1", m2: 2 };
const keys = Object.keys(listArrayPrimitive);
const entries = Object.entries(listArrayPrimitive); // require to have "lib": [ "es2017.object" ]
console.log("keys", keys);
console.log("entries", entries);
```

### While loop

```ts
let listArrayPrimitive = { m1: "valuem1", m2: 2 };
const entries: any[] = Object.entries(listArrayPrimitive); // require to have "lib": [ "es2017.object" ]
while (entries.length > 0) {
    const val = entries.shift();
    console.log(`The property name ${val[0]} has the value ${val[1]}`);
}
```

# 3. Iterating and the Asynchronous Loop

### Iteration and the TypeScript generator

TypeScript generators are an advanced and very modern concept. They use the function* syntax which is the standard function keyword followed by an asterisk. The star syntax indicates that a function returns a generator object. A function that returns a generator object can return multiple times. This function allows the use of the yield keyword, which returns a value without returning the function. It allows for potential infinite iteration, while still being able to consume the value outside the function. The function returns a generator object which has a .next() function. The next function returns a value of type IteratorResult. The function returns when the iteration is over with a done property from IteratorResult. The done property is of type Boolean and is used to tell a while or for loop to stop.

### Before TypeScript 3.2: Working with the <code>asynciterator</code>

```ts
// Step 1 (Older version of TypeScript only)
// (<any>Symbol).asyncIterator = Symbol.asyncIterator || Symbol.for("Symbol.asyncIterator");
// Step 2
function delay(ms: number): Promise<void> {
    return new Promise<void>(resolve => {
        setTimeout(resolve, ms);
    });
}
function getRandomSetChars(): string {
    const random = 1 + Math.floor(Math.random() * 5);
    let wordString = "";
    for (let i = 0; i < random; i++) {
        const letter = 97 + Math.floor(Math.random() * 26);
        wordString += String.fromCharCode(letter);
    }
    return wordString;
} 
// Step 3
async function* getRandomSetsChars(): AsyncIterableIterator<string> {
    for (let i = 0; i < 10; i++) {
        yield getRandomSetChars(); // return a random set of char
        await delay(200); // wait
        yield* [getRandomSetChars(), getRandomSetChars()]; // return two random sets of char
    }
}
// Step 4
async function addWordsAsynchronously() {
    for await (const x of getRandomSetsChars()) {
        console.log("Iterator loop:" + x);
    }
}
addWordsAsynchronously();
```




