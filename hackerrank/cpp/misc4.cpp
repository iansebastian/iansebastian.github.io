#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main () {
    bool flag;
    flag = true;
    if (flag) {
        cout << "It's true! For boolean values, I do not have to explicitly compare it with true or false bool values.";
    }
    else {
        cout << "You lied to me!";
    }
}