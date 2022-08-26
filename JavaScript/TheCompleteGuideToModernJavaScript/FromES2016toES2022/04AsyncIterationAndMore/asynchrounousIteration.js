const iterables = [1,2,3];

async function test() {
    for await (const value of iterables) {
        console.log(value);
    }
}
test();
// 1
// 2
// 3
