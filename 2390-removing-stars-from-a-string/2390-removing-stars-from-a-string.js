/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function(s) {

    const stack =[]
    for ( const char of s){
        if (char !== "*"){
            stack.push(char)
        }else{
            stack.pop()
        }
    }
    return stack.join('')

    
};