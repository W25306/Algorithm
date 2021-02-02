import java.util.Arrays;
import java.util.Comparator;


public class Dynamic {
    int answer = -1;
    public int solution(int N, int number) {


        dfs(N, number, 0, 0);


        return answer;
    }

    public void dfs(int N, int number, int num, int cnt) {
        int tempN = N;

        if(cnt > 8) {
            answer = -1;
            return;
        }        
        if(num == number) {
            if(answer == -1 || answer > cnt)
                answer = cnt;
            return;
        }

        for(int i = 0; i < 8 - cnt; i++) {
            dfs(N, number, num - tempN, cnt + 1 + i);
            dfs(N, number, num + tempN, cnt + 1 + i);
            dfs(N, number, num * tempN, cnt + 1 + i);
            dfs(N, number, num / tempN, cnt + 1 + i);
            tempN = increase(tempN, N);
        }
    }
    public int increase(int tempN, int N) {
        return (tempN * 10) + N;
    }
}


