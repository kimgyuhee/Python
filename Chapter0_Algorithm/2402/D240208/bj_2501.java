package D240208;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Comparator;
import java.util.List;

public class bj_2501 {

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] str = br.readLine().split(" ");
        int N = Integer.parseInt(str[0]);
        int K = Integer.parseInt(str[1]);

        List<Integer> divisors = new ArrayList<Integer>();

        for (int i = 1; i < (N + 1) / 2; i++) {
            if (N % i == 0) {
                if (!divisors.contains(i)) {
                    divisors.add(i);
                }
                if (!divisors.contains(N / i)) {
                    divisors.add(N / i);
                }
            }
        }

        divisors.sort(Comparator.naturalOrder());
        System.out.println(divisors.toString());
        if (divisors.size() < K) {
            System.out.println(0);
        } else {
            System.out.println(divisors.get(K - 1));
        }
    }

}
