#include <iostream>
#include <string>
using namespace std;

void sortSithNames(string names[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (names[j] > names[j + 1]) {
                swap(names[j], names[j + 1]);
            }
        }
    }
}

int main() {
    string siths[] = {'Darth Vader', 'Darth Maul', 'Darth Sidious'};
    sortSithNames(siths, 3);
    for (int i = 0; i < 3; i++) {
        cout << siths[i] << endl;
    }
    return 0;
}