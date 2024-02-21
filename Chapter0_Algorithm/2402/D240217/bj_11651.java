package D240217;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class bj_11651 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[][] points = new int[N][2];

        for (int i = 0; i < N; i++) {
            String[] p = br.readLine().split(" ");
            points[i][0] = Integer.parseInt(p[0]);
            points[i][1] = Integer.parseInt(p[1]);
        }

        Arrays.sort(points, new Comparator<int[]>() {

            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[1] != o2[1] ? o1[1] - o2[1] : o1[0] - o2[0];
            }
        });

        for (int i = 0; i < N; i++) {
            System.out.println(points[i][0] + " " + points[i][1]);
        }
    }
}
