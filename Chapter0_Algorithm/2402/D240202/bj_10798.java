package D240202;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_10798 {

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[][] words = new String[15][5];
        String w = "";
        for (int i = 0; i < 5; i++) {
            String[] word = br.readLine().split("");
            for (int j = 0; j < word.length; j++) {
                words[j][i] = word[j];
            }
        }

        for (int j = 0; j < 15; j++) {
            for (int i = 0; i < 5; i++) {
                if (words[j][i] != null)
                    w += words[j][i];
            }
        }
        System.out.println(w);
    }

}