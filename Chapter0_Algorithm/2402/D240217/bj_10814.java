package D240217;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class bj_10814 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Object[][] info_list = new Object[n][2];

        for (int i = 0; i < n; i++) {
            String[] info = br.readLine().split(" ");
            info_list[i][0] = Integer.parseInt(info[0]);
            info_list[i][1] = info[1];
        }

        Arrays.sort(info_list, new Comparator<Object[]>() {

            @Override
            public int compare(Object[] o1, Object[] o2) {
                return (Integer) o1[0] - (Integer) o2[0];
            }
        });

        for (int i = 0; i < n; i++) {
            System.out.println(info_list[i][0] + " " + info_list[i][1]);
        }

    }

}
