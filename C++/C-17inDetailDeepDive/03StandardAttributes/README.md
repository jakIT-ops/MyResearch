## Whe do we need attributes

### What is an attribute?

An attribute is an additional information that can be used by the compiler to produce code. It might be utilized for optimization or some specific code generation (like DLL stuff, OpenMP, etc.). In addition, annotations allow you to write more expressive syntax and help other developers to reason about code.

Contrary to other languages such as C#, in C++ that the compiler fixes meta information, you cannot add user-defined attributes. In C# you can ‘derive’ from <code>System.Attribute.</code>

### What's best about Modern C++ attributes?

Since C++11, we get more and more standardised attributes that will work with other compilers. We’re moving away from compiler-specific annotation to standard forms. Rather than learning various annotation syntaxes you’ll be able to write code that is common and has the same behaviour.


## Before C++11

### GCC Specific Attributes

```c++
int square(int) __attribute__ ((pure)); // pure function
```

Documentation

* [Attribute Syntax - Using the GNU Compiler Collection (GCC)](https://gcc.gnu.org/onlinedocs/gcc-4.8.1/gcc/Attribute-Syntax.html)
* [Using the GNU Compiler Collection (GCC): Common Function Attributes](https://gcc.gnu.org/onlinedocs/gcc/Common-Function-Attributes.html#Common-Function-Attributes)

### MSVC Specific Attributes

```c++
__declspec (deprecated) void LegacyCode() {}
```

## Attributes in C++11/c++14

### Specifying Annotations in C++11

```c++
[[attrib_name]] void foo() { }      // on a function
struct [[deprecated]] OldStruct { } // on a struct
```

### C++14 Additions

```c++
#include <iostream>
using namespace std;

[[deprecated("use AwesomeFunc instead")]] void GoodFunc() { }

int main()
{
  GoodFunc(); 
}
```

## C++17 additions

#### Two new Attributes

[[fallthrough]] attribute
```c++
switch (c) 
{
  case 'a':
    f(); // Warning! fallthrough is perhaps a programmer error
  case 'b':
    g();
    [[fallthrough]]; // Warning suppressed, fallthrough is ok
  case 'c':
    h();
}
```

[[maybe-unused]] attribute

```c++
static void impl1() { ... } // Compilers may warn about this

[[maybe_unused]] static void impl2() { ... } // Warning suppressed

void foo() 
{
  int x = 42; // Compilers may warn when x is not used later
  [[maybe_unused]] int y = 42; // Warning suppressed for y
}
```

## Summary

### All Attributes available in C++17

| Attribute | Description  |
| :-------- | -----------: | 
| [[noreturn]] | a function does not return to the caller |
| [[carries_dependency]] | extra information about dependency chains |
| [[deprecated]] | an entity is deprecated |
| [[deprecated("reason")]] | provides additional message about the deprecation |
| [[fallthrough]] | indicates a intentional fall-through in a switch statement |
| [[nodiscard]] | a warning is generated if the return value is discarded |
| [[maybe_unused]] | an entity might not be used in the code |


## Compiler Support

| Feature  | GCC  |  	Clang |	MSVC |
| :------- | ---- | --------- | ---: |
| <code>[[fallthrough]]</code> | 7.0 | 3.9 | 15.0 |
| <code>[[nodiscard]]</code> | 7.0 | 3.9 | 15.3 |
| <code>[[maybe_unused]]</code> | 7.0 |	3.9 | 15.3 |
| Attributes for namespaces and enumerators | 4.9/6[^gccnote] | 3.4 | 14.0 |
| Ignore unknown attributes |	All versions	| 3.9 | 14.0 |
| Using attribute namespaces without repetition | 7.0 |	3.9 | 15.3 |


