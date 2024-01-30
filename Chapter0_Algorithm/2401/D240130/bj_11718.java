package D240130;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.stream.Stream;

public class bj_11718 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder builder = new StringBuilder();
        while (true) {
            String str = br.readLine();
            if (str == null || str.isEmpty()) {
                break;
            }
            builder.append(str).append("\n");
        }

        br.close();
        System.out.println(builder);
    }
}
