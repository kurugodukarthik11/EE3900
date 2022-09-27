#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <complex.h>

complex *fft(int n, complex *a) {
    if (n == 1) return a;
    complex *f = (complex *)malloc(n/2*sizeof(complex));
    complex *g = (complex *)malloc(n/2*sizeof(complex));
    for (int i = 0; i < n; i++)
    {
        if (i%2==1)
        {
            g[i/2] = a[i];
        }
        else
        {
            f[i/2] = a[i];
        }
    }
    f = fft(n/2, f);
    g = fft(n/2, g);
    for (int i = 0; i < n; i++)
    {
        a[i] = f[i%(n/2)] + cexp(-I*2*M_PI*i/n)*g[i%(n/2)];
    }
    free(f);
    free(g);
    return a;
}

int main() {
    int n = 8;
    complex *a = (complex *)malloc(sizeof(complex)*n);
    // a={1,2,3,4,2,1,0,0};
    a[0] = 1.0, a[1] = 2.0, a[2] = 3.0, a[3] = 4.0, a[4] = 2.0, a[5] = 1.0, a[6] = 0.0, a[7] = 0.0;
    a = fft(n, a);
    for (int i = 0; i < n; i++)
    {
        printf("X(%d) = %lf + %lfj\n", i, creal(a[i]), cimag(a[i]));
    }
    free(a);
    return 0;
}