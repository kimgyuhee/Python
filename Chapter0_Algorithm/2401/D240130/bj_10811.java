// N, M = input().split(" ")

// assembly = [ i+1 for i in range(int(N))]

// for i in range(int(M)):
//     m = input().split(" ")
//     a = int(m[0])-1
//     b = int(m[1])

//     assembly = assembly[:a] + assembly[a:b][::-1]+assembly[b:]

// result = " ".join(map(str, assembly))

// print(result)

package D240130;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_10811 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));

        String[] n = br.readLine().split(" ");
        int N = Integer.parseInt(n[0]);
        int M = Integer.parseInt(n[1]);

        String[] array = new String[N];

        for (int i = 0; i < N; i++) {
            array[i] = "" + (i + 1);
        }

        System.out.println(array);

        for (int i = 0; i < M; i++) {
            String[] q = br.readLine().split(" ");
            int a = Integer.parseInt(q[0]);
            int b = Integer.parseInt(q[1]);
            int sum = a + b;

            for (int j = 0; j < (b - a + 1) / 2; j++) {
                int index = sum - 1 - (a + j);
                String temp = array[index];
                array[index] = array[(a + j) - 1];
                array[(a + j) - 1] = temp;
            }

            String strArrayToString = String.join(" ", array);
            System.out.println(strArrayToString);

        }

        String strArrayToString = String.join(" ", array);
        System.out.println(strArrayToString);
    }
}
