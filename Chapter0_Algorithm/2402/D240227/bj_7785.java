package D240227;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class bj_7785 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String co = st.nextToken();
            if (co.equals("enter")) {
                map.put(name, 0);
            } else {
                map.remove(name);
            }
        }

        List<String> keyList = new ArrayList<>(map.keySet());

        keyList.sort(String::compareTo);
        Collections.reverse(keyList);

        for (String key : keyList) {
            System.out.println(key);
        }

    }
}
