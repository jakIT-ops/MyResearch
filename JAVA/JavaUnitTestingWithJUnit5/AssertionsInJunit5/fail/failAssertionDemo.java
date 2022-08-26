package io.educative.junit5;

import static org.junit.jupiter.api.Assertions.fail;

import org.junit.jupiter.api.Test;

public class FailAssertionDemo {

	// usage 1 - @Test not implemented with fail()
	@Test
	public void testMethodYetNotImplemented() {
		fail();
	}
	
	// usage 2 - @Test not implemented with fail(String message)
	@Test
	public void testMethodYetNotImplemented1() {
		fail("@Test method not yet implemented !!!");
	}
	
	// usage 3 - @Test not implemented with fail(Supplier<String> messageSupplier)
	@Test
	public void testMethodYetNotImplemented2() {
		fail(() -> "@Test method not yet implemented !!!");
	}
	
	// usage 4 - @Test not implemented with fail(Throwable throwable)
	@Test
	public void testMethodYetNotImplemented3() {
		fail(new RuntimeException("@Test method not yet implemented !!!"));
	}
	
	// usage 5 - @Test not implemented with fail(String message, Throwable throwable)
	@Test
	public void testMethodYetNotImplemented4() {
		fail("@Test method not yet implemented !!!", new RuntimeException("Failed explicitly"));
	}
	
	// usage 6 - It can be used to verify that an actual exception is thrown
	@Test
	public void testActualExceptionThrown() {
		try {
			methodThatShouldThrowException();
			fail("Exception not thrown !!!");
		} catch (UnsupportedOperationException e) {
			// test case passed
		}
	}
	
	private void methodThatShouldThrowException() {
		throw new UnsupportedOperationException(); // uncomment this line to will fail the test case
	}
	
}
