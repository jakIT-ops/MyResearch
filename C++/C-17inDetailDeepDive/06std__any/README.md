### Why use std::any?

With std::optional you can represent a regular Type values or mark it as empty. With std::variant you can wrap several type alternatives into one entity.

> C++17 gives us one more wrapper type: std::any which can hold anything in a type-safe way.

### Performance & Memory Considerations

| Compiler | sizeof(any) |
| :------- | ----------: |
| GCC 8.1 (Coliru) |	16 |
| Clang 7.0.0 (Wandbox) |	32 |
| MSVC 2017 15.7.0 32-bit |	40 |
| MSVC 2017 15.7.0 64-bit |	64 |

## Summary

Some of the highlights are as follows:

* std::any is not a template class
* std::any uses Small Buffer Optimisation, so it will not dynamically allocate memory for simple types like ints, doubles… but for larger types, it will use extra new.
* std::any might be considered ‘heavy’, but offers a lot of flexibility and type-safety.
* you can access the currently stored value by using any_cast that offers a few “modes”: for example it might throw an exception or return nullptr.
* use it when you don’t know the possible types - in other cases consider std::variant.

## Compiler Support

| Feature	GCC |	Clang |	MSVC |
| std::any |	7.1 |	4.0  | VS 2017 15.0| 


