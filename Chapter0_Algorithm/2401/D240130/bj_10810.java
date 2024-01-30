package D240130;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_10810 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] n = br.readLine().split(" ");
        int N = Integer.parseInt(n[0]);
        int M = Integer.parseInt(n[1]);

        String[] array = new String[N];

        for (int i = 0; i < M; i++) {
            String[] q = br.readLine().split(" ");
            for (int j = Integer.parseInt(q[0]) - 1; j < Integer.parseInt(q[1]); j++) {
                array[j] = q[2];
            }
        }

        String strArrayToString = String.join(" ", array);
        String result = strArrayToString.replaceAll("null", "0");
        System.out.println(result);

    }
}
