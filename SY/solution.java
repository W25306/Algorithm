/* 2020.01.25 Stack
 * �ֽİ��� https://programmers.co.kr/learn/courses/30/lessons/42584
 * �̰� �� ������ ����� �ɱ� ����.
 */
public class solution {
	public static void main(String[] args) {
		
		int[] array = {1,2,3,2,3};
		System.out.println(solution(array)[0]);
	}
	
	
    public static int[] solution(int[] prices) {
    	
    	
    	int[] result = new int[prices.length];
    	
    	int time = 0;
    	for(int i = 0; i<prices.length; i++) {
    		for(int j = i+1; j< prices.length; j++) {
    			time++;
    			if(prices[i] > prices[j]) {
    				break;
    			}
    		}
    		result[i] = time;
    		time = 0;
    	}
    	
    	
    	
		return result;
    	
    }
       
}


