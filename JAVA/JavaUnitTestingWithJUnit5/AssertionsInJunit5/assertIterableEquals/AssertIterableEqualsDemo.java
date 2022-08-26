package io.educative.junit5;

import static org.junit.jupiter.api.Assertions.assertIterableEquals;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.jupiter.api.Test;

public class AssertIterableEqualsDemo {

	@Test
	public void testAssertIterableEqualsForEqualIterables() {
		  Iterable<Integer> expected = new ArrayList<>(Arrays.asList(1,2,3,4));
	    Iterable<Integer> actual = new ArrayList<>(Arrays.asList(1,2,3,4));
	    assertIterableEquals(expected, actual);
	}
	
	@Test
	public void testAssertIterableEqualsForNotEqualIterables() {
		  Iterable<Integer> expected = new ArrayList<>(Arrays.asList(1,2,3,4));
	    Iterable<Integer> actual = new ArrayList<>(Arrays.asList(1,2,3));
	    assertIterableEquals(expected, actual, "Iterables are not equal.");
	}
	
	@Test
	public void testAssertIterableEqualsForEqualIterablesWithDifferentOrder() {
		  Iterable<Integer> expected = new ArrayList<>(Arrays.asList(1,2,3,4));
	    Iterable<Integer> actual = new ArrayList<>(Arrays.asList(1,2,4,3));
	    assertIterableEquals(expected, actual, () -> "Iterables order is different");
	}
}
