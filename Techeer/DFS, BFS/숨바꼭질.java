import java.io.*;
import java.util.*;

import static java.lang.Integer.*;

public class Main {

    private static int[] graph = new int[100001];

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final StringTokenizer st = new StringTokenizer(br.readLine());
        final int n = parseInt(st.nextToken());
        final int k = parseInt(st.nextToken());
        bfs(n, k);
    }

    private static void bfs(int n, int k) {
        final Queue<Integer> queue = new LinkedList<>();
        queue.add(n);
        while (!queue.isEmpty()) {
            final int x = queue.poll();
            if (x == k) {
                System.out.println(graph[k]);
                return;
            }
            int[] moves = {x + 1, x - 1, x * 2};
            for (int move : moves) {
                if (0 <= move && move < 100001) {
                    if (graph[move] == 0) {
                        graph[move] = graph[x] + 1;
                        queue.add(move);
                    }
                }
            }
        }
    }
}
