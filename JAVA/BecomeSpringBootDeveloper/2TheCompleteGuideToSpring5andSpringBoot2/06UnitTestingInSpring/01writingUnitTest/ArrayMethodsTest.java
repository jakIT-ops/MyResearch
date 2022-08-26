package io.datajek.unittesting;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class ArrayMethodsTest {

	@Test
	public void testfindIndex_numberInArray() {
		//1. create object of the class
	    ArrayMethods arrayMethods = new ArrayMethods();
	    //2. call method
	    int result = arrayMethods.findIndex(new int[]{8,4,5}, 4);
	    //3. compare the actual results to the expected
	    assertEquals(1, result);
	}

	@Test
	public void testfindIndex_numberNotInArray() {
		ArrayMethods arrayMethods = new ArrayMethods();
	    assertEquals(-1, arrayMethods.findIndex(new int[]{8,4,5}, 1));
	}

	@Test
	public void testfindIndex_emptyArray() {
	    ArrayMethods arrayMethods = new ArrayMethods();
	    assertEquals(-1, arrayMethods.findIndex(new int[]{}, 1));
	}	
}
