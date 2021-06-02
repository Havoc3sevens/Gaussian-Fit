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

using namespace std;

int main(void)
{
    double x, y;
    string fi, line;
    vector <double> xv, yv;
    int n;
    cout.precision(16);

    fi = "test.txt";
    ifstream Imputfile(fi);
    n = -1;
    while (!Imputfile.eof()) {
        Imputfile >> x >> y;
        xv.push_back(x);
        yv.push_back(y);
        n += 1;
    }
    xv.resize(n);
    yv.resize(n);
    double xa[n], ya[n];
    copy(xv.begin(), xv.end(),xa); //x vector, xv, to x array, xa
    copy(yv.begin(), yv.end(),ya); //y vector, yv, to y array, ya

    /*double xy[n][2];
    for (int i = 0; i < n; i++) {
        xy[i][0] = xa[i];
        xy[i][1] = ya[i];
    }*/

    for (int i = 0; i < n; i++) {
        cout << xa[i] << ' ' << ya[i] << ' ' << i << endl;
    }

}