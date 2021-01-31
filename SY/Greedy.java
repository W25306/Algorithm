import java.util.Arrays;
import java.util.Comparator;
public class Greedy {//Ä«¸Þ¶ó


	public static int solution(int[][] routes) {
		int answer = 1;

        Comparator<int[]> c1 = (a,b)->{
            return a[0]-b[0];
        };

        Arrays.sort(routes, c1);
        int end = routes[0][1];

        for(int i=1; i<routes.length; i++){
            if( end > routes[i][1]){
                end = routes[i][1];
            }
            if(end < routes[i][0]){
                answer++;
                end = routes[i][1];
            }
        }
        return answer;
	}
}
