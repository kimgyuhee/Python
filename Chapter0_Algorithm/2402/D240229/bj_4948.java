package D240229;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class bj_4948 {
    public static void main(String args[]) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = "";
        while (true) {
            int num = Integer.parseInt(br.readLine());
            if (num == 0) {
                break;
            }
            int count = 0;
            for (int i = num + 1; i <= num * 2; i++) {
                if (is_prime_number(i)) {
                    count++;
                }
            }
            str += count + "\n";
        }

        System.out.println(str);
    }

    private static boolean is_prime_number(int n) {
        boolean result = true;
        if (n == 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                result = false;
                break;
            }
        }
        return result;
    }
}