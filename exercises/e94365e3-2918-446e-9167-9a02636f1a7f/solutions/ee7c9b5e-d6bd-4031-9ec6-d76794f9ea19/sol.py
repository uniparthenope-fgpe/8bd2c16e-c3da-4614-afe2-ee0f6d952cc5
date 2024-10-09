#include <iostream>
using namespace std;

class Starship {
    string name;
    int shieldStrength;
public:
    Starship(string n, int s) : name(n), shieldStrength(s) {}
    void displayStatus() {
        cout << 'Starship: ' << name << ', Shield Strength: ' << shieldStrength << endl;
    }
};

int main() {
    Starship falcon('Millennium Falcon', 100);
    falcon.displayStatus();
    return 0;
}