package D240229;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_13241 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long A = Integer.parseInt(st.nextToken());
        long B = Integer.parseInt(st.nextToken());
        long gcd = getGCD(A, B);

        System.out.println(A * B / gcd);

    }

    private static long getGCD(long a, long b) {
        // throw new UnsupportedOperationException("Unimplemented method 'gcd'");
        if (a % b == 0)
            return b;

        return getGCD(b, a % b);

    }

}