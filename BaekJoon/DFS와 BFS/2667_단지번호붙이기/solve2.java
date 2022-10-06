package com.simplecrud;

import java.io.*;
import java.util.*;

import static java.lang.Integer.*;

public class Main {

    private static int length;
    private static int[][] graph;
    private static boolean[][] visited;
    private static int[] dx = {1, -1, 0, 0};
    private static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        setInput();
        visited = new boolean[length][length];
        final List<Integer> countList = new ArrayList<>();
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length; j++) {
                if (graph[i][j] == 1 && !visited[i][j]) {
                    countList.add(dfs(i, j, 0));
                }
            }
        }
        Collections.sort(countList);
        System.out.println(countList.size());
        for (Integer count : countList) {
            System.out.println(count);
        }
    }

    private static void setInput() throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        length = parseInt(br.readLine());
        graph = new int[length][length];
        for (int i = 0; i < length; i++) {
            final String[] row = br.readLine().split("");
            for (int j = 0; j < length; j++) {
                graph[i][j] = parseInt(row[j]);
            }
        }
    }

    private static int dfs(int x, int y, int count) {
        visited[x][y] = true;
        count++;
        for (int i = 0; i < 4; i++) {
            final int nx = x + dx[i];
            final int ny = y + dy[i];
            if (0 <= nx && nx < length && 0 <= ny && ny < length) {
                if (graph[nx][ny] == 1 && !visited[nx][ny]) {
                    count = dfs(nx, ny, count);
                }
            }
        }
        return count;
    }
}
