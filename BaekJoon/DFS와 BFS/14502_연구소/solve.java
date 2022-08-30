import java.io.*;
import java.util.*;

import static java.lang.Integer.*;

public class Main {
    // 벽을 3개 세운다 (모든 경우의수) => dfs
    // 벽 3개 세우면 다시 graph에서 2(바이러스)인 곳을 시작으로 상하좌우로 움직이며 0이면 2로 만든다.
    // 2번 과정이 끝나면 0의 개수를 센 후 이 값들 중 max값을 구한다.
    private static int[][] graph;
    private static int n, m;
    private static int[] dx = {1, -1, 0, 0};
    private static int[] dy = {0, 0, 1, -1};
    private static int maxCount = 0;

    static class Node {
        int x;
        int y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = parseInt(st.nextToken());
        m = parseInt(st.nextToken());
        graph = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = parseInt(st.nextToken());
            }
        }
        makeWall(0);
        System.out.println(maxCount);
    }

    private static void makeWall(int count) {
        if (count == 3) {
            spreadVirus();
            return;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 0) {
                    graph[i][j] = 1;
                    makeWall(count + 1);
                    graph[i][j] = 0;
                }
            }
        }
    }

    private static void spreadVirus() {
        final Queue<Node> queue = new LinkedList<>();
        final int[][] copyGraph = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 2) {
                    queue.add(new Node(i, j));
                }
                copyGraph[i][j] = graph[i][j];
            }
        }
        while (!queue.isEmpty()) {
            final Node currentNode = queue.poll();
            for (int i = 0; i < 4; i++) {
                final int nx = currentNode.x + dx[i];
                final int ny = currentNode.y + dy[i];
                if ((0 <= nx && nx < n) && (0 <= ny && ny < m)) {
                    if (copyGraph[nx][ny] == 0) {
                        copyGraph[nx][ny] = 2;
                        queue.add(new Node(nx, ny));
                    }
                }
            }
        }
        countSafeArea(copyGraph);
    }

    private static void countSafeArea(int[][] copyGraph) {
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (copyGraph[i][j] == 0) {
                    count++;
                }
            }
        }
        if (count > maxCount) {
            maxCount = count;
        }
    }
}
