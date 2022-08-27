interface IN_A {
    m1: number;
    m2: boolean;
}
interface IN_B {
    m3: string;
}

function foo(x: IN_A | IN_B) {
    if ("m1" in x) { // m1 is only in IN_A
        console.log("Type narrowed to IN_A", x.m1, x.m2);
    } else { // IN_B
        console.log("Type narrowed to IN_B", x.m3);
    }
    console.log("A is still IN_A or IN_B");
}

foo({ m1: 1, m2: true }); // Implicit IN_A
foo({ m3: "" }); // Implicit IN_B
