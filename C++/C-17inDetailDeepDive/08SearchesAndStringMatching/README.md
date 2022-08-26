### std::search in C++14#

<code>std::search</code> in <code>C++14</code> offers a generic way to search for a pattern in a given range. The algorithm can be used not only for character containers but also for containers with custom types. This technique was, unfortunately, a bit limited as the performance was usually slow - it uses the naive matching algorithm, with the complexity of the size of the pattern times the size of the text.

### std::search in C++17

With <code>C++17</code> we get new <code>std::search</code> overloads that expose new and powerful algorithms like Boyer Moore variations that have linear complexity in the average case.


## Overview of String Matching Algorithms

### String Matching

String-matching consists of finding one or all of the occurrences of a string (“pattern”) in a text. The strings are built over a finite set of characters, called “alphabet”.

| Algorithm | Preprocessing | Matching | Space |
| :-------- | ------------- | -------- | ----: |
| Naive string-search |	none |	O(nm) |	none  |
| Rabin–Karp |	O(m) |	average O(n + m), worst O((n−m)m) | O(1) |
| Knuth–Morris–Pratt | O(m) | O(n) | O(m) |
| Boyer–Moore |	O(m + k) | best O(n/m), worst O(mn) | O(k) |
| Boyer–Moore-Horspool | O(m + k) | best O(n/m), worst O(mn) | O(k) |

### Before c++17

```c++
template< class ForwardIt1, class ForwardIt2 >
ForwardIt1 search( ForwardIt1 first, ForwardIt1 last,
                   ForwardIt2 s_first, ForwardIt2 s_last );
```

## New Algorithms Available in C++ 17

C++17 updated std::search algorithm in two ways:

* You can now use execution policy to run the default version of the algorithm in a parallel way.
* You can provide a Searcher object that handles the search.

In C++17 we have three searchers:

* <code>default_searcher</code> - same as the version before C++17, usually meaning the naive approach. Operates on Forward Iterators.
* <code>boyer_moore_searcher</code> - uses Boyer Moore Algorithm - the full version, with two rules: bad character rule and good suffix rule. Operates on Random Access Iterators.
* <code>boyer_moore_horspool_searcher</code> - Simplified version of Boyer-Moore that uses only Bad Character Rule, but still has good average complexity. Operates on Random Access Iterators.


### Using Searchers

```c++
template<class ForwardIterator, class Searcher>
ForwardIterator search(ForwardIterator first, ForwardIterator last, const Searcher& searcher );
```

```c++
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main(){
    string testString = "Hello Super World";
    string needle = "Super";
    const auto it = search(begin(testString), end(testString), boyer_moore_searcher(begin(needle), end(needle)));

    if (it == cend(testString))
        cout << "The string " << needle << " not found\n";
    return 0;
}
```

# Examples - Using Searchers

### Example benchmarks:

* The <code>std::string;:find</code> version:

```c++
RunAndMeasure("string::find", [&]() {
  for (size_t i = 0; i < ITERS; ++i)
  {
    std::size_t found = testString.find(needle);
    if (found == std::string::npos)
      std::cout << "The string " << needle << " not found\n";
  }
});
```

* The <code>default</code> version:

```c++
RunAndMeasure("default searcher", [&]() {
    for (size_t i = 0; i < ITERS; ++i)
    {
        auto it = std::search(testString.begin(), testString.end(),
            std::default_searcher(
                needle.begin(), needle.end()));
        if (it == testString.end())
            std::cout << "The string " << needle << " not found\n";
    }
});
```

* The <code>boyer_moore</code> version:

```c++
RunAndMeasure("boyer_moore_searcher", [&]() {
    for (size_t i = 0; i < ITERS; ++i)
    {
        auto it = std::search(testString.begin(), testString.end(),
            std::boyer_moore_searcher(
                needle.begin(), needle.end()));
        if (it == testString.end())
            std::cout << "The string " << needle << " not found\n";
    }
});
```

* The <code>boyer_moore_horspool</code> version:

```c++
RunAndMeasure("boyer_moore_horspool_searcher", [&]() {
for (size_t i = 0; i < ITERS; ++i)
{
  auto it = std::search(testString.begin(), testString.end(),
  std::boyer_moore_horspool_searcher(needle.begin(), needle.end()));
  if (it == testString.end())
    std::cout << "The string " << needle << " not found\n";
}
});
```

Here are some of the results running the application on Win 10 64bit, i7 8700, 3.20 GHz base frequency, 6 cores/ 12 threads (the application runs on a single thread, however). The string size is 547412 bytes (comes from a 500KB text file), and we run the benchmark 1000 times.


