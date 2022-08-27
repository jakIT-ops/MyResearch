# 1. An Introduction to Operators

### Types of Operators

As far as built-in operators go, Scala provides the following five types.

* Arithmetic Operators
* Relational Operators
* Logical Operators
* Bitwise Operators
* Assignment Operators

```scala
val infix = 1+1
val ordinary = 1.+(1)

// Driver Code
print("Using infix notation: ")
println(infix)

print("Using ordinary method call: ")
println(ordinary)
```

# 2. Arithmetic Operators

```scala
val operand1 = 10F
val operand2 = 7F

println(operand1 + operand2)
println(operand1 - operand2)
println(operand1 * operand2)
println(operand1 / operand2)
println(operand1 % operand2)
```

# 3. Relation Operators

```scala
val operand1 = 'a'
val operand2 = 'b'

println(operand1 > operand2)
println(operand1 < operand2)
println(operand1 >= operand2)
println(operand1 <= operand2)
println(operand1 != operand2)
```

# 4. Logical Operators

```scala
val A = true
val B = false
val exp = A && B //false

println(!A)
println(!B)
println(true && exp)
println(false && exp)
println(true || exp)
println(false || exp)
```

# 5. Bitwise Operators

```scala
val A = 12
val B = 5

println(~A)
println(~B)
println(A & B)
println(A | B)
println(A ^ B)
```

# 6. Assignment Operators

```scala
var A = 10
var B = 7

print("Before using an assignment operator: ")
println(A)

A += B

print("After using an assignment operator: ")
println(A)
```
















