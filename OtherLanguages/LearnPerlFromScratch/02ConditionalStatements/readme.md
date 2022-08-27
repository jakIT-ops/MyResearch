# 1. if-else Statement

### The `if-else` statement

```Perl
$a = 50; #change the value of "a" so its less than b in order to execute the else statement
$b = 15;

if ($a > $b) {
#this code is executed only if $a is greater than $b
  print "\$a is greater than \$b";
}
else {
#this code is executed if the preceding "if" condition evaluated to false
  print "\$a is less than \$b";
}
```

# 2. if-elsif-else Statement

### The `elsif` statement

```Perl
$score=50; #change the value of score to see other results

if ($score > 100){ # If score is greater than 100
print "Error: the score is greater than 100!\n";
}
elsif ($score < 0){ # Else If score is less than 0
print "Error: the score is less than 0!\n";
}
elsif ($score >= 50){ # Else if score is greater or equal to 50
print "Pass!\n";
}
else{ # If none above, then score must be between 0 and 49
print "Fail!\n";
}
```

# 2. Given and When Statement

example

```Perl
$color = 'Green'; #change value of color to see output for different cases

given ($color) {
when ('Red'){
print "The color is $color";
}
when ('Green'){
print "The color is $color";
}

default{   #executed if neither case 1 nor case 2 are executed
print "The color is neither 'Red' or 'Green'";
}
}
```

# 3. Ternary Operator

example

```Perl
$a=5; #Change values of $a and $b to change output of the code.
$b=2;

($a > $b) ? print "$a is greater than $b" : print  "$a is NOT greater than $b";
```
