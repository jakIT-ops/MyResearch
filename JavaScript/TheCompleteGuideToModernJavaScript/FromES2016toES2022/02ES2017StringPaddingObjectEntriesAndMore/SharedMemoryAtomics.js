// create a `SharedArrayBuffer`
const buffer = new SharedArrayBuffer(16);
const uint8 = new Uint8Array(buffer);

// add a value at the first position
uint8[0] = 10;

console.log(Atomics.add(uint8, 0, 5));
// 10

// 10 + 5 = 15
console.log(uint8[0])
// 15
console.log(Atomics.load(uint8,0));
// 15


// create a `SharedArrayBuffer`
const buffer = new SharedArrayBuffer(16);
const uint8 = new Uint8Array(buffer);

// add a value at the first position
uint8[0] = 10;

console.log(Atomics.sub(uint8, 0, 5));
// 10

// 10 - 5 = 5
console.log(uint8[0])
// 5
console.log(Atomics.store(uint8,0,3));
// 3
console.log(Atomics.load(uint8,0));
// 3
//



