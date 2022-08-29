import java.io.*;
import java.util.*;

import static java.lang.Integer.*;

public class Main {

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int node = parseInt(st.nextToken());
        int link = parseInt(st.nextToken());
        List<List<Integer>> network = makeNetwork(node, link);
        boolean[] visited = new boolean[node + 1];
        int count = 0;
        for (int i = 1; i < node + 1; i++) {
            if (!visited[i]) {
                dfs(i, visited, network);
                count++;
            }
        }
        System.out.println(count);
    }

    private static List<List<Integer>> makeNetwork(int node, int link) throws IOException {
        List<List<Integer>> network = new ArrayList<>();
        for (int i = 0; i < node + 1; i++) {
            network.add(new ArrayList<>());
        }
        for (int i = 0; i < link; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int a = parseInt(st2.nextToken());
            int b = parseInt(st2.nextToken());
            network.get(a).add(b);
            network.get(b).add(a);
        }
        return network;
    }

    private static void dfs(int currentNode, boolean[] visited, List<List<Integer>> network) {
        visited[currentNode] = true;
        for (int linkedNode : network.get(currentNode)) {
            if (!visited[linkedNode]) {
                dfs(linkedNode, visited, network);
            }
        }
    }
}
