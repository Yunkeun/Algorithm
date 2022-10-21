import java.io.*;
import java.util.*;

import static java.lang.Integer.*;

public class Main {

    private static List<List<Integer>> graph;

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        final int n = parseInt(st.nextToken());
        final int m = parseInt(st.nextToken());
        setGraph(br, n, m);
        int max = 0;
        final List<Integer> counts = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            final boolean[] visited = new boolean[n + 1];
            final int count = dfs(i, visited, 0);
            counts.add(count);
            if (max < count) {
                max = count;
            }
        }
        for (int i = 0; i < counts.size(); i++) {
            if (counts.get(i) == max) {
                System.out.print(i + 1 + " ");
            }
        }
    }

    private static int dfs(int x, boolean[] visited, int count) {
        visited[x] = true;
        for (int adjacentNode : graph.get(x)) {
            if (!visited[adjacentNode]) {
                count = dfs(adjacentNode, visited, count + 1);
            }
        }
        return count;
    }

    private static int bfs(int x, boolean[] visited) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(x);
        visited[x] = true;
        int count = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int adjacentNode : graph.get(node)) {
                if (!visited[adjacentNode]) {
                    queue.add(adjacentNode);
                    visited[adjacentNode] = true;
                    count++;
                }
            }
        }
        return count;
    }

    private static void setGraph(BufferedReader br, int n, int m) throws IOException {
        StringTokenizer st;
        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            final int node1 = parseInt(st.nextToken());
            final int node2 = parseInt(st.nextToken());
            graph.get(node2).add(node1);
        }
    }
}
