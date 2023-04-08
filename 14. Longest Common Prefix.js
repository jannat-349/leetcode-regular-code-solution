/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
  let str;
  let mn = 10000000;
  for(let i=0 ; i<strs.length; i++) {
    if(strs[i].length < mn) {
      str = strs[i];
      mn = str.length;
    }
  }
  let res = "";
  for(let i=0; i<str.length; i++){
    let f = 0;
    for(let j=0; j<strs.length; j++){
      if(strs[j][i] !== str[i]){
        f = 1;
        break;
      }
    }
    if(f === 0){
      res += str[i];
    }
    else
      break;
  }
  return res;
};