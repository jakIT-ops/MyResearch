# 1. Creating a Class in Scala

### Defining class

`class classIdentifier`

### Definging the Methods of o Class

```scala
class Person{
  var name: String = "temp"
  var gender: String = "temp"
  var age: Int = 0

  def walking = println(s"$name is walking")

  def talking = println(s"$name is talking")

}
```

# 2. Object of a Class


```scala
class Person{
  var name: String = "temp"
  var gender: String = "temp"
  var age: Int = 0

  def walking = println(s"$name is walking")

  def talking = println(s"$name is talking")

}
// Creating an object of the Person class
val firstPerson = new Person 

firstPerson.name = "Sarah"
firstPerson.gender = "female"
firstPerson.age = 25

firstPerson.walking
firstPerson.talking
```

### Multiple Objects of the Same Class#

```scala
class Person{
  var name: String = "temp"
  var gender: String = "temp"
  var age: Int = 0

  def walking = println(s"$name is walking")

  def talking = println(s"$name is talking")

}
// Creating an object of the Person class
val firstPerson = new Person 

firstPerson.name = "Sarah"
firstPerson.gender = "female"
firstPerson.age = 25

// Creating an object of the Person class
val secondPerson = new Person
secondPerson.name = "Ben"

// Creating an object of the Person class
val thirdPerson = new Person 
thirdPerson.name = "Martin"

// Creating an object of the Person class
val fourthPerson = new Person 
fourthPerson.name = "Hannah"

// Driver Code
println(firstPerson.name)
println(secondPerson.name)
println(thirdPerson.name)
println(fourthPerson.name)
```

### Private and Public Fields

```scala
class Person{
  private var name: String = "temp"
  private var gender: String = "temp"
  private var age: Int = 0

  def walking = println(s"$name is walking")

  def talking = println(s"$name is talking")
}
```


# 3. Creating an Object Using-Constructor Parameters

```scala
class Person(var name: String, var gender: String, var age: Int) {

  private var years = 15
    
  def walking = println(s"$name is walking")
  def talking = println(s"$name is talking")
  def yearsFromNow = {
    var newAge = years + age
    println(s"In $years years from $name will be $newAge")
  }
}
```

```scala
class Person(var name: String, var gender: String, var age: Int) {

  private var years = 15
    
  def walking = println(s"$name is walking")
  def talking = println(s"$name is talking")
  def yearsFromNow = {
    var newAge = years + age
    println(s"In $years years from $name will be $newAge")
  }
}

// Creating an object of the Person class
val firstPerson = new Person("Sarah", "Female", 25) 

// Accessing name, gender, and age
println(firstPerson.name)
println(firstPerson.gender)
println(firstPerson.age)
```

# 4. Singleton Objects: Companion

There are two types of singleton objects:

1. Companion Objects

2. Standalone Objects


### Companion Objects

```scala
import scala.collection.mutable
 
class ChecksumAccumulator {
  private var sum = 0
  def add(b: Byte) = sum += b
  def checksum() = ~(sum & 0xFF) + 1
}

//companion object of ChecksumAccumulator

object ChecksumAccumulator {
  private val cache = mutable.Map.empty[String, Int]
  def calculate(s: String): Int =
    if (cache.contains(s))
      cache(s)
    else {
      val acc = new ChecksumAccumulator
      for (c <- s)
        acc.add(c.toByte)
      val cs = acc.checksum()
      cache += (s -> cs)
      cs
    }
}

// Driver Code
val result = ChecksumAccumulator.calculate("hello")
print(result)
```

# 5. Singleton Objects: Standalone

Standalone Objects

```scala
import scala.collection.mutable
 
class ChecksumAccumulator {
  private var sum = 0
  def add(b: Byte) = sum += b
  def checksum() = ~(sum & 0xFF) + 1
}

//companion object of ChecksumAccumulator

object ChecksumAccumulator {
  private val cache = mutable.Map.empty[String, Int]
  def calculate(s: String): Int =
    if (cache.contains(s))
      cache(s)
    else {
      val acc = new ChecksumAccumulator
      for (c <- s)
        acc.add(c.toByte)
      val cs = acc.checksum()
      cache += (s -> cs)
      cs
    }
}

//standalone object that acts as an entry point for the ChecksumAccumulator application

import ChecksumAccumulator.calculate

object EntryApplication {
  def main(args: Array[String]) = {
    for(arg<-args)
      println(arg + ": " + calculate(arg))
  }
}
```






