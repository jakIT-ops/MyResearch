package ClassAndObjects;


//Square Sum
public class SquareSum {

	// Method to square the sum of three numbers
	double squareSum(double num1, double num2, double num3) {
		 double sum = 0;

		 num1 = num1 * num1;
		 num2 = num2 * num2;
		 num3 = num3 * num3;
		 sum = num1 + num2 + num3;

		 return sum;
	}

}
