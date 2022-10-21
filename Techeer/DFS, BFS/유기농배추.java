import java.io.*;
import java.util.*;

import static java.lang.Integer.*;

public class Main {

    private static int[][] graph;
    private static boolean[][] visited;
    private static final int[] dx = {1, -1, 0, 0};
    private static final int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int numberOfTests = parseInt(br.readLine());
        for (int i = 0; i < numberOfTests; i++) {
            final int numberOfWorms = getNumberOfWorms(br);
            System.out.println(numberOfWorms);
        }
    }

    private static int getNumberOfWorms(BufferedReader br) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        final int row = parseInt(st.nextToken());
        final int column = parseInt(st.nextToken());
        setGraph(br, st, row, column);
        int count = 0;
        visited = new boolean[row][column];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                if (graph[i][j] == 1 && !visited[i][j]) {
                    dfs(i, j);
                    count++;
                }
            }
        }
        return count;
    }

    private static void dfs(int x, int y) {
        visited[x][y] = true;
        for (int i = 0; i < 4; i++) {
            final int nx = x + dx[i];
            final int ny = y + dy[i];
            if (0 <= nx && nx < graph.length && 0 <= ny && ny < graph[0].length) {
                if (graph[nx][ny] == 1 && !visited[nx][ny]) {
                    dfs(nx, ny);
                }
            }
        }
    }

    private static void setGraph(BufferedReader br, StringTokenizer st, int row, int column) throws IOException {
        graph = new int[row][column];
        final int numberOfCabbages = parseInt(st.nextToken());
        for (int j = 0; j < numberOfCabbages; j++) {
            st = new StringTokenizer(br.readLine());
            final int r = parseInt(st.nextToken());
            final int c = parseInt(st.nextToken());
            graph[r][c] = 1;
        }
    }
}
