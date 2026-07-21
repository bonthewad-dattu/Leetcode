/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
        let first = 0;
    let second = 1;

    for(let i = 1; i <= n; i++){

        let third = first + second;

        first = second;
        second = third;
    }

    return first;
};