import java.util.Arrays;

public class graph {
	

	public static int solution(int n, int[][] results) {

		int OVER_POINT = 10000;
        int[][] rankingBoard = new int[n][n];
        int[] flag = new int[n];

       
        for(int i=0;i<n;i++) {
            for(int j=0;j<n;j++) {
                rankingBoard[i][j] = (i==j)? 0 : OVER_POINT;
            }
        }

      
        for(int[] result: results) {
            rankingBoard[result[0]-1][result[1]-1] = 1;
        }

       
        for(int k=0; k<n;k++) {
            for(int i=0;i<n;i++) {
                for(int j=0;j<n;j++) {
                    rankingBoard[i][j] = Math.min(rankingBoard[i][j], rankingBoard[i][k] + rankingBoard[k][j]);
                }
            }
        }

     
        for(int i=0;i<n;i++) {
            for(int j=0;j<n;j++) {
                if(rankingBoard[i][j]==OVER_POINT && rankingBoard[j][i]==OVER_POINT) {
                    flag[i] = 1;
                    break;
                }
            }
        }

        return (int)Arrays.stream(flag).filter(val->val==0).count();
	}

}
