val result = getFullName()
val first = result.first
val middle = result.second
val last = result.third

println("$first $middle $last") //John Quincy Adams


val (first, middle, last) = getFullName() 

println("$first $middle $last") //John Quincy Adams


