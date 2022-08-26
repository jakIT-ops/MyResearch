#include <iostream>
#include <utility>

// Driver code 
int main() 
{ 
	std::string str1 = "abcd";
	std::string str2 = "efgh";
	std::cout << "str1: " << str1 << std::endl;
	std::cout << "str2: " << str2 << "\n\n";

	// Copying
	str2 = str1;             // copy semantic
	std::cout << "After copying" << std::endl;
	std::cout << "str1: " << str1 << std::endl;
	std::cout << "str2: " << str2 << "\n\n";

	str1 = "abcd";
	str2 = "efgh";

	// Moving
	str2 = std::move(str1);
	std::cout << "After moving" << std::endl;
	std::cout << "str1: " << str1 << std::endl;
	std::cout << "str2: " << str2 << "\n\n";
} 
