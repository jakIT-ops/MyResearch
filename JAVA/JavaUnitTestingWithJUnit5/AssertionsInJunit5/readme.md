# Assertions in JUnit 5

JUnit 5 assertions help us in validating the expected output with the actual output of a test case. In short, assertions are nothing but static methods that we call in our tests to verify expected behavior. All JUnit Jupiter assertions are present in the org.junit.jupiter.Assertions class.

These methods support Java 8 lambda expressions and are extensively overloaded to support different types such as primitives, objects, streams, arrays etc.

| Assert Method	| What It Does |
| :------------ | -----------: |
| assertNull()  | Asserts that actual is null. |
| assertNotNull()| Asserts that actual is not null. |
| fail()	| Simply fails the test |
| assertSame()	| Assert that expected and actual refer to the same object. |
|assertNotSame() 	| Assert that expected and actual do not refer to the same object. |
| assertTrue() |	asserts that actual is true. |
| assertFalse()	| asserts that actual is false. |
|assertEquals()	| Assert that expected and actual are equal. |
|assertNotEquals() |	Assert that expected and actual are not equal. |
|assertArrayEquals()	 |Assert that expected and actual arrays are equal. |
|assertIterableEquals()	| Asserts that expected and actual iterables are deeply equal |
|assertThrows()	| Assert if an executable throws the specified exception type. |
|assertAll()| 	Assert multiple assertions in groups. |
|assertTimeout() |	Assert that the execution of a supplied Executable ends before a given timeout |
|assertTimeoutPreemptively()	| Assert that the execution of the Executable will be preemptively aborted if the timeout is exceeded. |














