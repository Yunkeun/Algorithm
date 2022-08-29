
import java.io.*;
import java.util.*;

import static java.lang.Integer.*;

public class Main {

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final int[] dx = {1, -1, 0, 0};
    private static final int[] dy = {0, 0, 1, -1};
    private static int row;
    private static int col;

    public static void main(String[] args) throws IOException {
        int numberOfTests = parseInt(br.readLine());
        for (int i = 0; i < numberOfTests; i++) {
            int minimumNumberOfWorm = test();
            System.out.println(minimumNumberOfWorm);
        }
    }

    private static int test() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        row = parseInt(st.nextToken());
        col = parseInt(st.nextToken());
        int numberOfCabbage = parseInt(st.nextToken());
        int[][] field = new int[row][col];
        for (int i = 0; i < numberOfCabbage; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int x = parseInt(st2.nextToken());
            int y = parseInt(st2.nextToken());
            field[x][y] = 1;
        }
        int count = 0;
        boolean[][] visited = new boolean[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (field[i][j] == 1 && !visited[i][j]) {
                    dfs(i, j, visited, field);
                    count++;
                }
            }
        }
        return count;
    }

    private static void dfs(int x, int y, boolean[][] visited, int[][] field) {
        visited[x][y] = true;
        for (int i = 0; i < dx.length; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (0 <= nx && nx < row && 0 <= ny && ny < col) {
                if (field[nx][ny] == 1 && !visited[nx][ny]) {
                    dfs(nx, ny, visited, field);
                }
            }
        }
    }
}