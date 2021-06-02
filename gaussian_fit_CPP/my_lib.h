/*
This header file contains a structure used as the downhill method
    Created by: Enrique Hurtado
    Date: 14 January 2021
    Latest update: 14 January 2021
    History:
        Date: 01/14/21 || Mod: Program written || By: Enrique Hurtado
    Purpose: Pass vectors back to main routine
        Specification:
    Notes:
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "setup.h"

using namespace std;
void dwnhll(double (*func)(double *param)) {
    double params[ ] = {0.0, 0.09, 1.0, 0.0004, 0.00005};
    func(params);
}

struct Datafit
{
    vector <double> paramsout;
    double ff;
    void downhill(double (*func)(double *param), 
    double param[], double fstart, int stepi, 
    int epsf, int itmin, int iter) {
        double xi[n+1][n];
    }

};
