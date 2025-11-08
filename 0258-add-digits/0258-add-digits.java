class Solution {
    public int addDigits(int num) {
        if (num == 0) return 0; // If the number is 0, the result is 0.  Base case.
        else if (num % 9 != 0) return num % 9; // If the number isn't divisible by 9, the result is the remainder when divided by 9. 
        else return 9; // If the number is divisible by 9 (and not 0), the result is 9. 
    }
}