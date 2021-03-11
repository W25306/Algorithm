
public class Solution0311 {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] a = { { 2, 2 } };
		System.out.println(solution3(4, 3, a));
	}

	public static int solution3(int m, int n, int[][] puddles) {

		int[][] table = new int[n][m];
		int insert = 1;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				table[i][j] = -1;
			}
		}
		for(int i = 0; i< puddles.length; i++) {
			table[puddles[i][1]-1][puddles[i][0]-1] = 0;
		}
		
		
		for(int i = 0; i < m; i++) {
			if(table[0][i] == 0) {
				insert = 0;
			}
			table[0][i] = insert;
		}
		
		insert = 1;
		for(int i = 0; i < n; i++) {
			if(table[i][0] == 0) {
				insert = 0;
			}
			table[i][0] = insert;
		}
		
		
		for (int i = 1; i < n; i++) {
			for (int j = 1; j < m; j++) {
				if(table[i][j] == -1)
				table[i][j] = table[i-1][j]%1000000007 + table[i][j-1]%1000000007;
			}
		}
		
		return table[n-1][m-1]%1000000007;
	}

}
