
package D240202;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class bj_2738 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] n = br.readLine().split(" ");
        int N = Integer.parseInt(n[0]);
        int M = Integer.parseInt(n[1]);

        Integer[][] arrays = new Integer[N][M];

        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < N; j++) {
                String[] line = br.readLine().split(" ");
                for (int k = 0; k < M; k++) {
                    if (arrays[j][k] == null) {
                        arrays[j][k] = 0;
                    }
                    int num = Integer.parseInt(line[k]);
                    arrays[j][k] += num;
                }
            }
        }

        for (Integer[] i : arrays) {
            String str = Arrays.toString(i);
            // String joinString = String.join(", ", str);
            System.out.println(str.substring(1, str.length() - 1));
            // System.out.println(joinString);
            // System.out.println("why..");
        }
    }
}