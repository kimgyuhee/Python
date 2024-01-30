package D240130;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class bj_5597 {
    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));

        Integer[] array = new Integer[30];

        for (int i = 1; i <= 30; i++) {
            array[i - 1] = i;
        }

        for (int i = 1; i <= 28; i++) {
            int submitted = Integer.parseInt(br.readLine());
            array[submitted - 1] = 0;
        }

        Arrays.sort(array);

        System.out.println(array[30 - 2]);
        System.out.println(array[30 - 1]);

    }
}
