import java.io.*;
import java.util.*;

import static java.lang.Integer.*;

public class Main {

    private static List<List<Integer>> graph;
    private static boolean[] visited;

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        final int numberOfNodes = parseInt(st.nextToken());
        final int numberOfEdges = parseInt(st.nextToken());
        final int startNode = parseInt(st.nextToken());
        setGraph(br, numberOfNodes, numberOfEdges);
        visited = new boolean[numberOfNodes + 1];
        dfs(startNode);
        System.out.println();
        visited = new boolean[numberOfNodes + 1];
        bfs(startNode);
    }

    private static void dfs(int x) {
        visited[x] = true;
        System.out.print(x + " ");
        for (int adjacentNode : graph.get(x)) {
            if (!visited[adjacentNode]) {
                dfs(adjacentNode);
            }
        }
    }

    private static void bfs(int x) {
        final Queue<Integer> queue = new LinkedList<>();
        queue.add(x);
        visited[x] = true;
        while (!queue.isEmpty()) {
            final int node = queue.poll();
            System.out.print(node + " ");
            for (int adjacentNode : graph.get(node)) {
                if (!visited[adjacentNode]) {
                    queue.add(adjacentNode);
                    visited[adjacentNode] = true;
                }
            }
        }
    }

    private static void setGraph(BufferedReader br, int numberOfNodes, int numberOfEdges) throws IOException {
        StringTokenizer st;
        graph = new ArrayList<>();
        for (int i = 0; i <= numberOfNodes; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < numberOfEdges; i++) {
            st = new StringTokenizer(br.readLine());
            final int node1 = parseInt(st.nextToken());
            final int node2 = parseInt(st.nextToken());
            graph.get(node1).add(node2);
            graph.get(node2).add(node1);
            Collections.sort(graph.get(node1));
            Collections.sort(graph.get(node2));
        }
    }
}
