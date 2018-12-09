#include <stdio.h>
#include <stdlib.h>
#include <list>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
    int num_players = atoi(argv[1]);
    int num_marbles = atoi(argv[2]);
    unsigned long long *score = new unsigned long long[num_players];
    list<int> circle;
    circle.push_back(0);
    auto idx = circle.begin();
    int player = 0;

    for (int i = 0; i < num_players; i++)
        score[i] = 0;
    
    for (int marble = 1; marble <= num_marbles; marble++) {
        if (marble % 23 == 0) {
            for (int i = 0; i < 6; i++)
                if (--idx == circle.begin())
                    idx = circle.end();
            idx--;
            score[player] += (marble + *idx);
            idx = circle.erase(idx);
        } else {
            if (++idx == circle.end())
                idx = circle.begin();
            idx++;
            idx = circle.insert(idx, marble);
        }
        player = (player + 1) % num_players;

        // for (auto idx2 : circle)
        //     printf("%d ", idx2);
        // printf("\n");
    }

    printf("part1: %llu\n", *max_element(score, score+num_players));
}
