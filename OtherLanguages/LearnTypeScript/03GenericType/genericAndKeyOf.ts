interface TypeA {
  prop1: string;
  prop2: number;
}

function printProps<T, K extends keyof T>(p1: T, p2: K[]): void { // Extends all properties' name of T
  console.log("Printing:");
  p2.forEach(propName => {
    console.log(`Name: ${propName} and value: ${p1[propName]}`);
  });
}

let a: TypeA = { prop1: "p1", prop2: 2 };

printProps(a, ["prop1"]);
printProps(a, ["prop1", "prop2"]);
// printProps(a, ["not", "working"]);

/*
 Printing:
Name: prop1 and value: p1
Printing:
Name: prop1 and value: p1
Name: prop2 and value: 2
 */
