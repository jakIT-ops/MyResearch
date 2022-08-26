package com.hubberspot.junit5.disabled;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.condition.EnabledIfEnvironmentVariable;

public class EnabledIfEnvironmentVariableTest {
	
    @Test
    void testOnAllEnvironmentVariables() {
        assertTrue(3 > 0);
    }
    
    @EnabledIfEnvironmentVariable(named="USER", matches="dinesh")
    @Test
    void testEnabledIfUserMatchesDinesh() {
    	assertFalse(0 > 4);
    }
    
    @EnabledIfEnvironmentVariable(named="HOME", matches="/dummies/home")
    @Test
    void testEnabledIfHomeMatchesDummyDirectory() {
    	assertFalse(10 > 40);
    }
}

