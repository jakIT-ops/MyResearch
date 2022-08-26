## Template Argument Deduction for Class Templates


C++17 has filled a gap in the deduction rules for templates. Now template deduction can occur for standard class templates and not just for functions. That also means that a lot of your code that uses <code>make_Type</code> functions can now be removed.

For instance, to create an <code>std::pair</code> object, it was usually more comfortable to write:
```c++
auto myPair = std::make_pair(42, "hello world");
```
Rather than:
```c++
std::pair<int, std::string> myPair(42, "hello world");
```

Now, since C++17, the conformant compiler will nicely deduce the template parameter types for class templates too!

> The feature is called “Class Template Argument Deduction” or CTAD in short.

In our example, you can now write:
```c++
using namespace std::string_literals;
std::pair myPair{42, "hello world"s};     // deduced automatically!
```
CTAD also works with copy initialisation and when allocating memory through new():
```c++
auto otherPair = std::pair{42, "Hello"s}; // also deduced
auto ptr = new std::pair{42, "World"s};   // for new
```

CTAD can substantially reduce complex constructions like:

```c++
#include <iostream>
#include <mutex>
#include <shared_mutex>
using namespace std;

int main(){
// lock guard:
std::shared_timed_mutex mut;
std::lock_guard<std::shared_timed_mutex> lck(mut);

// array:
std::array<int, 3> arr {1, 2, 3};
for(int i = 0; i < 3; i++){
cout << arr[i] << " ";
}
}
```

## Fold Expressions

<code>C++11</code> introduced variadic templates which is a powerful feature, especially if you want to work with a variable number of input template parameters to a function.

### Previously

Pre <code>C++11</code> you had to write several different versions of a template function (one for one parameter, another for two parameters, another for three params… ).

```c++
auto SumCpp11(){
  return 0;
}
template<typename T1, typename... T>
auto SumCpp11(T1 s, T... ts){
  return s + SumCpp11(ts...);
}
```

### Witch C++17

```c++
template<typename ...Args> auto sum(Args ...args){
  return (args + ... + 0);
}
// or even:
template<typename ...Args> auto sum2(Args ...args){
  return (args + ...);
}
```

## Template Code Simpplification

Before C++17 if you had several versions of an algorithm - depending on the type requirements - y​ou could use SFINAE or tag dispatching to generate a dedicated overload resolution set.

```c++
#include <iostream>
#include <type_traits>

template <typename T>
std::enable_if_t<std::is_integral_v<T>, T> simpleTypeInfo(T t) {
    std::cout << "foo<integral T> " << t << '\n';
    return t;
}

template <typename T>
std::enable_if_t<!std::is_integral_v<T>, T> simpleTypeInfo(T t) {
    std::cout << "not integral \n";
    return t;
}

int main() {
    simpleTypeInfo(10);
    simpleTypeInfo(10.5f);
    
    return 0;
}
```

Now, instead of SFINAE, we generate a unique type tag for the condition: <code>true_type</code> or <code>false_type</code>. Depending on the result, only one implementation is selected.

```c++
template <typename T>
T simpleTypeInfo(T t) {
    if constexpr (std::is_integral_v<T>) {
        std::cout << "foo<integral T> " << t << '\n';
    }
    else {
        std::cout << "not integral \n";
    }
    return t;
}
```

## Declaring Non-Type Template Parameters With auto

This is another part of the strategy to use auto everywhere. With C++11 and C++14 you can use it to deduce variables or even return types automatically, plus there are also generic lambdas. Now you can also use it for deduci​ng non-type template parameters. For example:

```c++
template <auto value> void f() { }
...
f<10>(); // deduces int
```

This is useful, as you don’t have to have a separate parameter for the type of non-type parameter. Like in C++11/14:

```c++
template <typename Type, Type value> constexpr Type TConstant = value;
...
constexpr auto const MySuperConst = TConstant<int, 100>;
```

With C++17 it’s a bit simpler:

```c++
template <auto value> constexpr auto TConstant = value;
...
constexpr auto const MySuperConst = TConstant<100>;
```

## Compiler Support

| Feature |	GCC |	Clang |	MSVC  |
| :------ | ------- | ------- | ----: |
| Template argument deduction for class templates | 7.0/8.0[^gccimprov] | 5.0 |	VS 2017 15.7 |
| Deduction Guides in the Standard Library | 8.0[^gccguides] | 7.0/in progress[^clangdeductionprogress] | VS 2017 15.7 |
| Declaring non-type template parameters with auto | 7.0 | 4.0 | VS 2017 15.7 |
| Fold expressions | 6.0 | 3.9 | VS 2017 15.5 |
| <code>if constexpr</code> | 7.0 | 3.9 | VS 2017 |


