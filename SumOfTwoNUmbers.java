class Solution {
    public int getSum(int a, int b) {
        while(b != 0){   // we XOR and & the bits till the carry is 0
            int temp = (a & b) << 1;   //to calculate the carry, we logical and a and b and left shift it by 1 so that next bit gets the carry
            a = a ^ b;   // XOR returns the 1 for different bits and 0 for same bits
            b = temp;  // we used a temp variable since a is getting updated in the previous step
         }
        return a;

    }
}
