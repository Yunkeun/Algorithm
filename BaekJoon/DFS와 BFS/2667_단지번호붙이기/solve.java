import java.io.*;
import java.util.*;

import static java.lang.Integer.*;

public class Main {

    private static int lengthOfMap;
    private static int[][] map;
    private static boolean[][] visited;
    private static int[] dx = {1, -1, 0, 0};
    private static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {

        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        lengthOfMap = parseInt(br.readLine());
        map = new int[lengthOfMap][lengthOfMap];
        for (int i = 0; i < lengthOfMap; i++) {
            String[] row = br.readLine().split("");
            for (int j = 0; j < lengthOfMap; j++) {
                map[i][j] = parseInt(row[j]);
            }
        }
        final List<Integer> numberOfHouses = new ArrayList<>();
        visited = new boolean[lengthOfMap][lengthOfMap];
        for (int i = 0; i < lengthOfMap; i++) {
            for (int j = 0; j < lengthOfMap; j++) {
                if (map[i][j] == 1 && !visited[i][j]) {
                    int currentCount = countHouseDfs(i, j, 0);
                    numberOfHouses.add(currentCount);
                }
            }
        }
        Collections.sort(numberOfHouses);
        System.out.println(numberOfHouses.size());
        for (Integer numberOfHouse : numberOfHouses) {
            System.out.println(numberOfHouse);
        }
    }

    private static int countHouseDfs(int x, int y, int count) {
        visited[x][y] = true;
        count++;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if ((0 <= nx && nx < lengthOfMap) && (0 <= ny && ny < lengthOfMap)) {
                if (map[nx][ny] == 1 && !visited[nx][ny]) {
                    count = countHouseDfs(nx, ny, count);
                }
            }
        }
        return count;
    }
}
