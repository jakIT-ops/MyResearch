# 1, String Interpolation with 's'

### The `s` string Interpolator

```scala
val country = "Japan"

println(s"I want to visit $country!")
```

`s"Optional String $VariableIdentifier Optional String"`

### Syntax for Expressions with Non-Identifier Characters#

```scala
println(s"3 + 4 = ${3 + 4}")
```

# 2. String Interpolation with 'f'

### The `f` String Interpolator# 

```scala
val pi = 3.14159F

println(f"the value of pi is $pi%.2f")
```

### Conversion-Characters


| Character	| Use |
| :------------ | --------: |
| s	|formats strings |
|d	|formats decimal integers |
|f	|formats floating-point numbers |
|t	|formats date/time values |


# 3. String Interpolation with 'raw'

### The `raw` String Interpolator


```scala
println("Without Raw:\nFirst\nSecond")
println(raw"With Raw:\nFirst\nSecond")
```


# 4. Testing String Equality

```scala
val string1 = "Educative"
val string2 = "educative"

val areTheyEqual = string1==string2

// Driver Code
println(areTheyEqual)
```

# 5. Creatubg Multiline Strings

```scala
val multilineString = """This is a 
multiline string
consisting of 
multiple lines"""

// Driver Code
print(multilineString)
```

# 6. Splitting Strings

```scala
val splitPizza = "Pizza Dough,Tomato Sauce,Cheese,Toppings of Choice".split(",")

// Driver Code
splitPizza.foreach(println)
```

# 7. Finding Patterns in Strings

```scala
val expressionToFind = "[1-5]{2}+".r

val stringToFindExpression = "12 67 93 48 51"

val match1 = expressionToFind.findAllIn(stringToFindExpression)

// Driver Code
match1.foreach(println)
```

# 8. Replacing Patterns in Strings


```scala
val replaceIn = "8201530"
val replaced = replaceIn.replaceAll("[01]", "X")

// Driver Code
println(replaced)
```

# 9. Methods for Comparing Strings

```scala
val string1 = "This is Educative"
val string2 = "Hello Scala"  
val string3 = "Hello Scala" 

val lexiCompare1 = string1.compareTo(string2) //string2-string1
val lexiCompare2 = string2.compareTo(string3) //string3-string2

// Driver Code
println(s"Comparing string1 and string2: $lexiCompare1")  
println(s"Comparing string2 and string3: $lexiCompare2") 
```





