import java.io.*;
import java.util.*;

import static java.lang.Integer.*;

public class Main {

    private static List<List<Integer>> graph;
    private static boolean[] visited;

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int numberOfComputers = parseInt(br.readLine());
        final int numberOfLinks = parseInt(br.readLine());
        setGraph(br, numberOfComputers, numberOfLinks);
        visited = new boolean[numberOfComputers + 1];
        final int count = dfs(1, 0);
        System.out.println(count);
    }

    private static int dfs(int x, int count) {
        visited[x] = true;
        for (int adjacentNode : graph.get(x)) {
            if (!visited[adjacentNode]) {
                count = dfs(adjacentNode, count + 1);
            }
        }
        return count;
    }

    private static void setGraph(BufferedReader br, int numberOfComputers, int numberOfLinks) throws IOException {
        graph = new ArrayList<>();
        for (int i = 0; i <= numberOfComputers; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < numberOfLinks; i++) {
            final StringTokenizer st = new StringTokenizer(br.readLine());
            final int node1 = parseInt(st.nextToken());
            final int node2 = parseInt(st.nextToken());
            graph.get(node1).add(node2);
            graph.get(node2).add(node1);
        }
    }
}
