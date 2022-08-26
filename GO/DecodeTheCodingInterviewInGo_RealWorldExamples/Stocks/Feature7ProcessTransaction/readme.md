## Description

In a stock trading company, several transactions are performed every day. All these transactions are recorded in a log file. The lines in the log file may start with a positive or negative integer that will represent the profit or loss on the transaction, followed by textual details about the transaction. There may be leading whitespace in the line.

Our task is to process one line of the log file and return the integer at the beginning of the line, while ignoring the whitespace until the first non-whitespace character is found. After this, we should check for an optional initial + or - sign followed by as many numerical digits as possible. If the first token on the line is not an integer, we will return 0.


## Solution

The problem is relatively simple, but we need to consider a few edge cases that were observed from the examples above. They are as follows:

* Ignore all the leading whitespaces.

* Check if a + or - is the first non-whitespace character on the line.

* Read the digits till the next non-digit character appears or the line ends.

* We need to avoid integer overflow by checking if the integer is within the 32-bit signed integer range, [-2^{31}
2 
31
 
, 2^{31}
2 
31
 
 - 1]. If the integer is out of this range, then we will return either of these limits, depending on the integer sign.



