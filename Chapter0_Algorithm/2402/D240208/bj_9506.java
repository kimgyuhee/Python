package D240208;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class bj_9506 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        List<String> expression = new ArrayList<String>();

        while (true) {
            int N = Integer.parseInt(br.readLine());
            if (N == -1)
                break;

            List<Integer> divisors = new ArrayList<Integer>();
            int sum = 0;

            for (int i = 1; i < (N + 1) / 2; i++) {
                if (N % i == 0) {
                    if (!divisors.contains(i)) {
                        divisors.add(i);
                        sum += i;
                    }
                    if (!divisors.contains((N / i))) {
                        divisors.add((N / i));
                        sum += (N / i);
                    }
                }
            }
            divisors.sort(Comparator.naturalOrder());
            divisors.remove(divisors.size() - 1);
            String div = divisors.toString();
            // System.out.println(divisors.toString());

            if (sum - N == N) {
                String ex = div.substring(1, div.length() - 1).replaceAll(",", " +");
                // String ex1 = String.join(" + ", div);
                expression.add(N + " = " + ex);
            } else {
                expression.add(N + " is NOT perfect.");
            }
        }

        for (String e : expression) {
            System.out.println(e);
        }

    }

}
