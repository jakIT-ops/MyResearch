package com.hubberspot.junit5.disabled;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.condition.EnabledOnJre;
import org.junit.jupiter.api.condition.JRE;

public class EnabledOnJreTest {
	
	  @Test
    void testOnAllJre() {
        assertTrue(3 > 0);
    }
    
    @EnabledOnJre(JRE.JAVA_8)
    @Test
    void testEnabledOnJava8() {
    	assertFalse(0 > 4);
    }
    
    @EnabledOnJre(JRE.JAVA_9)
    @Test
    void testEnabledOnJava9() {
    	assertFalse(10 > 40);
    }
}

