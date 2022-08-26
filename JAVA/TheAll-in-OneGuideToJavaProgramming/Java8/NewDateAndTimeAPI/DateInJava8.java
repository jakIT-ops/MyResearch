import java.time.*;
import java.time.format.DateTimeFormatter;
import java.time.Duration;
import java.time.temporal.ChronoUnit;

public class Date {

	public static void main(String[] args)
	{
		LocalTime now = LocalTime.now();
		System.out.println("Current time: "+ now);
		
		LocalTime later = now.plus(8, ChronoUnit.HOURS);
		System.out.println("After 8 hours: "+ later);
	
	}
}


