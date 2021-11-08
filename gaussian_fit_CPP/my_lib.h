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
//double * dwnhll(double (*func)(double *param), double xstart[ ], int fstart, int stepi, double epsf, int itmin, int iters, double xxi[], double &ffi) {
double * dwnhll(double (*func)(double *param), double xxi[ ], double &ffi) {
    xxi[0] = 1.;
    xxi[1] = 23.;
    xxi[2] = 42.;
    ffi = 69.420;
    return xxi;
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
