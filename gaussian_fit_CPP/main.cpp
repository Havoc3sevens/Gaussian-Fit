/*
This program will be used to wrap test the code in native CPP
    Created by: Enrique Hurtado
    Date: 12 January 2021
    Latest update: 13 January 2021
    History:
        Date: 01/12/21 || Mod: Program written || By: Enrique Hurtado
        Date: 01/13/21 || Mod: Struct implemented || By: Enrique Hurtado
    Purpose: This will be what the user interacts with
        Specification: should be able to work with PY and CPP-DLLs
    Notes:
*/
#include <cmath>
#include "readfile.h"
#include "my_lib.h"
using namespace std;

/*------------Global Variables------------
int fl;
int n;
int minsp, maxsp;
vector <double> xv, yv;
bool fileout = false;
string filename = "result";
^^^^^^^^^^^^Global Variables^^^^^^^^^^^^*/

double chi2(double param[]) {
    double a, b, y1, x1, sig1, ss, fi, step, x;
    int n;
    cout.precision(16);

    a = param[0], b = param[1];
    y1 = param[2], x1 = param[3], sig1 = param[4];
    
    ss = 0.0;
    for (int i = minsp; i < maxsp; i++) {
        ss += ((yv[i]-fi )*(yv[i]-fi ))/sqrt(yv[i]+2.0);
    }
    ss = ss/abs(maxsp - minsp );

    if (fileout == true) {
        ofstream OutputFile(filename + ".dat");
        n = 10000;
        step = (xv[maxsp-1]-xv[minsp])/float(n);
        x = xv[minsp];

        for (int i = 0; i <= n; i++) {
            fi = a*x + b + y1*exp( -((x-x1 )/ sig1 )*((x-x1 )/ sig1 ));
            OutputFile << x << " " << fi << endl;
            x = x + step;
        }
        OutputFile.close();
    }

    return ss;
}

int main(void)
{
    string fi;
    double params[ ] = {0.0, 0.09, 1.0, 0.00038, 0.00004};
    n = sizeof(params)/sizeof(params[0]);
    //cout << n << endl;
    cout.precision(16);
    fi = "test.txt";

    Readfile file_in;
    file_in.xy_file(fi);

    /*for (int i = 0; i < file_in.n; i++) {
        cout << file_in.xv[i] << ' ' << file_in.yv[i] << ' ' << i << endl;
    }*/
    fl = file_in.n;
    /*
    double xa[n], ya[n];
    copy(file_in.xv.begin(), file_in.xv.end(),xa); //x vector, xv, to x array, xa
    copy(file_in.yv.begin(), file_in.yv.end(),ya); //y vector, yv, to y array, ya
    */
    xv = file_in.xv;
    yv = file_in.yv;

    minsp = 0;
    maxsp = fl;
    fileout = true;
    //filename = "init_guess";
    //chi2(params);
    dwnhll(chi2);

}