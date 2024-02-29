package D240229;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_2485 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] T = new int[n - 1];

        int first = Integer.parseInt(br.readLine());
        int end = first;
        for (int i = 0; i < T.length; i++) {
            int num = Integer.parseInt(br.readLine());
            int diff = num - end;
            end = num;
            T[i] = diff;
        }

        long gcd = getGCD(T[0], T[1]);

        for (int i = 2; i < T.length; i++) {
            gcd = getGCD(gcd, T[i]);
        }

        System.out.println(((end - first) / gcd) - n + 1);
    }

    private static long getGCD(long a, long b) {
        // throw new UnsupportedOperationException("Unimplemented method 'gcd'");
        if (a % b == 0)
            return b;

        return getGCD(b, a % b);

    }

}