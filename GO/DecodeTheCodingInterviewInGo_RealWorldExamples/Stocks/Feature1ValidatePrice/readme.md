## Description

Stocks are being bought and sold every second in a trading company. It becomes common for new hires or interns with little experience to make mistakes while entering purchase or sale prices. The company has defined the fixed criteria for the purchasing and selling of stocks on its platform. In the trading section, if a price is entered with + sign, it means buy the stocks worth that amount. If a price is entered with - sign, it means sell the currently selected stock worth that amount. If no sign is entered with the price, that entry should be disregarded. Since stocks are traded in different currencies and we know that all currencies are not equal in value, prices can be fractional as well.

We’ll be provided with an input price in the form of a string. We have to validate this input so it can be either accepted or rejected. Some examples are mentioned below for reference:

+40.325 is a valid price.
-1.1.1 is NOT a valid price.
-222 is a valid price.
++22 is NOT a valid price.
10.1 is NOT a valid price.
+22.22 is a valid price.
100. is NOT a valid price.

## Solution

We’ll use the state machine below to check if a price is valid or not. The initial state is START. We’ll process each character to identify the next state. The input string is not a valid price if we reach an UNKNOWN state at any point or if it ends in a DECIMAL point.



