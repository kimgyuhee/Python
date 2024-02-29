package D240229;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_1735 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long A1 = Integer.parseInt(st.nextToken());
        long B1 = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        long A2 = Integer.parseInt(st.nextToken());
        long B2 = Integer.parseInt(st.nextToken());

        long A = A1 * B2 + A2 * B1;
        long B = B1 * B2;

        long gcd = getGCD(A, B);

        System.out.println(A / gcd + " " + B / gcd);

    }

    private static long getGCD(long a, long b) {
        // throw new UnsupportedOperationException("Unimplemented method 'gcd'");
        if (a % b == 0)
            return b;

        return getGCD(b, a % b);

    }

}