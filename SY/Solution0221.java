import java.util.PriorityQueue;

public class Solution0221 {
	
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> queue = new PriorityQueue<Integer>();
        for(int s : scoville) {
        	queue.add(s);
        }
        Integer a = queue.poll();
        Integer b = queue.poll();
        while(b != null&& a < K) {
        	queue.add(mix(a,b));
        	answer++;
        	a = queue.poll();
            b = queue.poll();
        }
        if(b == null && a < K) {
        	return -1;
        }
        return answer;
    }
    
    private int mix(int a, int b) {
    	return a + (2*b);
    }
}


