import java.io.*;
import java.util.*;

import static java.lang.Integer.*;

public class Main {

    static class Node implements Comparable<Node> {
        int end;
        int cost;

        public Node(int end, int cost) {
            this.end = end;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node node) {
            return cost - node.cost;
        }
    }

    private static int startCity, endCity;
    private static int numberOfCities, numberOfBuses;
    private static List<Node>[] adjacentNodes;
    private static int[] distances;

    public static void main(String[] args) throws IOException {
        getInput();
        setDistancesMax(numberOfCities);
        dijkstra();
        System.out.println(distances[endCity]);
    }

    private static void dijkstra() {
        PriorityQueue<Node> priorityQueue = new PriorityQueue<>();
        priorityQueue.add(new Node(startCity, 0));
        distances[startCity] = 0;
        boolean[] visited = new boolean[numberOfCities + 1];
        while (!priorityQueue.isEmpty()) {
            final Node currentNode = priorityQueue.poll();
            if (currentNode.end == endCity) {
                return;
            }
            if (!visited[currentNode.end]) {
                visited[currentNode.end] = true;
                search(priorityQueue, currentNode);
            }
        }
    }

    private static void search(PriorityQueue<Node> priorityQueue, Node currentNode) {
        for (Node adjacentNode : adjacentNodes[currentNode.end]) {
            final int totalCost = currentNode.cost + adjacentNode.cost;
            if (distances[adjacentNode.end] > totalCost) {
                distances[adjacentNode.end] = totalCost;
                priorityQueue.add(new Node(adjacentNode.end, totalCost));
            }
        }
    }

    private static void getInput() throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        numberOfCities = parseInt(br.readLine());
        numberOfBuses = parseInt(br.readLine());
        setAdjacentNodes(br);
        StringTokenizer st = new StringTokenizer(br.readLine());
        startCity = parseInt(st.nextToken());
        endCity = parseInt(st.nextToken());
    }

    private static void setAdjacentNodes(BufferedReader br) throws IOException {
        adjacentNodes = new List[numberOfCities + 1];
        for (int i = 1; i <= numberOfCities; i++) {
            adjacentNodes[i] = new ArrayList<>();
        }
        for (int i = 0; i < numberOfBuses; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            final int start = parseInt(st.nextToken());
            final int end = parseInt(st.nextToken());
            final int cost = parseInt(st.nextToken());
            adjacentNodes[start].add(new Node(end, cost));
        }
    }

    private static void setDistancesMax(int numberOfCities) {
        distances = new int[numberOfCities + 1];
        for (int i = 1; i <= numberOfCities; i++) {
            distances[i] = MAX_VALUE;
        }
    }
}
