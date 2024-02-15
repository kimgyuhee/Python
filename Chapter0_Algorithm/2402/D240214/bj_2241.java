package D240214;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_2241 {
    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        boolean found = false;

        for (int i = 1; i < n; i++) {
            String str = "" + i;
            String[] l = str.split("");
            int sum = i;
            for (int j = 0; j < l.length; j++) {
                sum += Integer.parseInt(l[j]);
            }

            if (sum == n) {
                System.out.println(i);
                found = true;
                break;
            }

        }

        if (!found) {
            System.out.println(0);
        }
    }
}
