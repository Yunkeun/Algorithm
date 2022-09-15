import java.io.*;

import static java.lang.Integer.*;

public class Main3 {

    private static int n;
    private static boolean[][] visited;
    private static String[][] originalGraph;
    private static String[][] weaknessGraph;
    private static int[] dx = {1, -1, 0, 0};
    private static int[] dy = {0, 0, 1, -1};
    private static String[] colorList = {"R", "G", "B"};

    public static void main(String[] args) throws IOException {
        getInput();
        visited = new boolean[n][n];
        int sum = countColors(originalGraph, visited);
        System.out.println(sum);
        visited = new boolean[n][n];
        sum = countColors(weaknessGraph, visited);
        System.out.println(sum);
    }

    private static int countColors(String[][] graph, boolean[][] visited) {
        int[] colorCount = new int[3];
        for (int c = 0; c < 3; c++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (graph[i][j].equals(colorList[c]) && !visited[i][j]) {
                        dfs(i, j, graph);
                        colorCount[c]++;
                    }
                }
            }
        }
        return countSum(colorCount);
    }
    private static int countSum(int[] colorCount) {
        int sum = 0;
        for (int c : colorCount) {
            sum += c;
        }
        return sum;
    }

    private static void dfs(int x, int y, String[][] graph) {
        visited[x][y] = true;
        final String currentColor = graph[x][y];
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if ((0 <= nx && nx < n) && (0 <= ny && ny < n)) {
                if (currentColor.equals(graph[nx][ny]) && !visited[nx][ny]) {
                    dfs(nx, ny, graph);
                }
            }
        }
    }

    private static void getInput() throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = parseInt(br.readLine());
        setGraph(br);
    }

    private static void setGraph(BufferedReader br) throws IOException {
        originalGraph = new String[n][n];
        weaknessGraph = new String[n][n];
        for (int i = 0; i < n; i++) {
            final String st = br.readLine();
            final String[] colors = st.split("");
            originalGraph[i] = new String[n];
            weaknessGraph[i] = new String[n];
            for (int j = 0; j < n; j++) {
                originalGraph[i][j] = colors[j];
                setWeaknessGraph(i, j, colors[j]);
            }
        }
    }

    private static void setWeaknessGraph(int i, int j, String color) {
        if (color.equals("G")) {
            weaknessGraph[i][j] = "R";
            return;
        }
        weaknessGraph[i][j] = color;
    }
}
