# Introduction to Operators

```perl
$a = 10;
$b = 4;
print "\$a + \$b = ". ($a + $b);   #addition
print "\n";
print "\$a - \$b = ".($a - $b);   #subtraction
print "\n";
print "\$a * \$b) = ". ($a * $b); #multiplication
print "\n";
print "\$a / \$b = ". ($a / $b);  #division
print "\n";
print "\$a % \$b = ".($a % $b);   #modulus returns the remainder of the $a / $b
print "\n";
print "\$a ** \$b = ".($a ** $b);   #Exponent (10^4) = 10 * 10 * 10 * 10
```

# Precedence and Associativity

```perl
print "5 - 3 + 2 = ". (5-3+2);    # 5-3+2 is treated as (5-3)+2
print "\n";
print "5 - (3 + 2) = ". (5-(3+2));    # 5-3+2 is treated as 5-(3+2) => 0
print "\n";
print "5 + 3 * 2 = ". (5+3*2);    # 5+3*2 is treated as 5+(3*2)
print "\n";
print "15 / 3 * 5 = ". (15/3*5);  # 15/3*5 is treated as (15/3)*5
print "\n";
print "42 + 7 % 2 = ". (42+7%2);  # 42+7%2 is treated as 42+(7%2)
print "\n";
print "(42 + 7) % 2 = ". ((42+7)%2);  # 42+7%2 is treated as (42+7)%2 => 1
print "\n";
$a = 6;
print "6 += 4 => ". ($a += 4);     # compined addition operators have right associativity.
```

### Operators with the same precedence and associativity#

```Perl
$a = 5 * 3 % 2; # $a now is (5 * 3) % 2 => (15 % 2) => 1
print $a."\n";
$a = 5 % 3 * 2; # $a now is (5 % 3) * 2 => (2 * 2) => 4
print $a."\n";
```

# Relational Operators

Example
```perl
$a = 4;
$b = 4;
if ($a != $b) {
  print 'a and b are not equal';  # this will not be printed
}
if ($a == $b) {
  print 'a and b are equal';
}
```

```perl
$a = 6;
$b = 8;

if($b > $a){     # greater than
  print ("Yes -- $b is greater than $a\n");
}
else{            
  print ("No -- $b is not greater than $a\n");
}
if($a < $b){     # Less than
  print ("Yes -- $a less than $b\n");
}
else{
  print ("No -- $a is not less than $b\n");
}
if($a <= $b){    # Less than or equal to
  print ("Yes -- $a is less than or equal to $b\n");
}
else{
  print ("No -- $a is not less than or equal to $b\n");
}
if($b >= $a){    # Greater than or equal to
  print ("Yes -- $b is greater than or equal to $a\n");
}
else{
  print ("No -- $b is not greater than or equal to $a\n");
}
```

### `cmp` operator
The cmp operator is just like the <=> operator, except that it is constructed to work with the string operands.

```perl
# Strings
print (("a" cmp "a").","); #prints 0
print (("a" cmp "b").","); #prints -1
print ("b" cmp "a");       #prints 1
```

# Logical Operators

### `and`

```perl
$x=7;
$y=6;
$z=2;

if($x > $y && $x > $z) {
  print "You're in IF statement";
}
else {
  print "You're in ELSE statement";
}
```

### `or`

```perl
$x = 7;
$y = 10;
$z = 2;

if($x > $y || $x > $z){
  print "Successful!";
}
else {
  print "Failed!";
}
```

### `not`

```perl
$x = 7;
$y = 10;


if(!($x > $y)){
  print "Passed!";
}
else {
  print "Failed!";
}
```

# Assignment Operators

```perl
$a = 3;
print "\$a = ".$a;    #prints $a = 3
$b = ($a = 5);        #assigns 5 to $a and then assigns the value of $a to $b
print "\n\$a = ".$a;  #prints $a = 5
print "\n\$b = ".$b;  #prints $b = 5    
```
