#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <vector>
#include <string>

using namespace std;

struct Has23 {
    bool has2;
    bool has3;
};

const struct Has23 count_appear(const char *s) {
    int d[26];

    for (int i = 0; i < 26; i++)
        d[i] = 0;

    for (int i = 0; i < strlen(s); i++) {
        d[s[i]-'a']++;
    }

    struct Has23 has23 = {false, false};
    for (int i = 0; i < 26; i++) {
        if (d[i] == 2)
            has23.has2 = true;
        else if (d[i] == 3)
            has23.has3 = true;
    }

    return has23;
}

void letters_in_common(const string s, const string t, char *res) {
    int j = 0;
    for (int i = 0; i < s.length(); i++)
        if (s[i] == t[i])
            res[j++] = s[i];
    
    res[j] = '\0';
}

int main(int argc, char *argv[]) {
    const unsigned long MAX_LEN = 1024;
    FILE *fp;
    if ((fp = fopen(argv[1], "r")) == NULL) {
        perror(argv[1]);
        exit(1);
    }

    char line[MAX_LEN+1];
    int num2 = 0;
    int num3 = 0;
    vector<string> ids;
    while (fgets(line, MAX_LEN, fp) != NULL) {
        line[strlen(line)-1] = '\0'; // strip trailine newline
        const struct Has23 has23 = count_appear(line);
        ids.push_back(line);
        
        if (has23.has2)
            num2++;
        if (has23.has3)
            num3++;
    }

    printf("checksum = %d\n", num2 * num3);

    int target_len = ids[0].length() - 1;
    char res[target_len + 1];
    for (int i = 0; i < ids.size() - 1; i++)
        for (int j = i+1; j < ids.size(); j++) {
            letters_in_common(ids[i], ids[j], res);
            if (strlen(res) == target_len)
                puts(res);
        }
    
    return 0;
}
