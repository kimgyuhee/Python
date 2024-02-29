package D240229;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_1934 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");
        int T = Integer.parseInt(br.readLine());

        int[] result = new int[T];
        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int gcd = getGCD(A, B);
            System.out.println(A * B / gcd);
            result[i] = A * B / gcd;
        }

        for (int n : result) {
            System.out.println(n);
        }
    }

    private static int getGCD(int a, int b) {
        // throw new UnsupportedOperationException("Unimplemented method 'gcd'");
        if (a % b == 0)
            return b;

        return getGCD(b, a % b);

    }

}