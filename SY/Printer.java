import java.util.Queue;
import java.util.LinkedList;
import java.util.Arrays;

class Priority {
    int value;
    int index;

    public Priority(int value, int index) {
        this.value = value;
        this.index = index;
    }
}

public class Printer {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Priority> queue = new LinkedList<Priority>();
        int[] order = priorities.clone();

        Arrays.sort(order);

        for(int i=0;i<priorities.length;i++) {
            queue.offer(new Priority(priorities[i],i));
        }

        int index = order.length-1;

        do {
            if(order[index] > queue.peek().value) {
                queue.offer(queue.peek());
            } else {
                index--;
                answer++;
                if(location == queue.peek().index)
                    break;
            }
            queue.poll();

        }while(!queue.isEmpty());

        return answer;
    }
}