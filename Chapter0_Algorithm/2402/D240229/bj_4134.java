package D240229;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_4134 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double T = Double.parseDouble(br.readLine());

        double[] result = new double[(int) T];
        for (double i = 0; i < T; i++) {
            double num = Double.parseDouble(br.readLine());
            while (!getPrimeNumber(num)) {
                num++;
            }
            result[(int) i] = num;

        }

        for (double n : result) {
            System.out.println((int) n);
        }
    }

    private static boolean getPrimeNumber(double n) {
        boolean result = true;
        if (n == 1 || n == 0) {
            return false;
        }
        for (double i = 2; i < Math.sqrt(n); i++) {
            if (n % i == 0) {
                result = false;
                break;
            }
        }

        return result;

    }

}