Since C++11 and move semantics, passing strings has become much faster. You can end up with many temporary string copies. In C++17 you get a new type called <code>string_view</code>. It allows you to create a constant, non-owning view of a contiguous character sequence. You can manipulate that view and pass it around without the need to copy the referenced data.


### Compiler Support

| Feature |	GCC | Clang	 | MSVC |
| :------ | ------- | ---------- | ---: |
| std::string_view | 7.1 | 4.0 | VS 2017 15.0 |


