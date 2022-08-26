let str = "    this string has a lot of whitespace   ";

str.length;
// 42

str = str.trimStart();
console.log(str);
// "this string has a lot of whitespace   "
console.log(str.length);
// 38

str = str.trimEnd();
console.log(str);
// "this string has a lot of whitespace"
console.log(str.length);
// 3
