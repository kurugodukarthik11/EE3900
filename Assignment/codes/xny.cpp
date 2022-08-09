#include <bits/stdc++.h>

using namespace std;

#include <fstream>

using std::ofstream;


int main() {
    double x[6] = {1.0, 2.0, 3.0, 4.0, 2.0, 1.0};
    int n_size = 20;
    double y[n_size];
    for (int i = 0; i < n_size; i++)
        y[i] = 0;
    y[0] = x[0];
    y[1] = -0.5 * y[0] + x[1];
    for (int i = 2; i < n_size - 1; i++) {
        if (i < 6)
            y[i] = -0.5 * y[i - 1] + x[i] + x[i - 2];
        else if (i > 5 and i < 8)
            y[i] = -0.5 * y[i - 1] + x[i - 2];
        else
            y[i] = -0.5 * y[i - 1];
    }
    ofstream outdata;
    outdata.open("E:\\cliin\\abc.dat");
    for (double i: x) {
        outdata << i << " ";
    }
    outdata << endl;
    for (double i: y) {
        outdata << i << " ";
    }
    outdata.close();
    return 0;
}
