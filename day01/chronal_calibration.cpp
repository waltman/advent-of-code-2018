#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <set>

using namespace std;

const unsigned long MAX_LEN = 1024;
int main(int argc, char *argv[]) {
        FILE *fp;
        if ((fp = fopen(argv[1], "r")) == NULL) {
                perror(argv[1]);
                exit(1);
        }

        int freq = 0;
        vector<int> deltas;
        char line[MAX_LEN+1];
        while (fgets(line, MAX_LEN, fp) != NULL) {
                int val = atoi(line);
                freq += val;
                deltas.push_back(val);
        }

        printf("resulting frequency = %d\n", freq);

        set<int> seen;
        freq = 0;
        int i = 0;
        while (1) {
                freq += deltas[i];
                if (seen.find(freq) != seen.end()) {
                        printf("%d is first seen twice\n", freq);
                        break;
                }
                seen.insert(freq);
                i = (i + 1) % deltas.size();
        }
}
