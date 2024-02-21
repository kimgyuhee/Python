package D240217;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class bj_25305 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] N_k = br.readLine().split(" ");
        int N = Integer.parseInt(N_k[0]);
        int k = Integer.parseInt(N_k[1]);

        String[] scores = br.readLine().split(" ");
        int[] sc = new int[scores.length];

        for (int i = 0; i < scores.length; i++) {
            sc[i] = Integer.parseInt(scores[i]);
        }

        Arrays.sort(sc);

        System.err.println(sc[N - k]);
    }
}
