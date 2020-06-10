#include <iostream>

bool begins( char string1[], char string2[]) {
	/*
		Check if string 1 overlaps the beginning of string 2.
		Returns true if string 1 is completely contained in string 2 starting from the first char.

		args:
			string1, string2 : Strings in C format: char array
	*/
	for (int i = 0; string1[i] != '\0'; ++i) {
		if (string2[i] == '\0') {
			return false;
		} else if (string1[i] != string2[i]) {
			return false;
		}
	}
	return true;
}

namespace hello {
	float in;
}

inline int square(float n) {
	return n*n;
}

int main() {
	char string1[4]; strcpy(string1, "Thi\0"); 
	char string2[5]; strcpy(string2, "This\0");
	char string3[4]; strcpy(string3, "thi\0");
	std::cout << "'This' begins with 'Thi': " << begins(string1, string2) << "\n";
	std::cout << "'This' begins with 'thi': " << begins(string3, string2) << "\n\n";


	std::cout << "Hello World\n";
	std::cout << "Enter a number...\n";
	std::cin >> hello::in;
	std::cout << "The square of the number is " << square(hello::in) << "\n";
	return (0);
}