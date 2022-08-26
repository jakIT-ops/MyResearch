1. assertNull(Object actual) - It asserts whether actual value is null or not.

2. assertNull(Object actual, String message) - It asserts whether actual value is null or not. In case, if the actual value is not null then the test case will fail with a provided message.

3. assertNull(Object actual, Supplier<String> messageSupplier) - It assert whether actual value is null or not. In case, if the actual value is not null then the test case will fail with a provided message through Supplier function. The main advantage of using Supplier function is that it lazily evaluates to String only when the test case fails.

```java
public static void assertNull(Object actual)

public static void assertNull(Object actual, String message)

public static void assertNull(Object actual, Supplier<String> messageSupplier)
```




