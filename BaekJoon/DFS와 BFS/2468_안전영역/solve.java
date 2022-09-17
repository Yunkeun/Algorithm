import java.io.*;
import java.util.*;

import static java.lang.Integer.*;

public class Main {

    private static int n;
    private static int maxHeight = 0;
    private static int[][] board;
    private static boolean[][] visited;
    private static int[] dx = {1, -1, 0, 0};
    private static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        getInput();
        int currentCount;
        int max = 0;
        for (int currentHeight = 0; currentHeight < maxHeight; currentHeight++) {
            visited = new boolean[n][n];
            currentCount = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (board[i][j] > currentHeight && !visited[i][j]) {
                        dfs(i, j, currentHeight);
                        currentCount++;
                    }
                }
            }
            max = Math.max(max, currentCount);
        }
        System.out.println(max);
    }

    private static void dfs(int x, int y, int currentHeight) {
        visited[x][y] = true;
        for (int i = 0; i < 4; i++) {
            final int nx = x + dx[i];
            final int ny = y + dy[i];
            if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                if (board[nx][ny] > currentHeight && !visited[nx][ny]) {
                    dfs(nx, ny, currentHeight);
                }
            }
        }
    }

    private static void getInput() throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = parseInt(br.readLine());
        setBoard(br);
    }

    private static void setBoard(BufferedReader br) throws IOException {
        board = new int[n][n];
        for (int i = 0; i < n; i++) {
            final StringTokenizer st = new StringTokenizer(br.readLine());
            board[i] = new int[n];
            for (int j = 0; j < n; j++) {
                final int height = parseInt(st.nextToken());
                findMaxHeight(height);
                board[i][j] = height;
            }
        }
    }

    private static void findMaxHeight(int height) {
        if (height > maxHeight) {
            maxHeight = height;
        }
    }
}
