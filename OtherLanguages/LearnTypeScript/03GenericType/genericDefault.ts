/*
TypeScript allows us to define a default type for generic, also known as “generic parameter defaults”. The syntax is intuitive which is the equal sign of the generic type. The generic type parameter doesn’t need to be explicit when an optional value is provided. TypeScript can infer its type. 
*/

interface InterfaceGenericDefinedTwoPlace<T = string> {
    myProp: T;
}
interface InterfaceGenericDefinedTwoPlace<T> {}
interface InterfaceGenericDefinedTwoPlace {}

let x: InterfaceGenericDefinedTwoPlace = { myProp: "stringHere" };
