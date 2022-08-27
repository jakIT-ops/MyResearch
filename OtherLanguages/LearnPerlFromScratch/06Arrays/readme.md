# 1. Arrays and their Operations

### Outputting a structured view of arrays

```perl
@fruits = ('Grapes', 'Apple', 'Banana' );

print "@fruits";
```


### The `..` operator

```perl
@integers = ( 0 .. 9);   # print from 0 to 9
@alphabets = (A .. Z);  # print form A to Z (Upper case)

print "@integers\n";
print "@alphabets";
```

### `pop` and `push` subroutines

```perl
@alphabets = (A .. F);

print "Original: @alphabets \n";
push (@alphabets, 'G');   # add G to the last index array

print "Pushing G in the array: @alphabets\n";

pop (@alphabets);   # removing last element of array

print "Removing last element from array: @alphabets\n";
pop (@alphabets);   # removing last element of array

print "Removing last element from array: @alphabets\n\n";
```

### `shift` and `unshift` subroutine

```perl
@alphabets = (a .. f);

print "Original: @alphabets \n";
shift (@alphabets);   # removing first element of the array

print "Removing first element from an array: @alphabets\n";

unshift (@alphabets, 'a');   # adding last element of the array

print "Adding first element to an array: @alphabets";
```


### Length of an array

```perl
@fruits = ("Orange", "Grapefruit", "Lemon");#initializing associative array
print "Length of fruits array is " . scalar(@fruits);
```


### Accessing element at a specific index

```perl
@fruits = ("Orange", "Grapefruit", "Lemon");#initializing associative array
print "Maximum index of fruits array is " . $#fruits . "\n";

print $fruits[1];  # accessing first index of fruits array
```

# 2. Multidimensional Arrays

```perl

@comparisonAdjectives= (["good", "better", "best"],
                        ["bad", "worse", "worst"],
                        ["tall", "taller", "tallest"]);

for ($i = 0; $i < 3 ; $i++) {
    for ($j = 0; $j < 3; $j++) {
        print $comparisonAdjectives[$i][$j] . " ";
    }
    print "\n";
}
```

# 3. Adding Elements in an Array

### Adding elements at the start using `unshift()`

```perl
@myArray = (2, 3);
print("Original: @myArray\n\n");

unshift(@myArray, 0, 1);
print("After adding 0 and 1: @myArray");
```

### Adding elements at the end using `push()`

```perl
@array = (1, 2, 3);
print("Original: @array\n\n");

push(@array, 4); # Pushing 4 at the end of $array
push(@array, 5); # Pushing 5 at the end of $array
print("After adding 4 and 5 at the end: @array");
```

# 4. Removing Element from an Array

### Removing element from the start

```perl
@myArray = (0, 1, 2, 3);
print("Original: @myArray\n\n");

shift(@myArray);
print("After removing 0 from the array: @myArray");
```

### Removing element at the end

```perl
@myArray = (0, 1, 2, 3);
print("Original: @myArray\n\n");

pop(@myArray); # removing 3 from the end of $array
print("Removing 3 from the end of the array: @myArray");
```

# 5. Sorting Arrays

### Sorting array of strings

```perl
#defining and array
@fruits = ('Rasberry', 'Orange', 'Apricot','Banana', 'Apple','Olive' );

@fruits = sort(@fruits); #applying the sort function
print("@fruits"); #printing the sorted array
```

### Sorting array of numbers

```perl
@numbers = (13, 9, 22, 27, 1, 3, -4, 10);
print "Original: @numbers\n\n";

@sorted_numbers = sort { $a <=> $b } @numbers;

print "After sorting: @sorted_numbers";
```
