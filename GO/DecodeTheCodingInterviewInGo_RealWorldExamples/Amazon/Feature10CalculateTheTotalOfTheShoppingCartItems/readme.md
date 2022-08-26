## Description

Suppose that a customer has purchased some items online. Their shopping cart is ready for billing, and we need to calculate the total bill.

While calculating the bill, we need to consider that the customer may have purchased more than one unit of the same item. In this case, the unit price must be multiplied by the quantity. We must also consider that they may be eligible for certain discounts. Some discounts are applied as an absolute amount—for example, a $5 discount on every purchase of a 30-inch TV. Some discounts are applied as a fraction—for example, the price of a can of Coca-Cola is divided by 2 for a 50% discount.

The shopping cart is provided to us in the form of an arithmetic expression involving whole numbers and the operators +, -, *, and /. The expression is in the form of a string. We need to calculate the total cost of the items listed in the shopping cart as an integer. The rules of operator precedence in arithmetic apply here.

Let’s demonstrate this with an example. Suppose that a customer bought an item for $2, another item for $3 with a discount of 1/7 off, and that they are eligible for $1 off their total bill because they are a loyalty club member. The string input for this calculation would be: “2 + 3 / 7 - 1”.


## Solution

We know that there can be four types of operations in a given data—addition (+), subtraction (-), multiplication (*), and division (/). As per operator precedence in arithmetic, when there is no parenthesis present, multiplication (*) and division (/) will always have higher precedence than addition (+) and subtraction (-).

We can make the following observations after looking at the examples given above and while evaluating the expressions from left to right:

* If the current operator is an addition (+) or subtraction (-), the expression is evaluated based on the precedence of the next operator.

* If the current operator is multiplication (*) or division (/), the expression gets evaluated without looking into the next operator. Multiplication (*) and division (/) will be evaluated first, because they have the highest precedence among the set of operators (+, -, /, *) in our example.

Using this, let’s look at the algorithm that is used to implement the solution to the problem.







