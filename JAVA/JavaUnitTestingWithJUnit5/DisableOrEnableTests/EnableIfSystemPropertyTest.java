package com.hubberspot.junit5.disabled;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.condition.EnabledIfSystemProperty;

public class EnabledIfSystemPropertyTest {
	
    @Test
    void testOnAllSystemProperties() {
        assertTrue(3 > 0);
    }
    
    @EnabledIfSystemProperty(named="user.name", matches="dinesh")
    @Test
    void testEnabledIfUserNameMatchesDinesh() {
    	assertFalse(0 > 4);
    }
    
    @EnabledIfSystemProperty(named="os.name", matches="Windows")
    @Test
    void testEnabledIfOperatingSystemMatchesWindows() {
    	assertFalse(10 > 40);
    }
}

