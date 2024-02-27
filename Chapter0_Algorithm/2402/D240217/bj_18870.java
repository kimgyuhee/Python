package D240217;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class bj_18870 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String[] xys = br.readLine().split(" ");
        List<Integer> intList = new ArrayList<>();

        int[] folder = new int[N];

        String result = "";
        for (int i = 0; i < N; i++) {
            if (intList.contains(Integer.parseInt(xys[i]))) {
                continue;
            } else {
                intList.add(Integer.parseInt(xys[i]));
                folder[i] = Integer.parseInt(xys[i]);
            }
        }

        Collections.sort(intList);
        // intList.sort(Comparator.naturalOrder());
        Arrays.sort(folder);

        for (int i = 0; i < N; i++) {
            int count = 0;
            int co = Integer.parseInt(xys[i]);
            for (int j = 0; j < intList.size(); j++) {
                // System.out.println(xys[i] + " " + foler[j]);
                if (co == intList.get(j)) {
                    break;
                }
                count++;
            }

            result += count + " ";
        }

        System.out.println(result);

    }

}
