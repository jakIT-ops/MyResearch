/// 1
for (var i = 0; i < 10; i++) {
  var leak = "I am available outside of the loop";
}

console.log(leak);
// I am available outside of the loop

// 2 
function myFunc(){
  var functionScoped = "I am available inside this function";
  console.log(functionScoped);
}
myFunc();
// I am available inside this function
console.log(functionScoped);
// ReferenceError: functionScoped is not defined
