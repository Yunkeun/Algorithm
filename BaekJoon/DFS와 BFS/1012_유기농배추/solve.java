import java.io.*;
import java.util.*;

import static java.lang.Integer.*;

public class Main {

    private static int[][] graph;
    private static boolean[][] visited;
    private static int row;
    private static int column;
    private static final int[] dx = {1, -1, 0, 0};
    private static final int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int numberOfTestCase = parseInt(br.readLine());
        for (int i = 0; i < numberOfTestCase; i++) {
            final int count = getCount(br);
            System.out.println(count);
        }
    }

    private static int getCount(BufferedReader br) throws IOException {
        setGraph(br);
        int count = 0;
        for (int m = 0; m < row; m++) {
            for (int n = 0; n < column; n++) {
                if (graph[m][n] == 1 && !visited[m][n]) {
                    dfs(m, n);
                    count++;
                }
            }
        }
        return count;
    }

    private static void setGraph(BufferedReader br) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        row = parseInt(st.nextToken());
        column = parseInt(st.nextToken());
        graph = new int[row][column];
        visited = new boolean[row][column];
        final int numberOfCabbage = parseInt(st.nextToken());
        for (int j = 0; j < numberOfCabbage; j++) {
            st = new StringTokenizer(br.readLine());
            final int x = parseInt(st.nextToken());
            final int y = parseInt(st.nextToken());
            graph[x][y] = 1;
        }
    }

    private static void dfs(int x, int y) {
        visited[x][y] = true;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (0 <= nx && nx < row && 0 <= ny && ny < column) {
                if (graph[nx][ny] == 1 && !visited[nx][ny]) {
                    dfs(nx, ny);
                }
            }
        }
    }
}
