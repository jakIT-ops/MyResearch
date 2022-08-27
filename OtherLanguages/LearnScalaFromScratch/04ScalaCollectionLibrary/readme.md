# 1. An Introduction to the Collection Library

### Mutable Collections

Mutable collections are collections which can be updated. Elements can be added to the collection and can be removed or manipulated. In this case, the collection itself will be getting modified.

### Immutable Collections

Immutable collections cannot be updated. When you add, remove, or manipulate an element in an immutable collection, you are creating a new collection and leaving the old one unchanged.

### Sequences, Sets, and Maps

The collection library takes on a hierarchical structure. At the top of the library, there are three main categories of collection classes under which different collections lie:

* Sequences - Seq

* Sets - Set

* Maps - Map

```scala
val mapCollection = Map(("a",25),("b",50),("c",75))

val result = mapCollection.apply("c")

// Driver Code
print(result)


val setCollection = Set("apple", "orange", "banana", "grape")

val result = setCollection.apply("orange")

// Driver Code
print(result)


val seqCollection = Seq(2,4,6,8)

val result = seqCollection.apply(1)

// Driver Code
print(result)
```

# 2.  foreact: A Collection Method

```scala
val collection = Seq(2,4,6,8,10)

collection.foreach(println)
```

# 3. The Array Collection

```scala
val intArray = Array(1,2,3,4,5,6,7,8,9,10) 
val evenArray = intArray.filter(_ % 2 == 0)
val doubleArray = evenArray.map(_ * 2)
val finalArray = doubleArray.reverse

// Driver Code
finalArray.foreach(println)
```

```scala
val intArray = Array(17, 34, 23, 6, 50)
val len = intArray.length

println(len)
```

# 4. ArrayBuffers


### Creating an ArrayBuffer

```scala
import scala.collection.mutable.ArrayBuffer

val myFirstArrayBuffer = ArrayBuffer(1,2,3,4,5)

// Driver Code
myFirstArrayBuffer.foreach(println)
```

### Adding Elements


```scala
import scala.collection.mutable.ArrayBuffer
val newArrayBuff = new ArrayBuffer[Int]()

newArrayBuff += 6
newArrayBuff += 15
newArrayBuff += 78
newArrayBuff += 4
newArrayBuff += 32
newArrayBuff += 11

// Driver Code
newArrayBuff.foreach(println)
```

### Delete Elements

```scala
import scala.collection.mutable.ArrayBuffer
val newArrayBuff = new ArrayBuffer[Int]()

newArrayBuff += 6
newArrayBuff += 15
newArrayBuff += 78
newArrayBuff += 4
newArrayBuff += 32
newArrayBuff += 11

newArrayBuff -= 78 //Remove the element with the value 78

// Driver Code
newArrayBuff.foreach(println)
```

### `remove` method


```scala
import scala.collection.mutable.ArrayBuffer
val newArrayBuff = new ArrayBuffer[Int]()

newArrayBuff += 6
newArrayBuff += 15
newArrayBuff += 78
newArrayBuff += 4
newArrayBuff += 32
newArrayBuff += 11

newArrayBuff -= 78

newArrayBuff.remove(4) //Remove the element at the 4th index

// Driver Code
newArrayBuff.foreach(println)
````

### `clear` method

```
import scala.collection.mutable.ArrayBuffer
val newArrayBuff = new ArrayBuffer[Int]()

newArrayBuff += 6
newArrayBuff += 15
newArrayBuff += 78
newArrayBuff += 4
newArrayBuff += 32
newArrayBuff += 11

newArrayBuff -= 78

newArrayBuff.remove(4)

newArrayBuff.clear() //Remove all the elements from newArrayBuff

// Driver Code
newArrayBuff.foreach(println)
```

# 5. Working With Lists


### Creating a List

```scala
val fruitList = List("orange", "banana", "apple", "grape")

// Driver Code
fruitList.foreach(println)


val intList = List.range(1, 10)

// Driver Code
intList.foreach(println)



val educativeList = List.fill(3)("educative")

// Driver Code
educativeList.foreach(println)
```   


### Constructuring Lists Using `::` and `nil`

```scala
val fruitList = "orange"::"banana"::"apple"::"grape"::Nil

// Driver Code
fruitList.foreach(println)
```

### Appending elements

```scala
val fruitList = "orange"::"banana"::"apple"::"grape"::Nil
val fruitList2 = fruitList :+ "peach"

// Driver Code
fruitList2.foreach(println)
```

### Prepending Elements

```scala
val fruitList = "orange"::"banana"::"apple"::"grape"::Nil
val fruitList2 = fruitList :+ "peach"
val fruitList3 = "watermelon"::fruitList2

// Driver Code
fruitList3.foreach(println)
```

### Lsit Concatenation

```scala
val fruitList = "orange"::"banana"::"apple"::"grape"::Nil
val fruitList2 = fruitList :+ "peach"
val fruitList3 = "watermelon"::fruitList2
val fruitList4 = "mango" +: fruitList3
val twoFruits = "pear"::"apricot"::Nil
val fruitList5 = twoFruits ::: fruitList4

// Driver Code
fruitList5.foreach(println)
```

### Head and tail

```scala
val fruitList = "orange"::"banana"::"apple"::"grape"::Nil
val fruitList2 = fruitList :+ "peach"
val fruitList3 = "watermelon"::fruitList2
val fruitList4 = "mango" +: fruitList3
val twoFruits = "pear"::"apricot"::Nil
val fruitList5 = twoFruits ::: fruitList4

val getHead = fruitList5.head
val getTail = fruitList5.tail

// Driver Code
println(getHead)
println(getTail)
```

# 6. Getting Started with Vectors


### Creating a Vector

```scala
val numVector = Vector(1,2,3,4,5)

numVector.foreach(println)
```
```scala
val emptyVector = Vector.empty
```

### Accessing an Element

```scala
val patternVector = Vector("a~a", "b~b", "c~c")
val pattern = patternVector(1)

println(pattern)
```

### Appending an Element

```scala
val patternVector = Vector("a~a", "b~b", "c~c")
val patternVector2 = patternVector :+ "d~d"

// Driver Code
patternVector2.foreach(println)
```

### Vector Concatenation

```scala
val patternVector = Vector("a~a", "b~b", "c~c")
val patternVector2 = patternVector :+ "d~d"
val patternVector3 = "1~1" +: patternVector2
val tempVector = Vector("e~e","f~f")
val patternVector4 = patternVector3 ++ tempVector

// Driver Code
patternVector4.foreach(println)
```

# 7. LazyList: A Lazy Version of List

### Creating LazyList

`head #:: tail #:: lazylist.empty`

```scala
val myFirstLazyList = 1.5 #:: 2.5 #:: 3.5 #:: LazyList.empty

myFirstLazyList.foreach(println)
```























































