# Unit Test

## What is it?

A unit test is a way of testing of unit,
the smallest piece of code that can be logically isolated in a program

# Test file

* Naming
  - Snake case
  - Starts with name of the file in question
  - Ends with "_test.go"
  - main_test.go for main.go
- Placement
  - Same package
  ```
  math
    |_math.go
    |_math_test.go
  ```
  - Test package
  ```
  math
    |_ math.go
  math_test.go
    |_ math_test.go
  ```

# Test case


* Naming
  - Pascal case
  - Starts with "Test"
  - Followed by name of function in question
  - TestF for function F()
  - TestT & TestT_M for
  ```
  type T struct {}
  func (T) M() {}
  ```
- Usage
  - import package
  ```
  import "testing"
  ```
  - testing.T struct
  ```
  func TestF(t *testing.T) {
    //....
  }
  ```
