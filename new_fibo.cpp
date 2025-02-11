#include <iostream>

void fibonacci_iterative(int n) {
    int a = 0, b = 1, next;
    
    std::cout << "Fibonacci Sequence (Iterative): ";
    for (int i = 0; i < n; i++) {
        std::cout << a << " ";
        next = a + b;
        a = b;
        b = next;
    }
    std::cout << std::endl;
}

int main() {
    int n;
    std::cout << "Enter the number of terms: ";
    std::cin >> n;

    if (n <= 0) {
        std::cout << "Please enter a positive integer." << std::endl;
    } else {
        fibonacci_iterative(n);
    }

    return 0;
}
