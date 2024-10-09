#include <iostream>
using namespace std;

bool isEven(int number) {
    return number % 2 == 0;
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