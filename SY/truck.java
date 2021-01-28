import java.util.Arrays;

public class truck {
	

	 public int solution(int bridge_length, int weight, int[] truck_weights) {
         int answer = 1;
         int[] list=new int[truck_weights.length];
         Arrays.fill(list,bridge_length);
         int pweight=truck_weights[0];
         for(int start=0,end=0;start<truck_weights.length&&end<truck_weights.length;answer++) {
             for(int i=start;i<=end;i++){
                 list[i]--;
             }
             if(list[start]==0){
                 if(start==truck_weights.length)
                     break;
                 pweight-=truck_weights[start++];
             }
             if(end+1<truck_weights.length&&truck_weights[end+1]+pweight<=weight){
                 pweight+=truck_weights[++end];
             }
         }
         return answer;
     }

}
