class Solution {
    
    private static boolean[][] visited;
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (computers[i][j] == 1 && !visited[i][j]) {
                    dfs(i, j, n, computers);
                    answer++;
                }
            }
        }
        return answer;
    }
    
    private void dfs(int x, int y, int n, int[][] computers) {
        visited[x][y] = true;
        for (int i = 0; i < n; i++) {
            if (computers[y][i] == 1 & !visited[y][i]) {
                dfs(y, i, n, computers);
            }
        }
    }
}
