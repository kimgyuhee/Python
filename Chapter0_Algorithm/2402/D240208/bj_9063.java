package D240208;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class bj_9063 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        List<Integer> xlist = new ArrayList<Integer>();
        List<Integer> ylist = new ArrayList<Integer>();

        for (int i = 0; i < N; i++) {
            String[] xy = br.readLine().split(" ");
            int x = Integer.parseInt(xy[0]);
            int y = Integer.parseInt(xy[1]);

            if (!xlist.contains(x)) {
                xlist.add(x);
            }

            if (!ylist.contains(y)) {
                ylist.add(y);
            }
        }

        xlist.sort(Comparator.naturalOrder());
        ylist.sort(Comparator.naturalOrder());

        System.out.println(xlist.toString());
        System.out.println(ylist.toString());

        int X = (int) xlist.get(xlist.size() - 1) - (int) xlist.get(0);
        int Y = (int) ylist.get(ylist.size() - 1) - (int) ylist.get(0);

        System.out.println(X * Y);

    }
}
