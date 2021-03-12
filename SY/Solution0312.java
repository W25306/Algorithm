import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Solution0312 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] a = {{0,3}, {1,9}, {2,6}};
		System.out.println(solution(a));
	}

	public static int solution(int[][] jobs) {
		
		ArrayList<int[]> list = new ArrayList<>();
		for(int i = 0; i<jobs.length; i++) {
			list.add(jobs[i]);
		}
		
		Collections.sort(list, new Comparator<int[]>() {
		
			@Override
			public int compare(int[] a, int[] b) {
				
				//�ҿ�ð� ���� ��.
				if(a[0] < b[0]) {
					return -1;
				}
				else if(a[0] == b[0]){
					if(a[1] < b[1]) {
						return -1;
					}else if(a[1] == b[1]) {
						return 0;
					}else {
						return 1;
					}
				}
				else {
				//a[0] > b[0]
					return 1;
				}
			
			}
		});
		
		int result = 0;
		int task_complete = 1;
		
		int[] current = list.get(0);
		list.remove(0);
		int current_time = current[0] + current[1];
		result += current[1];
		
		while(task_complete != jobs.length) {
			
			int min = 2147483647; // ���� �۾��� ����Ǵ� ���� ��û�� �۾��� ������� �״�� 
			int min_index = -1;
			for(int i = 0; i <=current_time; i++) {
				for(int j = 0; j < list.size(); j++) {
					//�ð����� �ּڰ� �ϳ�����.
					if(i == list.get(j)[0]) {
						if(list.get(j)[1]  < min) {
							min_index= j;
							min = list.get(j)[1];
						}
						break;
					}
					else if( i < list.get(j)[0]) {
						break;
					}
				}
			}
			//���� �۾� ����. (current_time�� ������.)
			//��û�� ������ ���� ��� �ٷ� �����ϰ� ����ð� ����.
			
			if(min == 2147483647) {
				current_time = list.get(0)[0] + list.get(0)[1];
				result += list.get(0)[1];
				System.out.println("result ++ "+ list.get(0)[1]);
				list.remove(0);
			}
			else {
				
				result += current_time - list.get(min_index)[0] + list.get(min_index)[1] ;
				current_time +=  list.get(min_index)[1];
				list.remove(min_index);

				}
			System.out.println("current_time : "
					+ "" + current_time);
			task_complete ++;
			
			
			
			
			
			
		}
		
		
		
		
		
		
		
		
		return result/task_complete;
	}

}
