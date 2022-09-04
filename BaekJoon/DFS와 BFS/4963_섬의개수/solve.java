import java.io.*;
import java.util.*;

import static java.lang.Integer.*;

public class Main3 {

    private static int[][] graph;
    private static boolean[][] visited;
    private static int w;
    private static int h;
    private static final int[] dx = {1, -1, 0, 0, 1, 1, -1, -1};
    private static final int[] dy = {0, 0, 1, -1, 1, -1, 1, -1};

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            w = parseInt(st.nextToken());
            h = parseInt(st.nextToken());
            if (w == 0 && h == 0) {
                break;
            }
            setGraph(br);
            int count = 0;
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    if (graph[i][j] == 1 && !visited[i][j]) {
                        count += dfs(i, j, 0);
                    }
                }
            }
            System.out.println(count);
        }
    }

    private static void setGraph(BufferedReader br) throws IOException {
        StringTokenizer st;
        graph = new int[h][w];
        visited = new boolean[h][w];
        for (int i = 0; i < h; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < w; j++) {
                graph[i][j] = parseInt(st.nextToken());
            }
        }
    }

    private static int dfs(int x, int y, int count) {
        visited[x][y] = true;
        count++;
        for (int i = 0; i < 8; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if ((0 <= nx && nx < h) && (0 <= ny && ny < w)) {
                if (graph[nx][ny] == 1 && !visited[nx][ny]) {
                    dfs(nx, ny, count);
                }
            }
        }
        return count;
    }
}
