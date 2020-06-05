// Learning C++... a bit
#include <iostream>
#include <vector>
#include <string>

using namespace std;

template <class myType>
myType getArray () {
    return 
}

int main () {
    vector <string> msg {"Hello", "C++", "World", "from",
"VS Code", "and the C++ extension"};

    for (const string& word: msg)   {
        cout << word << " ";
    }
    cout << endl;
}