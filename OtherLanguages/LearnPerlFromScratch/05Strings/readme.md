# 1. Strings Interpolation

### String interpolation

```perl
$name = 'Leo';
print "Hello $name, Nice to see you.";
# $name will be replaced with `Leo`
```


### Complex syntax

```perl
$name = 'Joel';
# Example using the \ syntax for the variable $name
print "We need more $name\s to help us!\n";
```

# 2. String Operators

### Concatenation

```perl
$a = "water";
$b = " bottle";
$c = $a . $b; # $c => water bottle
print $c;
```

### Concatenation assignment

```perl
$a = "Hello";
$a .= " World"; # $a => Hello World
print $a;
```

# 2. Built-in Subroutines

### Extracting substrings

```perl
$foo = "Hello world";

@arr = split("",$foo);
print $arr[6]; # returns w
print "\n";

print substr($foo, 6, 5); # returns 'world'
```

### Ways to display string

```perl
$str = q^A string with \^\^ delimiter ^;
$str1 = q{A string with q delimiter };
$str2 = 'A string with \'\' delimiter';
$str3 = "A string with \"\" delimiter";
$str4 = qq{A string with qq delimiter };


print $str , "\n";
print $str1 , "\n";
print $str2 , "\n";
print $str3 , "\n";
print $str4 , "\n";
```

### Finding position of a substring

```perl
$str = "The occurence of hay is hay at position:";

print $str . index($str, "hay")."\n";
```

### Changing letter case of a string

```perl
$foo = 'hello world';
$foo2 = 'HELLO WORLD';

print uc($foo), "\n"; # convert string to upper case
print lc($foo2), "\n"; # convert string to lower case
```

### Calculating the length of a string

```perl
$my_str = 'Welcome to Educative!';

print length($my_str); # returns 21 which is number of characters
```

### Reversing a string

```perl
$my_str = '!lrep gninraeL';

# Display reversed string
$print = reverse($my_str);
print $print;
```
