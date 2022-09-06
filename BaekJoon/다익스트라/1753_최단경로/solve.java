import java.io.*;
import java.util.*;

import static java.lang.Integer.*;

public class Main3 {

    private static int[] distance;
    private static ArrayList[] adjacentList;

    static class Node implements Comparable<Node> {

        int end;
        int weight;

        public Node(int end, int weight) {
            this.end = end;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o) {
            return weight - o.weight;
        }
    }

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        final int numberOfV = parseInt(st.nextToken());
        final int numberOfEdge = parseInt(st.nextToken());
        final int startV = parseInt(br.readLine());

        makeDistanceINF(numberOfV);
        makeAdjacentList(br, numberOfV, numberOfEdge);
        dijkstra(startV, numberOfV);
        print(numberOfV);
        br.close();
    }

    private static void print(int numberOfV) {
        final StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= numberOfV; i++) {
            if (distance[i] == MAX_VALUE) {
                sb.append("INF\n");
                continue;
            }
            sb.append(distance[i] + "\n");
        }
        System.out.println(sb);
    }

    private static void dijkstra(int start, int numberOfV) {
        final PriorityQueue<Node> priorityQueue = new PriorityQueue<>();
        final boolean[] visited = new boolean[numberOfV + 1];
        distance[start] = 0;
        priorityQueue.add(new Node(start, 0));
        while (!priorityQueue.isEmpty()) {
            final Node currentNode = priorityQueue.poll();
            if (visited[currentNode.end]) {
                continue;
            }
            visited[currentNode.end] = true;
            search(priorityQueue, currentNode);
        }
    }

    private static void search(PriorityQueue<Node> priorityQueue, Node currentNode) {
        int length = adjacentList[currentNode.end].size();
        for (int i = 0; i < length; i++) {
            Node nextNode = (Node) adjacentList[currentNode.end].get(i);
            final int nextWeight = currentNode.weight + nextNode.weight;
            if (distance[nextNode.end] > nextWeight) {
                distance[nextNode.end] = nextWeight;
                priorityQueue.add(new Node(nextNode.end, distance[nextNode.end]));
            }
        }
    }

    private static void makeAdjacentList(BufferedReader br, int numberOfV, int numberOfEdge) throws IOException {
        StringTokenizer st;
        adjacentList = new ArrayList[numberOfV + 1];
        for (int i = 1; i <= numberOfV; i++) {
            adjacentList[i] = new ArrayList<>();
        }
        for (int i = 0; i < numberOfEdge; i++) {
            st = new StringTokenizer(br.readLine());
            final int start = parseInt(st.nextToken());
            final int end = parseInt(st.nextToken());
            final int weight = parseInt(st.nextToken());
            adjacentList[start].add(new Node(end, weight));
        }
    }

    private static void makeDistanceINF(int v) {
        distance = new int[v + 1];
        for (int i = 1; i <= v; i++) {
            distance[i] = MAX_VALUE;
        }
    }
}
