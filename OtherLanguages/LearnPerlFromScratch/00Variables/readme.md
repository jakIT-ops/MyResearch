# 1. Variables and Data Types

A variable in any programming language is a named piece of computer memory to hold some program data. Variables are an essential part of a computer program.

```js
$string = "This is a string.";   # stores string
$int = 5;     # stores an integer
$float = 5.7;    # stores a floating point type value
$char = 'a';    # stores character type value

print $string, "\n";
print "An integer type: ", $int, "\n";
print "A float type: ", $float, "\n";
print "A character type: ", $char, "\n";
```

### Escape characters

```js
print "Hello World!\n";    # \n inserts a new line
print "Hello\tWorld!\n";    # \t adds a tab space
print "\"Double quotes\"\n";  # use \ to add double quotes
print '\'Single quotes\'';  # use \ to add single quotes
```

### Boolen

```js
$false = 0;    # reutrns false
$true = 1;   # any values greater or less than 0 returns true
```


### Integer

```js
$negative = -3; # negative
$zero = 0; # zero (can also be false, if used as a Boolean
$positive = 123; # positive decimal
$zeroPos = 0123; #0 prefix is used to sepcify octal - octal value = 83 decimal
$hex = 0xAB; #0x prefix is used to specify hexadecimal - hexadecimal value = 171 decimal
$bin = 0b1010; # 0b prefix is used to specify binary - binary value = 10 decimal
print $negative," " ,$zero," " , $positive," " , $zeroPos," " , $hex," " , $bin;
```

### Float

```js
$float1 = 1.23;
$float2 = 10.0000001;
print $float1," ",$float2;
```


### Array

```js
@intarray = (1, 2, 3); # An array of integers
print "@intarray \n";

@floatarray = (1.123, 2.356, 19.76); # An array of floats
print "@floatarray \n";

@chararray = ('a', 'b','c'); # An array of characters
print "@chararray \n";

@mixed = (1, 2, 3, 'a', 'b', 'c'); #contains both characters and numbers
print "@mixed";
```


### String

```js
$string1 = "A quick brown fox jumps over the lazy dog";
print $string1;
```
