package D240208;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_5086 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String result = "";
        while (true) {
            String[] n = br.readLine().split(" ");
            int a = Integer.parseInt(n[0]);
            int b = Integer.parseInt(n[1]);

            if (a == 0 && b == 0)
                break;
            else if (b % a == 0)
                // System.out.println("factor");
                result += "factor";
            else if (a % b == 0)
                // System.out.println("multiple");
                result += "multiple";
            else
                // System.out.println("neither");
                result += "neither";

            result += "\n";
        }
        System.out.println(result.substring(0, result.length() - 1));

    }
}
