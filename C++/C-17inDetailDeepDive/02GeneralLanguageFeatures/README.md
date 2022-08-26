## Structured Binding Declarations

If not, then you should probably start looking into those handy types. Tuples enable you to bundle data ad-hoc with excellent library support instead of creating small custom types. The language features like structured binding make the code even more expressive and concise.

```c++
#include <iostream>
#include <set>
#include <tuple>

int main(){
  std::set<int> mySet;
  std::set<int>::iterator iter;
  bool inserted;

  std::tie(iter, inserted) = mySet.insert(10);
  if (inserted)
    std::cout << "Value was inserted\n";
}
```

```c++
std::set<int> mySet;
auto [iter, inserted] = mySet.insert(10);
```

<code>const</code> modifiers
```c++
const auto [a, b, c, ...] = expression;
```

References
```c++
auto& [a, b, c, ...] = expression;
auto&& [a, b, c, ...] = expression;
```

For example

```c++
#include <iostream>
using namespace std;

int main() {
  std::pair a(0, 1.0f);
  auto& [x, y] = a;
  x = 10; // write access
  std::cout << a.first;// a.first is now 10
}
```

### Compiler Support

| Feature | GCC | Clang | MSVC |
| :------ | --- | ----- | ---- |
| Structured Binding Declarations | 7.0 | 4.0 |	VS 2017 15.3 |
| Init-statement for if/switch | 7.0 | 3.9 | VS 2017 15.3 |
| Inline variables | 7.0 | 3.9 | VS 2017 15.5 |
| <code>constexpr</code> Lambda Expressions | 7.0 | 5.0 | VS 2017 15.3 |
| Lambda Capture of *this | 7.0 | 3.9 |	VS 2017 15.3 |
| Nested namespaces | 6.0 | 3.6 | VS 2015 |
| <code>has_include</code> | 5  | Yes | VS 2017 15.3 |






























