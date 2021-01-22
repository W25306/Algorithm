
import java.util.PriorityQueue;

	



class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visit = new boolean[n];
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            if (visit[i]) {
                continue;
            }

            visit[i] = true;
            pq.offer(i);

            while (!pq.isEmpty()) {
                int cur = pq.poll();
                for (int j = 0; j < n; j++) {
                    if (!visit[j] && computers[cur][j] == 1) {
                        visit[j] = true;
                        pq.offer(j);
                    }
                }
            }

            answer++;
        }

        return answer;
    }
}
