## Introduction to date and time API

Java 8 introduces a new Date/Time API that is thread-safe, easier to read, and more comprehensive than the previous API. Java’s calendar implementation has not changed much since it was first introduced, and Joda-Time is widely regarded as a better replacement. Java 8’s new Date/Time API is very similar to Joda-Time.

## New classes

The main difference is that there are several different classes to represent date, time, time period, and timezone specific data. Also, there are transformers for dates and times.

For dates and times without a timezone, use the following:

* LocalDate: Day, month, and year.

* LocalTime: Time of day only

* LocalDateTime: Both date and time

For timezone specific times, use ZonedDateTime.






