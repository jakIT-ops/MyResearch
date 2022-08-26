## Whe use std:: variant

Another handy wrapper type that we get in C++17 is <code>std::variant</code>. This is a type-safe union - you can store different type variants with the proper object lifetime guarantee. The new type offers a huge advantage over the C-style union. You can store all of the types inside - no matter if it’s something simple like int, or float, but also complex entities like std::vector<std::string>. In all of the cases, objects will be correctly initialised and cleaned up.

> What’s crucial is the fact that the new type enhances the implementation of design patterns. For example, you can now use a visitor, pattern matching and runtime polymorphism for unrelated type hierarchies in a much easier way.


### Things to remember

Here are the things to remember about <code>std::variant:</code>

* It holds one of several alternatives in a type-safe way

* No extra memory allocation is needed. The variant needs the size of the max of the sizes of the alternatives, plus some little extra space for knowing the currently active value

* By default, it initialises with the default value of the first alternative

* You can access the value through <code>std::get</code>, <code>std::get_if</code> or through a form of a visitor

* To check the currently active type you can use <code>std::holds_alternative</code> or <code>std::variant::index</code>

* <code>std::visit</code> provides a way to perform an operation that is implemented for any possible type that might currently be the active one in the variant. Such a polymorphic operation is represented by a callable object that implements its call-operator for every possible type that this variant can hold

* Rarely <code>std::variant</code> might get into an invalid state, you can check this issue with the valueless_by_exception() method

## Compiler support

| Feature | GCC | Clang |	MSVC |
| :------ | --- | ----- | ---------: |
| std::variant | 7.1 |	4.0 | VS 2017 15.0 |


