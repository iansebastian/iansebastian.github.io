#include <iostream>
#include <vector>
#include <string>

// Just dabbling into pointers
// https://www.geeksforgeeks.org/pointers-c-examples/

void geeks()
{
    int var = 20;

    // declare pointer variable
    int *ptr;

    // note that data type of ptr and var must be the same
    ptr = &var;

    // assign the address of a variable to a pointer
    printf("Value at ptr = %p \n", ptr);
    printf("Value at var = %d \n", var);
    printf("Value at *ptr = %d \n", *ptr);
}

// Driver program
int main () {
    geeks();
}