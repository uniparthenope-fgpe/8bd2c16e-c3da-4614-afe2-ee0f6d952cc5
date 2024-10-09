#include <iostream>
using namespace std;

bool isEven(int number) {
    // There is a bug in this logic
    return number % 2 == 1;
}

int main() {
    int num = 4;
    if (isEven(num)) {
        cout << 'Even';
    } else {
        cout << 'Odd';
    }
    return 0;
}