package D240229;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class bj_17103 {
    public static void main(String args[]) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String str = "";
        for (int i = 0; i < n; i++) {

            int num = Integer.parseInt(br.readLine());
            int square = 1;
            int nn = 2;
            int count = 0;
            while (square < num) {
                square = (int) Math.pow(nn, 2);
                nn++;
                count++;
            }

            str += count + "\n";
        }

        System.out.println(str);
    }

}