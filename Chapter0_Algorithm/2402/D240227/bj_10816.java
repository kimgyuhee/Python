package D240227;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.StringTokenizer;

public class bj_10816 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine()); // 카드의 개수

        HashMap<String, Integer> map = new HashMap<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            String n = st.nextToken();
            if (map.containsKey(n)) {
                int count = map.get(n) + 1;
                map.put(n, count);
            } else {
                map.put(n, 1);
            }
        }

        // Map<String, Integer> sortmap = new TreeMap<>(map);

        int M = Integer.parseInt(br.readLine()); // 구별할 수의 개수

        StringBuilder sb = new StringBuilder();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            String temp = st.nextToken();
            sb.append(binarySearch(map, temp) + " ");
        }

        bw.write(sb.toString() + "\n");
        bw.flush();
        bw.close();
        br.close();
    }

    public static int binarySearch(HashMap<String, Integer> map, String temp) {
        if (map.containsKey(temp)) {
            return map.get(temp);
        } else {
            return 0;
        }
    }

}
