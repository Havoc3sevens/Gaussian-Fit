#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(void)
{
    int n = 5;
    int nn;
    double xi[n+1][n];
    double params[ ] = {0.0, 0.09, 1.0, 0.00038, 0.00004};
    cout.precision(16);
    //cout << n << " " << nn << endl;
    for (int i=0; i<n; i++) {
        xi[0][i] = params[i];
        //cout << xi[1][i] << " " << i << endl;
    }

    for (int j = 0; j < n+1; j++) {
        for (int i=0; i<n; i++) {
            //cout << xi[j][i] << " " << i << endl;
        }
    }

    for (double val: params) {
        cout << val << endl;
    }
}