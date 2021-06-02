/*
This program will be used to wrap test the code in native CPP
    Created by: Enrique Hurtado
    Date: 12 January 2021
    Latest update: 12 January 2021
    History:
        Date: 01/12/21 || Mod: Program written || By: Enrique Hurtado
    Purpose: This will be what the user interacts with
        Specification: should be able to work with PY and CPP-DLLs
    Notes:
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <array>

using namespace std;

struct Arr {
    double arr[2];
    vector <double> vec;
    double function(){
        arr[0] = 3.0290;
        arr[1] = -9.02789;
        vec.push_back(arr[0]);
        vec.push_back(arr[1]);
    }
};

//struct Arr function()
//{
//    Arr x;
//
//    x.arr[0] = 3.0290;
//    x.arr[1] = -9.02789;
//
//    return x;
//    
//}



int main(void)
{
    string fi;
    cout.precision(16);

    Arr array;
    array.function();

    cout << array.vec[0] << endl;

}