| Algorithm |	GCC 8.2 |	Clang 7.0 |	Visual Studio (Release x64) |
| :-------- | --------- | --------------- | ------------------------------: |
| string::find	| 579.48	| 367.90 |	380.78 |
| default searcher | 391.99 | 552.02 | 604.33 |
| boyer_moore_searcher | 37.89 (init 3.98) | 32.73 (init 3.02) | 34.71 (init 3.52) |
| boyer_moore_horspool_searcher | 30.943 (init 0) | 28.72 (init 0.5) |	31.70 (init 0.69) |

Here are the results from another run, this time we use the same input string (from a 500KB text file), we perform 1000 iterations, but the pattern is only 48 letters. It’s a sentence that’s located at the end of the file (a single occurrence).

| Algorithm |	GCC 8.2 |	Clang 7.0 |	Visual Studio (Release x64)  |
| :-------- | --------- | --------------- | -------------------------------: |
| string::find | 164.58	 | 39.63 | 40.28  |
|default searcher | 102.75 | 332.98 | 396.11 |
| boyer_moore_searcher | 115.69 (init 0.96) | 95.56 (init 0.45)	| 101.73 (init 0.49) |
| boyer_moore_horspool_searcher | 100.74 (init 0) | 97.48 (init 0.21) |	105.44 (init 0.23) |

# DNA Matching

To demonstrate the range of uses for <code>std::search</code>, let’s have a look at a simple DNA matching demo. The example will match custom types rather than regular characters.

For instance, we’d like to search a DNA sequence to see whether <code>GCTGC</code> occurs in the sequence <code>CTGATGTTAAGTCAACGCTGC</code>.

The code block uses a simple data structure for Nucleotides:

```c++
struct Nucleotide {
    enum class Type : uint8_t {
        A = 0,
        C = 1,
        G = 3,
        T = 2
    };
    
    Type mType;
    
    friend bool operator==(Nucleotide a, Nucleotide b) noexcept {
        return a.mType == b.mType;   
    }
    
    static char ToChar(Nucleotide t);
    static Nucleotide FromChar(char ch);
};
```

With the two converting static methods:

```c++
char Nucleotide::ToChar(Nucleotide t) {
    switch (t.mType) {
    case Nucleotide::Type::A: return 'A';
    case Nucleotide::Type::C: return 'C';
    case Nucleotide::Type::G: return 'G';
    case Nucleotide::Type::T: return 'T';
    }
    return 0;
}

Nucleotide Nucleotide::FromChar(char ch) {
    return Nucleotide { static_cast<Nucleotide::Type>((ch >> 1) & 0x03) };
}
```

And the two functions that work on a whole string:

```c++
std::vector<Nucleotide> FromString(const std::string& s) {
    std::vector<Nucleotide> out;
    out.reserve(s.length());
    std::transform(std::cbegin(s), std::cend(s), 
                   std::back_inserter(out), Nucleotide::FromChar);
    return out;
}

std::string ToString(const std::vector<Nucleotide>& vec) {
    std::stringstream ss;
    std::ostream_iterator<char> out_it(ss);
    std::transform(std::cbegin(vec), std::cend(vec), out_it, Nucleotide::ToChar);
    return ss.str();
}
```

The demo uses <code>boyer_moore_horspool_searcher</code> which requires hashing support. So we have to define it as follows:

```c++
namespace std {
    template<> struct hash<Nucleotide> {
        size_t operator()(Nucleotide n) const noexcept {
            return std::hash<Nucleotide::Type>{}(n.mType);
        }
    };
}
```

<code>std::hash</code> has support for enums, so we just have to “redirect” it from the whole class.

And then the test code:

```c++
const std::vector<Nucleotide> dna = FromString("CTGATGTTAAGTCAACGCTGC");
std::cout << ToString(dna) << '\n';
const std::vector<Nucleotide> s = FromString("GCTGC");
std::cout << ToString(s) << '\n';

std::boyer_moore_horspool_searcher searcher(std::cbegin(s), std::cend(s));
const auto it = std::search(std::cbegin(dna), std::cend(dna), searcher);
        
if (it == std::cend(dna))
    std::cout << "The pattern " << ToString(s) << " not found\n";
else {
    std::cout << "DNA matched at position: " 
              << std::distance(std::cbegin(dna), it) << '\n';
}
```

The Nucleotide type wastes a bit of space - as we use the full byte just to store four options - C T G A. We could use only 2 bits, though the implementation would be more complicated. Another option is to represent the triplets of Nucleotides - Codons. Each codon can be expressed in 6 bits, so that way we’d use the full byte more efficiently.


### Summary

<code>std::search</code> with searchers is a general algorithm that works for most of the containers that expose random access iterators. If you work with strings and characters, then you might also compare it against 

<code>std::string::find</code>, which is usually specialised and optimised for character processing (implementation-dependent!).

## Compiler Support

| Feature |	GCC	 | Clang	| MSVC |
| :------ | ----------- |------------- | ------: |
| Searchers| 	7.1 |	3.9	| VS 2017 15.3 |
















