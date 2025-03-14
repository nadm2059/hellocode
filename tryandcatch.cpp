#include <iostream>
using namespace std;

int main() {
    try {
        int num1, num2;
        cout << "Enter two numbers: ";
        cin >> num1 >> num2;
        
        if (num2 == 0) {
            throw "Division by zero is not allowed!";
        }

        cout << "Result: " << (num1 / num2) << endl;
    }
    catch (const char* errorMsg) {
        cout << "Error: " << errorMsg << endl;
    }

    cout << "Program continues after exception handling..." << endl;
    return 0;
}

