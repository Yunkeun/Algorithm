import java.util.*;

class Solution {
    
    private static int[] dx = {1, -1, 0, 0};
    private static int[] dy = {0, 0, 1, -1};
    private static int[][] visited;
    private static int n, m;
    
    public int solution(int[][] maps) {
        n = maps.length;
        m = maps[0].length;
        visited = new int[n][m];
        bfs(maps);
        final int answer = visited[n-1][m-1];
        if (answer == 0) {
            return -1;
        }
        return answer;
    }
    
    private void bfs(int[][] maps) {
        final Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {0, 0});
        visited[0][0] = 1;
        while (!queue.isEmpty()) {
            final int[] current = queue.poll();
            final int cx = current[0];
            final int cy = current[1];
            for (int i = 0; i < 4; i++) {
                final int nx = cx + dx[i];
                final int ny = cy + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (maps[nx][ny] == 1 && visited[nx][ny] == 0) {
                        visited[nx][ny] = visited[cx][cy] + 1;
                        queue.add(new int[] {nx, ny});
                    }
                }
            }
        }
    }
}
