package D240207;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_2720 {
    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] coins = { 25, 10, 5, 1 };

        int T = Integer.parseInt(br.readLine());

        String result = "";
        for (int i = 0; i < T; i++) {

            int C = Integer.parseInt(br.readLine());

            for (int j = 0; j < 4; j++) {
                int c = C / coins[j];
                C = C % coins[j];
                // count[j] = c;
                if (j == 3) {
                    if (i == T - 1)
                        result = result + c;
                    else
                        result = result + c + "\n";
                } else {
                    result = result + c + " ";
                }
            }
        }

        System.out.println(result);
    }
}
