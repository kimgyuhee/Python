package D240131;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_3003 {
    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Integer[] basic_set = { 1, 1, 2, 2, 2, 8 };

        String[] arrays = br.readLine().split(" ");

        String result = "";

        for (int i = 0; i < 6; i++) {
            int n = Integer.parseInt(arrays[i]);
            result += (basic_set[i] - n) + " ";
        }

        System.out.println(result);

    }
}
