# 1. Enum With and Without Values

### The role of <code>enum</code>

An enum is a structure that proposes several allowed values for a variable. It is a way to constrain variable values by defining specific possible entries.

### <code>enum</code> with values

```ts
enum MyStringEnum {
    ChoiceA = "A",
    ChoiceB = "B",
}
```

```ts
enum MyStringAndNumberEnum {     
    ChoiceA, // 0     
    ChoiceB = "B",     
    ChoiceC = 100 
}
```

### <code>enum</code> without values

```ts
enum MyEnum {
    ChoiceA,
    ChoiceB,
    ChoiceC,
}
let x: MyEnum = MyEnum.ChoiceA;
console.log(x);
```

```ts
enum MyEnum {
    ChoiceA,
    ChoiceB,
    ChoiceC,
}
enum MyEnum2 {
    ChoiceA, // 0
    ChoiceB = 100, // 100
    ChoiceC, // 101
    ChoiceD = MyEnum.ChoiceC, // 2
}
console.log(MyEnum2.ChoiceA);
console.log(MyEnum2.ChoiceB);
console.log(MyEnum2.ChoiceC);
console.log(MyEnum2.ChoiceD);
```

### <code>enum</code> with  bitwise values

```ts
enum Power {
    None = 0, // Value 0 in decimal (00 in binary)
    Invincibility = 1 << 0, // Value 1 in decimal (01 in binary)
    Telepathy = 1 << 1, // Value 2 in decimal (10 in binary)
    Invisibility = 1 << 2, // Value 3 in decimal (11 in binary)
    Everything = Invincibility | Telepathy | Invisibility,
}
let power: Power = Power.Invincibility | Power.Telepathy;
console.log("Power values:" + power);
if (Power.Telepathy === (power & Power.Telepathy)) {
    console.log("Power of telepathy available");
}
```

# 2. Accessing Enum Values

### TypeScript map objects to allow access

A variable set with an <code>enum</code> that has a <code>number</code> lets you access the enum name from the integer. However, an enum with string values does not have this capability. This means you can use the enum name followed by the name of the constant to get the value. Also, with a number, you can also use the value to return the name.

For example, an enum called Orientation with East, West, North, South could use <code>Orientation.East</code> to get the value zero or use Orientation[0] to get East. This works because TypeScript generates a map object which gives you access using the name of the entry or the value.

```ts
enum Orientation {
    East,
    West,
    North,
    South,
}
let directionInNumber = Orientation.East; // Access with the Enum
let directionInString = Orientation[0];  // Access the Enum string from number
console.log(directionInNumber);
console.log(directionInString);
```

# 3. Merging and Adding Functionality to Enum

### Merging values

Like interfaces, an enum can be defined in more than one place. You can start defining the enum and later define it again. In the end, all values merge into a single enum. There is one constraint with multiple definitions of a single enum: the first value of every enum must have an explicit value. If an explicit value is defined twice, only the last value will be associated with the enum when using the reverse value to find an enum. Listing the same value twice is not a feature of multiple definitions; a single enumeration definition can have several entries with the same values as well.

```ts
enum EnumA {
    ChoiceA,
}
enum EnumA {
    ChoiceB = 1,
}

let variable1: EnumA = EnumA.ChoiceA;
console.log(variable1);
variable1 = EnumA.ChoiceB;
console.log(variable1);
```

### Adding functions

```ts
enum Orientation {
    East,
    West,
    North,
    South,
}
namespace Orientation {
    export function yourFunction() {
        console.log("I am in a Enum");
    }
}
Orientation.yourFunction();
```


