class Solution {
public:
    bool isValid(string s) {
        stack<char> s2;
        s2.push(s[0]);
        for (int i = 1; i < s.length(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                s2.push(s[i]);
            } else if (s[i] == ')') {
                if (!s2.empty()) {
                    char a = s2.top();
                    if (a == '(')
                        s2.pop();
                    else
                        s2.push(a);
                } else {
                    return false;
                }
            } else if (s[i] == ']') {
                if (!s2.empty()) {
                    char a = s2.top();
                    if (a == '[')
                        s2.pop();
                    else
                        s2.push(a);
                } else {
                    return false;
                }
            } else if (s[i] == '}') {
                if (!s2.empty()) {
                    char a = s2.top();
                    if (a == '{')
                        s2.pop();
                    else
                        s2.push(a);
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
        if (!s2.empty()) {
            return false;
        }
        return true;
    }
};
