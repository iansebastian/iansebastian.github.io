// June 6th 2020, 10:52 PM. I copied this from https://www.programmingwithbasics.com/2018/03/day-21-generics-hackerrank-solution-c.html
// because I am too impatient and have too little time to properly re-learn the basics
// of C++ up to that level right now. But of course, imitation is the sincerest form of flattery, and I thank you, 
// kind stranger of the internet putting this up on your website. It's a good idea tho lmao
// And of course as always, it's not like I cut corners on this one, it's just the fundamental, structural ideas
// So...in that sense, I think that sooner or later, I will eventually get to this level, and do the exact same thing, that is,
// learning by imitation and hands-on coding, which is -- yes, I think the best and really the only way to really learn and get started to code.

#include <iostream>
#include <string>
#include <vector>

using namespace std;

template <class T>
    void printArray (vector<T> i) {
        for (int j = 0; j < i.size(); ++j) {
            cout << i[j] << endl;
        }
    }

int main() {
    int n;

    cin >> n;
    vector<int> int_vector(n);
    for (int i = 0; i < n; i++) {
        int value;
        cin >> value;
        int_vector[i] = value;
    }

    cin >> n;
    vector<string> string_vector(n);
    for (int i = 0; i < n; i++) {
        string value;
        cin >> value;
        string_vector[i] = value;
    }

    printArray<int>(int_vector);
    printArray<string>(string_vector);
}