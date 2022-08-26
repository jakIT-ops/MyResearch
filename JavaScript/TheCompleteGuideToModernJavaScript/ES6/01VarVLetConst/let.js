// 1.
// using `let`
let x = "global";

if (x === "global") {
  let x = "block-scoped";

  console.log(x);
  // expected output: block-scoped
}

console.log(x);
// expected output: global

// 2.
// using `var`
var y = "global";

if (y === "global") {
  var  y= "block-scoped";

  console.log(y);
  // expected output: block-scoped
}

console.log(y);
// expected output: block-scoped
