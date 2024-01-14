/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
    let substr = [];
    let l = 0;
    for (let i = 0; i < s.length; i++) {
        if (substr.includes(s[i]))
            substr.splice(0, substr.indexOf(s[i]) + 1);

        substr.push(s[i]);
        if (substr.length > l)
            l = substr.length;
    }
    return l;
};