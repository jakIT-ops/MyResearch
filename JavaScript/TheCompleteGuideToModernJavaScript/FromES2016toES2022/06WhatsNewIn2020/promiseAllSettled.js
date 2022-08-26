
// IF YOU ARE GETTING ERRORS, RUN THIS CODE IN THE CONSOLE OF YOUR BROWSER

const arrayOfPromises = [
    new Promise((res, rej) => setTimeout(res, 1000)),
    new Promise((res, rej) => setTimeout(rej, 1000)),
    new Promise((res, rej) => setTimeout(res, 1000)),
]

Promise.allSettled(arrayOfPromises).then(data => console.log(data));

// [
//   Object { status: "fulfilled", value: undefined},
//   Object { status: "rejected", reason: undefined},
//   Object { status: "fulfilled", value: undefined},
// ]
