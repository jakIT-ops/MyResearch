package io.educative.junit5;

import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

public class DisabledMethodTest {
	
    @Test
    void testOnDevelopmentEnvironment() {
        System.setProperty("ENV", "DEV");
        assertTrue("DEV".equals(System.getProperty("ENV")));
    }
    
    @Disabled("Skip in upper environments")
    @Test
    void testOnProductionEnvironment() {
        System.setProperty("ENV", "PROD");
        assertTrue("PROD".equals(System.getProperty("ENV")));
    }
}
