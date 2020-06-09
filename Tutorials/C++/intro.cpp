#include <iostream>

namespace hello {
	float in;
}

int square(float n) {
	return n*n;
}

int main() {
	std::cout << "Hello World\n";
	std::cout << "Enter a number...\n";
	std::cin >> hello::in;
	std::cout << "The square of the number is " << square(hello::in) << "\n";
	return (0);
}

