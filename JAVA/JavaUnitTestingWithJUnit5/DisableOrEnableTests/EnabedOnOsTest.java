package com.hubberspot.junit5.disabled;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.condition.EnabledOnOs;
import org.junit.jupiter.api.condition.OS;

public class EnabledOnOsTest {
	
    @Test
    void testOnAllOs() {
        assertTrue(3 > 0);
    }
    
    @EnabledOnOs(OS.WINDOWS)
    @Test
    void testEnabledOnWindowsOs() {
    	assertFalse(0 > 4);
    }
    
    @EnabledOnOs(OS.MAC)
    @Test
    void testEnabledOnMacOs() {
    	assertFalse(10 > 40);
    }
}

