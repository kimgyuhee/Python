package D240208;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_11653 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int n = 2;
        while (true) {
            if (N == 1)
                break;
            else if (N == n) {
                System.out.println(n);
                break;
            } else {
                if (N % n == 0) {
                    N = N / n;
                    System.out.println(n);
                } else {
                    n += 1;
                }
            }

        }
    }

}
