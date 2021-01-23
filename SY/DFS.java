
public class solution {
	
	private static final int[] mx = {-1, 1, 0, 0};
    private static final int[] my = {0, 0, 1, -1};
    private static boolean[][] visited;
    private static int[][] picture;
    private static int yLimit;
    private static int xLimit;

    public int[] solution(int m, int n, int[][] input) {
        int numberOfArea = 0;
        int maxSize = 0;
        visited = new boolean[m][n];
        picture = input;
        yLimit = m;
        xLimit = n;

        for(int y = 0 ; y < m ; ++y) {
            for(int x = 0 ; x < n ; ++x) {
                if(picture[y][x] != 0 && !visited[y][x]) {
                    numberOfArea++;
                    maxSize = Math.max(maxSize, DFS(y, x));
                }
            }
        }

        return new int[] {numberOfArea, maxSize};
    }

    private static int DFS(int y, int x) {
        visited[y][x] = true;
        int areaSize = 1;

        for(int i = 0 ; i < mx.length ; ++i) {
            int nx = x + mx[i];
            int ny = y + my[i];

            if(nx < 0 || ny < 0 || nx == xLimit || ny == yLimit || visited[ny][nx] ||
                    picture[y][x] != picture[ny][nx])
                continue;

            areaSize += DFS(ny, nx);
        }


        return areaSize;
    }
	
}


