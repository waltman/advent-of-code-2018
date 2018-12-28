#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <map>
#include <string>
#include "util.h"

using namespace std;
const int NUM_REGS=6;
bool DEBUG = false;

struct Cmd {
    int op;
    int a;
    int b;
    int c;
};

void do_inst(const int op, long int *regs, const int a, const int b, const int c) {
    switch (op) {
    case 0:
        regs[c] = regs[a] + regs[b]; break;
    case 1:
        regs[c] = regs[a] + b; break;
    case 2:
        regs[c] = regs[a] * regs[b]; break;
    case 3:
        regs[c] = regs[a] * b; break;
    case 4:
        regs[c] = regs[a] & regs[b]; break;
    case 5:
        regs[c] = regs[a] & b; break;
    case 6:
        regs[c] = regs[a] | regs[b]; break;
    case 7:
        regs[c] = regs[a] | b; break;
    case 8:
        regs[c] = regs[a]; break;
    case 9:
        regs[c] = a; break;
    case 10:
        regs[c] = (a > regs[b]) ? 1 : 0; break;
    case 11:
        regs[c] = (regs[a] > b) ? 1 : 0; break;
    case 12:
        regs[c] = (regs[a] > regs[b]) ? 1 : 0; break;
    case 13:
        regs[c] = (a == regs[b]) ? 1 : 0; break;
    case 14:
        regs[c] = (regs[a] == b) ? 1 : 0; break;
    case 15:
        regs[c] = (regs[a] == regs[b]) ? 1 : 0; break;
    }
}

int main(int argc, char *argv[]) {
    map<string, int> opcode;
    opcode["addr"] = 0;
    opcode["addi"] = 1;
    opcode["mulr"] = 2;
    opcode["muli"] = 3;
    opcode["banr"] = 4;
    opcode["bani"] = 5;
    opcode["borr"] = 6;
    opcode["bori"] = 7;
    opcode["setr"] = 8;
    opcode["seti"] = 9;
    opcode["gtir"] = 10;
    opcode["gtri"] = 11;
    opcode["gtrr"] = 12;
    opcode["eqir"] = 13;
    opcode["eqri"] = 14;
    opcode["eqrr"] = 15;

    FILE *fp;
    if ((fp = fopen(argv[1], "r")) == NULL)
        die("error opening %s", argv[1]);

    const int MAX_LEN = 80;
    char line[MAX_LEN];
    vector<string> pgms;
    int ipr = -1;
    vector<struct Cmd> pgm;
    while (fgets(line, MAX_LEN, fp) != NULL) {
        line[strlen(line)-1] = '\0';
        if (line[0] == '#')
            ipr = line[4] - '0';
        else {
            pgms.push_back(line);
            vector<string> v = vec_split(line, ' ');
            struct Cmd cmd;
            cmd.op = opcode[v[0]];
            cmd.a = atoi(v[1].c_str());
            cmd.b = atoi(v[2].c_str());
            cmd.c = atoi(v[3].c_str());
            pgm.push_back(cmd);
        }            
    }
    // run the program
    int ip = 0;
    long int regs[] = {1, 0, 0, 0, 0, 0};
    // int ip = 3;
    // long int regs[] = {1,10551330,10551340,3,1,0};
//    long int regs[] = {1,5275650,10551340,3,2,0};
//    long int regs[] = {10551341,10551300,10551340,3,10551340,0};
    unsigned long int n = 0;
    while (ip >= 0 && ip < (int) pgm.size()) {
        struct Cmd cmd = pgm[ip];
        regs[ipr] = ip;
//        printf("ip=%2d [%ld,%ld,%ld,%ld,%ld,%ld]\t%s", ip, regs[0],regs[1],regs[2],regs[3],regs[4],regs[5], pgms[ip].c_str());
        do_inst(cmd.op, regs, cmd.a, cmd.b, cmd.c);
//        printf("\t[%ld,%ld,%ld,%ld,%ld,%ld]\n", regs[0],regs[1],regs[2],regs[3],regs[4],regs[5]);
        ip = regs[ipr] + 1;
        n++;
        if (n % 100000000 == 0)
            printf("n=%lu ip=%2d [%ld,%ld,%ld,%ld,%ld,%ld]\t%s\n", n, ip, regs[0],regs[1],regs[2],regs[3],regs[4],regs[5], pgms[ip].c_str());
    }
    printf("part1: %ld\n", regs[0]);
    long int sum = 0;
    long int val = 10551340;
    for (long int i = 1; i <= val; i++) {
        if (val % i == 0) {
            sum += i;
            printf("i = %ld, sum = %ld\n", i, sum);
        }
    }
    printf("part2: %ld\n", sum);
                
}
