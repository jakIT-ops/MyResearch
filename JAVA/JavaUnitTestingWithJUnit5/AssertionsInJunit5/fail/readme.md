## fail() method

Assertions API provide static fail() method. As soon as, any @Test method encounters fail() static method, it will fail the test case. The primary usages of fail() method are as follows -

* It gives a piece of meaningful information to the programmer writing a test, that test case is in progress and still needs to be implemented.

* It can be used to verify that an actual exception is thrown. Usually based on some input when test case expects an exception at a certain line, providing fail() below that line will verify that exception was not thrown as code execution reached fail() method line. Thus, it explicitly fails the test case.

```java
public static void fail()

public static void fail(String message)

public static void fail(Supplier<String> messageSupplier)
  
public static void fail(Throwable throwable)  
  
public static void fail(String message, Throwable throwable)  
```


