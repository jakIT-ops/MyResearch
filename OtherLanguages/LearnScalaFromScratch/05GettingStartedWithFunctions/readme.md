# 1. Defining a Function

### Syntax

`def functionName(parameters): returnType ={function body}`

```scala
def sum(x: Int, y: Int): Int ={
  x+y
}

val total = sum(2,3)

// Driver Code
println(total)
```

# 2. Evaluation Strategies

### The Substituation Model

```scala
def square(x: Double) ={
  x * x
}

def squareSum(x: Double, y: Double) ={
  square(x) + square(y)
}

val total = squareSum(2,4+1) // 4+1 reduces to 5 so this is a valid parameter

// Driver Code
println(total)
```

# 3. Code Termination

```scala
def loop :Int = loop

def accessFirst(x: Int, y: => Int) = x

val result = accessFirst(1,loop)
println(result)
```

# 4. Recursive Functions


```scala
def factorial(x: Int) : Int = {
  if(x == 1)
    1
  else
    x * factorial(x-1)
}

// Driver Code
print(factorial(4))
```

# 5. Blocks

```scala
def abs(x: Double) =
  if (x < 0) -x else x

def isGoodEnough(guess: Double, x: Double) =
  abs(guess * guess - x) / x < 0.0001

def improve(guess: Double, x: Double) =
  (guess + x / guess) / 2

def sqrtIter(guess: Double, x: Double): Double =
  if (isGoodEnough(guess, x)) guess
  else sqrtIter(improve(guess, x), x)

def sqrt(x: Double) = sqrtIter(1.0, x)
```

### Nested functions

```scala
def abs(x: Double) =
  if (x < 0) -x else x

def sqrt(x: Double) ={ 
  def sqrtIter(guess: Double, x: Double): Double =
    if (isGoodEnough(guess, x)) guess
    else sqrtIter(improve(guess, x), x)  

  def isGoodEnough(guess: Double, x: Double) =
    abs(guess * guess - x) / x < 0.0001

  def improve(guess: Double, x: Double) =
    (guess + x / guess) / 2

  sqrtIter(1.0, x)
}

println(sqrt(4))
```

### Visiblilty

```scala
val amIVisible = 0
def square(x: Int) =
  x * x

val result = {
  val amIVisible = square(3)
  println(s"Variable Inside Block: $amIVisible")
} 

println(s"Variable Outside Block: $amIVisible")
```

# 6. Lexical Scope

```scala
def abs(x: Double) =
  if (x < 0) -x else x

def sqrt(x: Double) ={ 
  def sqrtIter(guess: Double, x: Double): Double =
    if (isGoodEnough(guess, x)) guess
    else sqrtIter(improve(guess, x), x)  

  def isGoodEnough(guess: Double, x: Double) =
    abs(guess * guess - x) / x < 0.0001

  def improve(guess: Double, x: Double) =
    (guess + x / guess) / 2

  sqrtIter(1.0, x)
}

//Driver Code
println(sqrt(4))
```

# 7. Tail Recursion

```scala
def factorial(x: Int): Int = {
  if(x==0) 1
  else x * factorial(x-1)
}

println(factorial(4))
```







