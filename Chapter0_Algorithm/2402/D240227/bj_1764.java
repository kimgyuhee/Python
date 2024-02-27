package D240227;

// 시간 초과
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class bj_1764 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<String> arrayList1 = new ArrayList<String>();
        List<String> arrayList2 = new ArrayList<String>();

        for (int i = 0; i < n; i++) {
            String name = br.readLine();
            arrayList1.add(name);
        }

        for (int i = 0; i < m; i++) {
            String name = br.readLine();
            arrayList2.add(name);
        }

        arrayList1.retainAll(arrayList2);
        arrayList1.sort(String::compareTo);

        System.out.println(arrayList1.size());
        for (String name : arrayList1) {
            System.out.println(name);
        }

    }
}
