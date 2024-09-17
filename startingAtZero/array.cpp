//Nicholas Norman
//Array.cpp
//16 Sep 2024

#include <iostream>

int main() {
    int arr[] = {5,6,7,8,9,10,11};

    //Keep in mind that arr is an address
    // * means: the value at <address>
    std::cout << *(arr + 0) << std::endl;
    std::cout << *(arr + 1) << std::endl;
    std::cout << *(arr + 2) << std::endl;
    std::cout << *(arr + 3) << std::endl;
    std::cout << *(arr + 4) << std::endl;
    
    for (int i = 0; i < sizeof(arr) / 4; i++) {
        std::cout << "Address: " << arr + i << " Value: " << *(arr + i) << std::endl;
    }

    return 0;
}

/* An Example Output

5
6
7
8
9
Address: 0x7ffcf46caf90 Value: 5
Address: 0x7ffcf46caf94 Value: 6
Address: 0x7ffcf46caf98 Value: 7
Address: 0x7ffcf46caf9c Value: 8
Address: 0x7ffcf46cafa0 Value: 9
Address: 0x7ffcf46cafa4 Value: 10
Address: 0x7ffcf46cafa8 Value: 11

*/
