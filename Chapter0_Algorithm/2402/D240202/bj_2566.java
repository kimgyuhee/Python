package D240202;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_2566 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int result = Integer.MIN_VALUE;
        int a = 0;
        int b = 0;

        int[][] arrays = new int[9][9];

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                int num = Integer.parseInt(br.readLine());
                arrays[i][j] = num;
                if (num >= result) {
                    result = num;
                    a = i + 1;
                    b = j + 1;
                }
            }
        }

        System.out.println(result);
        System.out.println(a + " " + b);
    }

}
