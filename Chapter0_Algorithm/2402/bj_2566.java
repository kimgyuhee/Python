import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.stream.Stream;

public class bj_2566 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Scanner sc = new Scanner(System.in);
        System.out.println("anjdianjdu\n\n]n]n]n]n\n\n\n");
        int result = Integer.MIN_VALUE;
        int a = 0;
        int b = 0;

        // for (int i = 0; i < 9; i++) {
        // String str = br.readLine();
        // int[] digits = Stream.of(str.split("
        // ")).mapToInt(Integer::parseInt).toArray();
        // for (int j = 0; i < digits.length; j++) {
        // if (result < digits[j]) {
        // result = digits[j];
        // a = i + 1;
        // b = j + 1;
        // }
        // }
        // }
        int[][] arrays = new int[9][9];

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                int num = sc.nextInt();
                arrays[i][j] = num;
                if (num >= result) {
                    result = num;
                    a = i + 1;
                    b = j + 1;
                }
            }
        }

        System.out.println(result);
        System.out.println(a + " " + b);
    }

}
