# 1. While Loop

Example
```perl
$x=4;
$y=0;
while ( $y <= 10 ) {   # the while loop will run till y<=10 condition is being met               
$y += $x;
$x += 1;
} #the loop will iterate 3 times
print "the value of x is: $x\n";
print "the value of y is: $y\n";
```

# 2. Do-while Loop

```perl
$number=5;
do{
  print "Value of number is: $number\n";
  $number++;
} while($number<=9); # the contition is being checked after the first run
```

# 3. For Loop

```perl
for ($i = 0; $i < 10; $i++){
  print "value of i is: $i\n";
}
```

# 4. Foreach Loop

```perl
@itemsToWrite = ('Alpha', 'Bravo', 'Charlie'); #an array of strings

foreach $item(@itemsToWrite){ #iterating through each element of array itemsToWrite
    print "$item\n"; #displaying each element of array in console
}  
```

# 5. Until Loop

```perl
$y=0;
until ( $y > 5 ) {   # the until loop will run "until" the condition is false               
$y += 1;
print "The value of y is: $y\n";
} #the loop will iterate 6 times
```

# 6. Equivalence of for Loop and while Loop

```perl
for ($i=0 ; $i<10 ; $i++){
  $i = $i*2;
  print "Value of i is: $i\n";
}
print "Final value of i is: $i\n";
```

### Converting a for loop into a while loop#

```perl
$i=0 ;
while ($i<10) {
  $i = $i*2;
  print "Value of i is: $i\n";
  $i++;
}
print "Final value of i is: $i\n";   
```

# 7. Infinite Loop


```perl
$a = 1;
  # the while condition will always be met as it will always return true
  while($a){
    print "Infinite loop\n";
  }
```
