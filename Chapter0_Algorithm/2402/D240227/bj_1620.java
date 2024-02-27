package D240227;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class bj_1620 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashMap<Object, Object> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String pokemon = br.readLine();
            int num = i + 1;
            map.put(pokemon, "" + num);
            map.put("" + num, pokemon);
        }

        List<Object> list = new ArrayList<Object>();

        for (int i = 0; i < m; i++) {
            String q = br.readLine();
            list.add(map.get(q));
        }

        System.out.println("==============");
        for (Object o : list) {
            System.out.println(o);
        }
    }
}
