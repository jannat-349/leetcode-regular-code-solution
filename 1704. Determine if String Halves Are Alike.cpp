class Solution {
public:
    bool halvesAreAlike(string s) {
        int x = 0;
        int y = 0;
        int j = s.length() - 1;
        for (int i = 0; i < j; i++) {
            if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' ||
                s[i] == 'u' || s[i] == 'A' || s[i] == 'E' || s[i] == 'I' ||
                s[i] == 'O' || s[i] == 'U') {
                x++;
            }

            if (s[j] == 'a' || s[j] == 'e' || s[j] == 'i' || s[j] == 'o' ||
                s[j] == 'u' || s[j] == 'A' || s[j] == 'E' || s[j] == 'I' ||
                s[j] == 'O' || s[j] == 'U') {
                y++;
            }
            j--;
        }
        if(x==y){
            return true;
        }
        else return false;
    }
};
