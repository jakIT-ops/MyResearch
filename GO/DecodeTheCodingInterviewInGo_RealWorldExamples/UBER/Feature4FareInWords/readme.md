## Description

At the end of a ride, the Uber app displays the fare to the customer. For accessibility, we want the fare to be read out, should the customer so choose. Assuming that the ride fare is an integer and that a text to speech engine is available, all we need to do is to convert the fare to English words. For example, we need to change $120 to one hundred and twenty dollars. The fare may be as high as several billion depending on the country the ride is taken in.

We’ll be provided with an integer number, fare, which represents the fare. Our task will be to convert fare to its English word representation.

## Solution

We can solve this problem by dividing the initial number into a specific set of digits and then solving those sets. Initially, we can split the number into sets of three. For example, if we split the amount 1234567890 into sets of three digits, we’ll get 1 234 567 890. Now, the values are separated into billion, million, and thousand parts in the number. At this stage, our English representation will become 1 Billion 234 Million 567 Thousand 890.

The three digits from each set can be further divided into individual sets to obtain the values at the hundreds, tens, and ones places. For example, 567 can be split into 5 6 7. After splitting, 5 6 7 will be converted to the English word representation five Hundred sixty seven. We need to consider the values from 10 to 19 separately for conversion if they are present at the ones and tens places.


