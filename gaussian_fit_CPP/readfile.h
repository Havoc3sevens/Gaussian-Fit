/*
This header file contains a structure used to read in a text file
    Created by: Enrique Hurtado
    Date: 13 January 2021
    Latest update: 13 January 2021
    History:
        Date: 01/13/21 || Mod: Program written || By: Enrique Hurtado
    Purpose: Create two arrays of data and pass to a main routine
        Specification: X, Y data preferred.
    Notes:
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct Readfile
{
    vector <double> xv, yv;
    int n;
    void xy_file(string fi) {
        /*
            Function: xy_file
            Created by: Enrique Hurtado
            Date: 13 January 2021
            Description: Creates two arrays of data from a text file.
            
            Variables
            xv: Left most column of data
            yv: Right most column of data
            n:  number of line in text file
        */
        double x, y;
        string line;
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

        Imputfile.close();
    }
};