import java.util.*;
public class Calendardate {
    public static void main(String args[])
    {
        Calendar cal = Calendar.getInstance();
        System.out.println("Current time: " + cal.getTime());
        cal.add(Calendar.HOUR, 8); 
        System.out.println("After 8 hours: " + cal.getTime()); //returns a date
    }
}
