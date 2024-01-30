package D240130;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Scanner;

public class bj_9086 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        String[] array = new String[n];

        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            char first = str.charAt(0);
            char end = str.charAt(str.length() - 1);

            String add = "" + first + end;

            array[i] = add;

        }

        for (String a : array) {
            System.out.println(a);
        }
    }
}
