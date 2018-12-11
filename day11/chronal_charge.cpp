#include <stdio.h>
#include <stdlib.h>
#include "array2d.h"

inline const int hundreds_digit(const int n) {
    return (n/100) % 10;
}

inline const int power_level(const int x, const int y, const int serial) {
    const int rack_id = x+10;
    int level = rack_id * y;
    level += serial;
    level *= rack_id;
    return hundreds_digit(level) - 5;
}

inline const int sum_square(array2d<int> &grid, const int xoff, const int yoff, const int dim) {
    int sum = 0;
    for (int x = xoff; x < xoff+dim; x++)
        for (int y = yoff; y < yoff+dim; y++)
            sum += grid(x, y);

    return sum;
}

int main(int argc, char *argv[]) {
    int serial = atoi(argv[1]);
    const int DIM = 300;
    array2d<int> grid(DIM, DIM);

    for (int x = 0; x < DIM; x++)
        for (int y = 0; y < DIM; y++)
            grid(x, y) = power_level(x, y, serial);
            
    int best_sum = -1e6;
    int best_x = -1;
    int best_y = -1;

    for (int x = 0; x < DIM-2; x++) {
        for (int y = 0; y < DIM-2; y++) {
            int power = sum_square(grid, x, y, 3);
            if (power > best_sum) {
                best_sum = power;
                best_x = x;
                best_y = y;
            }
        }
    }
    printf("part 1: (%d,%d) %d\n", best_x, best_y, best_sum);

    best_sum = -1e6;
    best_x = -1;
    best_y = -1;
    int best_size = -1;
    
    for (int size = 1; size <= DIM; size++) {
        if (size % 10 == 0)
            printf("size = %d\n", size);
        for (int x = 0; x < DIM-(size-1); x++) {
            for (int y = 0; y < DIM-(size-1); y++) {
                int power = sum_square(grid, x, y, size);
                if (power > best_sum) {
                    best_sum = power;
                    best_x = x;
                    best_y = y;
                    best_size = size;
                }
            }
        }
    }
    printf("part 2: (%d,%d, %d) %d\n", best_x, best_y, best_size, best_sum);
}
