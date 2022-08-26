# 1. Removed or Fixed Languge Features

The C++17 Standard contains over 1600 pages, growing over 200 pages compared to C++14 [^note1]! Fortunately, the language specification was cleaned up in a few places, and some old or potentially harmful features could be cleared out.

One of the core concepts behind each iteration of C++ is its compatibility with previous versions. We’d like to have new things in the language, but at the same time, our old projects should still compile.

### Compiler Support

| Feature   | 	GCC 	|	Clang 	| 	MSVC |
| :-------- | --------- | ------------- | ---------: |
| Removing <code>register</code> keyword | 7.0 | 3.8 | VS 2017 15.3 |
| Remove Deprecated <code>operator++</code>(bool) | 7.0 | 3.8 |	VS 2017 15.3 |
| Removing Deprecated Exception Specifications | 7.0| 4.0 | VS 2017 15.5 |
| Removing trigraphs | 5.1 | 3.5 | VS 2010 |
| New auto rules for direct-list-initialisation | 5.0 |	3.8 | VS 2015 |
| <code>static_assert<code> with no message | 6.0 | 2.5 | VS 2017 |
| Different begin and end types in range-based for | 6.0 | 3.6 | VS 2017 |

# 2. Removed And Deprecated Library Features

In the chapter about Removed or Fixed Language Features, we focused only on the language side. But The Standard Library was also cleaned-up in C++17. This chapter shows the list of most [^mostdepr] of the removed or deprecated types and utilities.

### Compiler Support

| Feature  |	GCC    |	Clang |  MSVC 	 |
| :------- | --------- | ------------ | -------: |
| Removing <code>auto_ptr</code>, <code>random_shuffle</code>, old <functional> stuff |	No [^gccfunccompat] | not yet | VS 2015 |
| Deprecating <code>std::iterator</code> | not yet | not yet | VS 2017 15.5 |
| Deprecating <code>shared_ptr::unique()</code> | not yet | not yet | VS 2017 15.5 |
| Deprecating <codecvt>	| not yet | not yet | VS 2017 15.5 |
| Removing Deprecated Iostreams Aliases | not yet | 3.8 | VS 2015.2 |
| Deprecate <code>result_of</code> | not yet | not yet | VS 2017 15.3 |
| Removing Allocator Support In <code>std::function</code> not yet | 4.0 | VS 2017 15.5 |
| C++17 should refer to C11 instead of C99 | 9.1 | 7.0 | VS 2015 |
| Removing Deprecated Iostreams Aliases	| not yet | 3.8 | VS 2015.2 |

# 2. Language Clarification

One of the reasons for the lack of clarity might be the freedom given to the implementation/compiler. For example, some parts of the language are left vague to allow for more aggressive optimisations. Other difficulties can arise from the requirement to be compatible with C.

## 2.1 Expression Evaluation Order

### Expression Evaluation: C++ Older Version

Until C++17 the language hasn’t specified any evaluation order for function parameters. Period.

For example, that’s why in C++14 <code>make_unique</code> is not just syntactic sugar, but it guarantees memory safety.

Let’s have a look at the following example:

```c++
foo(unique_ptr<T>(new T), otherFunction()); // first case
```
And without explicit new:
```c++
foo(make_unique<T>(), otherFunction()); // second case
```

### Expression Evaluation: C++17

C++17 addresses the issue shown in the first case. Now, the evaluation order of function arguments is “practical” and predictable. In our example, the compiler won’t be allowed to call <code>otherFunction()</code> before the expression <code>unique_ptr<T>(new T)</code> is fully evaluated.

In an expression:
```c++
f(a, b, c);
```

The order of evaluation of a, b, c is still unspecified, but any parameter is fully evaluated before the next one is started. It’s especially crucial for complex expressions like this:

```c++
f(a(x), b, c(y));
```

### Compiler Support

| Feature |	GCC |	Clang |	MSVC  |
| :------- | ------- | ------- | ----: |
| Stricter expression evaluation order |	7.0 |	4.0 |	VS 2017 |
| Guaranteed copy elision	| 7.0|	4.0 | VS 2017 15.6 |
| Dynamic memory allocation for over-aligned data | 7.0 | 4.0 |	VS 2017 15.5 |
| Exception specifications part of the type system | 7.0 | 4.0 | VS 2017 15.5 |
