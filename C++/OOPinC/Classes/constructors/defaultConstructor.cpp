#include <iostream>
#include <string>

using namespace std;

class Date {

	int day;
	int month;
	int year;

	public:
	// Default constructor
	Date(){
		// We must define the default values for day, month, and year
		day = 0;
		month = 0;
		year = 0;
	}

	// A simple print function
	void printDate(){
		cout << "Date: " << day << "/" << month << "/" << year << endl;
	}
};

int main() {
	// Call the Date constructor to create its object;
	
	Date d; // Object created with default values!
	d.printDate();
}
