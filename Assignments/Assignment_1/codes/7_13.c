#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include <time.h>

#define dc double complex

dc *fft(dc *signal, int N);
dc *ifft(dc *X, int N);
dc *convolution(dc *a, int n, dc *b, int m);
dc cexp(double complex z);

dc *fft(dc *signal, int N) {
    if (N == 1) {
        return signal;
    }
    dc *f1 = malloc(N/2 * sizeof(*f1));
    dc *f2 = malloc(N/2 * sizeof(*f2));
    for (int i = 0; i < N/2; i++) {
        f1[i] = signal[2*i];
        f2[i] = signal[2*i + 1];
    }
    dc *F1 = fft(f1, N/2);
    dc *F2 = fft(f2, N/2);
    dc *X = malloc(N * sizeof(*X));
    for (int i = 0; i < N/2; i++) {
        X[i] = 	F1[i] + cexp(-2 * I * M_PI * i / N) * F2[i];
        X[i + N/2] = F1[i] - cexp(-2 * I * M_PI * i / N) * F2[i];
    }
    return X;
}

dc *ifft(dc *X, int N) {

    if (N == 1)
    {
        return X;
    }

    dc *F1 = malloc(N/2 * sizeof(*F1));
    dc *F2 = malloc(N/2 * sizeof(*F2));

    for (int i = 0; i < N/2; i++)
    {
        F1[i] = X[2*i];
        F2[i] = X[2*i + 1];
    }

    dc *f1 = fft(F1, N/2);
    dc *f2 = fft(F2, N/2);

    dc *x = malloc(N * sizeof(*x));

    for (int i = 0; i < N/2; i++)
    {
        x[i] = 	0.5 * (f1[i] + cexp(2 * I * M_PI * i / N) * f2[i]);
        x[i + N/2] = 0.5 * (f1[i] - cexp(2 * I * M_PI * i / N) * f2[i]);
    }

    return x;
}

dc *convolution(dc *x, int nx, dc *h, int nh)
{
    int ny = nx + nh - 1;
    dc *y = malloc(ny * sizeof(*y));

    for (int n = 0; n < ny; n++)
    {
        for (int k = 0; k < nx; k++)
        {
            if (n - k >= 0 && n - k < nh)
            {
                y[n] = x[k] * h[n-k];
            }
        }
    }

    return y;
}

int main()
{
    srand(time(0));

    FILE *fft_time = fopen("fft_time.txt", "w");
    FILE *conv_time = fopen("conv_time.txt", "w");

    for(double n = 3; n < 25000; n *= 2)
    {
        dc *x = malloc(n * sizeof(*x));
        dc *h = malloc(n * sizeof(*h));

        for(int i = 0; i < n; i++)
        {
            x[i] = rand();
            h[i] = rand();
        }

        clock_t fft_start = clock();

        dc *X = fft(x, n);
        dc *H = fft(h, n);
        dc *Y = malloc(n * sizeof(*Y));

        for(int i = 0; i < n; i++)
        {
            Y[i] = X[i] * H[i];
        }

        dc *y = ifft(Y, n);

        clock_t fft_end = clock();
        fprintf(fft_time, "%lf\n", (double)(fft_end - fft_start) / CLOCKS_PER_SEC);

        clock_t conv_start = clock();
        dc *y2 = convolution(x, n, h, n);
        clock_t conv_end = clock();

        fprintf(conv_time, "%lf\n", (double)(conv_end - conv_start) / CLOCKS_PER_SEC);
    }

    fclose(fft_time);
    fclose(conv_time);
    return 0;
}
