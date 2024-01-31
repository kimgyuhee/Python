package D240131;

import java.util.Scanner;

public class bj_2444 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 0; i < (n * 2 - 1); i++) {
            int e = Math.abs((n - i) - 1);
            int s;
            if (i < n)
                s = i * 2 + 1;
            else
                s = Math.abs(i - (2 * n - 2)) * 2 + 1;

            System.out.println(" ".repeat(e) + "*".repeat(s));

        }
    }
}
