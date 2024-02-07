package D240207;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_11005 {
    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] N_digit = br.readLine().split(" ");
        int N = Integer.parseInt(N_digit[0]);
        int digit = Integer.parseInt(N_digit[1]);

        String con = convert(N, digit);
        System.out.println(reverse(con));
    }

    public static String convert(int N, int digit) {
        char[] words = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };

        String result = "";

        while (N != 0) {
            if (N % digit >= 10) {
                result += words[N % digit];
            } else {
                result += "" + (N % digit);
            }

            N = N / digit;
        }

        return result;
    }

    public static String reverse(String str) {
        String result = "";

        for (int i = str.length() - 1; i >= 0; i--) {
            result = result + str.charAt(i);
        }
        return result;
    }

}
