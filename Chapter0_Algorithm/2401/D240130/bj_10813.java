// N, M = input().split(" ")

// array = [ i+1 for i in range(int(N))]

// for i in range(int(M)):
//     m = input().split(" ")
//     a = int(m[0])-1
//     b = int(m[1])-1
//     temp = array[a]
//     array[a] = array[b]
//     array[b] = temp

// result = " ".join(map(str, array))

// print(result)

package D240130;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_10813 {
    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

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
            String temp = array[Integer.parseInt(q[0]) - 1];
            array[Integer.parseInt(q[0]) - 1] = array[Integer.parseInt(q[1]) - 1];
            array[Integer.parseInt(q[1]) - 1] = temp;
        }

        String strArrayToString = String.join(" ", array);
        String result = strArrayToString.replaceAll("null", "0");
        System.out.println(result);

    }
}
