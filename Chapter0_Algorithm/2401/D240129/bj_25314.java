package D240129;

import java.util.Scanner;

public class bj_25314 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String str = "long ";
        String result = "";
        for (int i = 0; i < N / 4; i++) {
            result += str;
        }
        System.out.println(result + "int");
        // System.out.println(N / 4);
    }
}
