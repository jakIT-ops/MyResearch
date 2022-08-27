function genericInferred<T extends string>(param: T) {
    return param.length;
}
console.log(genericInferred("Four")); // 4
// genericInferred(123); // Does not transpile
type UUID = string;
let id: UUID = "123-456";
console.log(genericInferred(id)); // 7
