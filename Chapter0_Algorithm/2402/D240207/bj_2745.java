package D240207;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_2745 {
    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] B_N = br.readLine().split(" ");
        String B = B_N[0];
        char[] chs = B.toCharArray();
        int N = Integer.parseInt(B_N[1]);
        int result = 0;

        for (int i = 0; i < B.length(); i++) {
            int digit = (int) Math.pow(N, i);
            if (!Character.isDigit(chs[chs.length - 1 - i])) {
                int n = (int) chs[chs.length - 1 - i] - 55;
                result += (n * digit);
            } else {
                int n = chs[chs.length - 1 - i] - '0';
                result += (n * digit);
            }
        }

        System.out.println(result);
    }
}
