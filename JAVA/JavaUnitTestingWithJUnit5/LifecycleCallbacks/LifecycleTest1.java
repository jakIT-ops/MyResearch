package io.educative.junit5;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class LifecycleTest {
	
	@BeforeAll
	public static void beforeAll() {
		System.out.println("LifecycleTest - beforeAll() got executed !!!");
	}
	
	public LifecycleTest() {
		System.out.println("LifecycleTest - Constructor got executed !!!");
	}
	
	@BeforeEach
	public void beforeEach() {
		System.out.println("LifecycleTest - beforeEach() got executed !!!");
	}
	
	@Test
	public void testOne() {
		System.out.println("LifecycleTest - testOne() got executed !!!");
	}
	
	@Test
	public void testTwo() {
		System.out.println("LifecycleTest - testTwo() got executed !!!");
	}
	
	@AfterEach
	public void afterEach() {
		System.out.println("LifecycleTest - afterEach() got executed !!!");
	}
	
	@AfterAll
	public static void afterAll() {
		System.out.println("LifecycleTest - afterAll() got executed !!!");
	}

}
