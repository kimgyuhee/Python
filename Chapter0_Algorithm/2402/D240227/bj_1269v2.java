package D240227;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class bj_1269v2 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashMap<String, Integer> map = new HashMap<>();
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            map.put(st.nextToken(), 0);
        }

        int intersection = 0;
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < m; i++) {
            if (map.containsKey(st.nextToken())) {
                intersection += 1;
            }
        }

        System.out.println(n + m - (intersection * 2));

    }
}
