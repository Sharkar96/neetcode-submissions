class Solution {
public:
    int getSum(int a, int b) {
        while(b != 0){
            auto tmp = (a & b) << 1;
            a = a ^ b;
            b = tmp;
        }
        return a;
    }
};
