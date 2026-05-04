class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int add;
            int carry;
            add = a ^ b;
            carry = (a & b) << 1;
            a = add;
            b = carry;
            }
        return a;
    }
}
