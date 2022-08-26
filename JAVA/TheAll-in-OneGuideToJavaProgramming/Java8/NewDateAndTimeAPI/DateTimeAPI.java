import java.time.*;
import java.time.format.DateTimeFormatter;
import java.time.Duration;
import java.time.temporal.ChronoUnit;

public class Date {

	public static void main(String[] args)
	{
		// current date
		LocalDate date = LocalDate.now();
		System.out.println("The current date is "+ date);

		//  current time
		LocalTime now = LocalTime.now();
		System.out.println("Current time: "+ now);

		// later time
		LocalTime later = now.plus(8, ChronoUnit.HOURS);
		System.out.println("Later time: "+ later);

		// current day
		LocalDate today = LocalDate.now();
		System.out.println("Today: "+ today);

		// 30 days later
		LocalDate thirtyDaysFromNow = today.plusDays(30);
		System.out.println("Thirty days from now: "+ thirtyDaysFromNow);

		// next month
		LocalDate nextMonth = today.plusMonths(1);
		System.out.println("Next month: "+ nextMonth);

		// last month
		LocalDate aMonthAgo = today.minusMonths(1);
		System.out.println("Last month: "+ aMonthAgo);
	
	}
}


