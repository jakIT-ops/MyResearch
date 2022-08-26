assertNotNull(Object actual) - It assert whether actual value is not null.

assertNotNull(Object actual, String message) - It assert whether actual value is not null. In case, if the actual value is null then test case will fail with the provided message.

assertNotNull(Object actual, Supplier<String> messageSupplier) - It assert whether actual value is not null. In case, if the actual value is null then test case will fail with the provided message through Supplier function. The main advantage of using Supplier function is that it lazily evaluates to String only when the test case fails.i


```java
public static void assertNotNull(Object actual)

public static void assertNotNull(Object actual, String message)

public static void assertNotNull(Object actual, Supplier<String> messageSupplier)
  
```



