package D240131;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_10988 {
    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String palindrome = br.readLine();

        boolean result = true;

        for (int i = 0; i < palindrome.length() / 2; i++) {
            if (palindrome.charAt(i) != palindrome.charAt(palindrome.length() - 1 - i)) {
                result = false;
                break;
            }

        }

        if (result)
            System.out.println(1);
        else
            System.out.println(0);

    }
}
