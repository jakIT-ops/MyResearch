package io.educative.junit5;

import static org.junit.jupiter.api.Assertions.*;

import java.util.function.Supplier;
import org.junit.jupiter.api.Test;

class StringUtilsTest1 {

	// ******** assertEquals Example - Start **********
	
	@Test
	void givenEmptyString_whenReverseIsCalled_thenEmptyStringIsReturned() {
		String actual = StringUtils.reverse((""));
		String expected = "";
		
		// assertEquals without message
		assertEquals(expected, actual);
	}
	
	@Test
	void givenNonNullString_whenReverseIsCalled_thenReversedStringIsReturned() {
		String actual = StringUtils.reverse(("ABCD"));
		String expected = "DBCA";
		
		String message = "assertEquals failed";
		// assertEquals with message
		assertEquals(expected, actual, message);
	}
	
	@Test
	void givenNonNullString_whenReverseIsCalled_thenReversedStringIsReturned2() {
		String actual = StringUtils.reverse(("1234"));
		String expected = "2314";
		
		Supplier<String> messageSupplier = () -> "assertEquals failed";
		// assertEquals with Java 8 Supplier<String>
		assertEquals(expected, actual, messageSupplier);
	}
	
	// ******** assertEquals Example - End **********
}
