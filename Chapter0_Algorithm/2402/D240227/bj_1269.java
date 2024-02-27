package D240227;

//시간초과
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class bj_1269 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        List<String> arrayList1 = new ArrayList<String>();
        List<String> arrayList3 = new ArrayList<String>();
        for (int i = 0; i < n; i++) {
            String num = st.nextToken();
            arrayList1.add(num);
            arrayList3.add(num);
        }

        st = new StringTokenizer(br.readLine());
        List<String> arrayList2 = new ArrayList<String>();
        for (int i = 0; i < m; i++) {
            arrayList2.add(st.nextToken());
        }

        arrayList3.retainAll(arrayList2);

        System.out.println(arrayList1.size() + arrayList2.size() - (arrayList3.size() * 2));

    }
}
