package D240217;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class bj_2587 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] list = new int[11];
        Integer[] l = new Integer[5];
        int sum = 0;

        for (int i = 0; i < 5; i++) {
            int n = Integer.parseInt(br.readLine());
            l[i] = n;
            list[n / 10] = n;
            sum += n;
        }

        Arrays.sort(l);

        int idx = 0;
        int mid = 0;
        for (int i = 0; i < list.length; i++) {
            if (list[i] != 0) {
                idx += 1;
            }

            if (idx == 2) {
                mid = list[i];
                break;
            }
        }

        System.out.println(sum / 5);
        System.out.println(l[2]);
        System.out.println(mid);
    }
}
