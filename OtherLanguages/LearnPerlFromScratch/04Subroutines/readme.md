# Introduction to Subroutines

### What is a subroutine?

A subroutine is a block of code that is written in order to perform a specific task.

Let’s discuss a real-life example to understand the concept better. While using a vending machine, we put the money in the machine and select the desired item to be purchased. The machine gives back the requested product. To accomplish this task, there is a subroutine written at the backend.

Subroutines work in a similar way. They take the required information to perform a task as input parameter(s), perform the required operations on these parameters, and then return the final answer.

### Types of subroutines

In Perl, there are two major types of subroutines:

* Built-in subroutines

* User-defined subroutines

```perl
sub Examplesubroutine { #subroutine that outputs some text
    print "This is a user-defined subroutine";
}

# Calling the subroutine
Examplesubroutine();
```

# 1. Variable Scope

### Types of variables

Local variables

```perl
$number = 20;   # if my is not used then its scope is global

sub foo{
  my $num = 10;  # using my keyword for local variable
  print "Local Variable value" .$num . "\n";
}
foo(); #Will print 10 because text defined inside function is a local variable

print "global Variable value " . $number . "\n";
```

Global variables

```perl
$num1 = 5;  # global variables
$num2 = 2;

sub multiply(){
  $::num1 = 10;
  $::num2 = 20;
  return  $num1 * $num2;
}

# When in the global scope, regular global variables can be used
# without explicitly stating '$::variablename'
print "num1 is: $num1\n";
print "num2 is: $num2\n";
print multiply();
```

# 2. Passing Arguments in Subroutines

Example

```perl
#subroutine with two parameters
sub mySubroutine{
    $num1 = @_[0];
    $num2 = @_[1];

    print  "The value assigned to num1 is $num1\n";
    print  "The value assigned to num2 is $num2";
}
#calling subroutine and passing arguments to it
mySubroutine(3,4);
```


# 3. Passing Parameters by Value

### Example: swap numbers

```perl
sub swap{ #parameters num1 and num2 passed using pass by value method
  my $a = @_[0];
  my $b = @_[1];

  my $temp = $a;   #creating a variable temp and setting equal to arg2
  $a = @_[1];  #setting the value of arg2 equal to arg1
  $b = $temp;  #setting the value of arg1 equal to temp which is equal to arg2
}

$num1 = 4;
$num2 = 5;

# Have a careful look at this function call
print "num1 is: $num1\n";
print "num2 is: $num2\n";
print "\nAfter swapping\n\n";

swap($num1,$num2);
print "num1 is: $num1\n";
print "num2 is: $num2";
```

# 4. Passing Parameters by Reference

### Example: swap numbers

```Perl
sub swap{ #parameters num1 and num2 passed using pass by value method

  $temp = $_[0];   #creating a variable temp and setting equal to $_[0]
  $_[0] = $_[1];  #setting the value of $_[0] equal to $_[1]
  $_[1] = $temp;  #setting the value of $_[1] equal to temp which is equal to $_[0]
}

$num1 = 4;
$num2 = 5;

# Have a careful look at this function call
print "num1 is: $num1\n";
print "num2 is: $num2\n";
print "\nAfter swapping\n\n";

swap($num1,$num2);
print "num1 is: $num1\n";
print "num2 is: $num2";
```
