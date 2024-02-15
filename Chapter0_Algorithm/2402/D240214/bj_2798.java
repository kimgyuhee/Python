package D240214;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_2798 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] N_M = br.readLine().split(" ");
        int N = Integer.parseInt(N_M[0]);
        int M = Integer.parseInt(N_M[1]);

        Integer[] cards = new Integer[N];

        String[] card_str = br.readLine().split(" ");

        for (int i = 0; i < N; i++) {
            cards[i] = Integer.parseInt(card_str[i]);
        }

        int max = 0;
        boolean check_point = true;

        for (int i = 0; i < N - 2; i++) {
            if (!check_point)
                break;
            for (int j = i + 1; j < N - 1; j++) {
                if (!check_point)
                    break;
                for (int k = j + 1; k < N; k++) {
                    int card_sum = cards[i] + cards[j] + cards[k];
                    // System.out.println(card_sum);
                    if (card_sum == M) {
                        System.out.println(M);
                        check_point = false;
                        break;
                    } else if (card_sum > M) {
                        continue;
                    } else {
                        if (max <= card_sum) {
                            // System.out.println("최댓값이 바뀜요 ~");
                            max = card_sum;
                        }
                    }
                }
            }
        }

        if (check_point)
            System.out.println(max);

    }
}
