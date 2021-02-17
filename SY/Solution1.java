public class Solution1 {//´ëÁøÇ¥
    public int solution(int n, int a, int b) {
        if (a > b)
            return solution(n, b, a);

        int count = 1;
        while (b % 2 == 1 || a != b - 1) {
            a = (a + 1) / 2;
            b = (b + 1) / 2;
            count++;
        }

        return count;
    }
}