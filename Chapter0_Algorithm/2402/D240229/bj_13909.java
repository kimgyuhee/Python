package D240229;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class bj_13909 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int cnt = 0;
        for (int i = 1; i < n + 1; i++) {
            if ((int) Math.pow(i, 2) <= n) {
                cnt++;
            } else {
                break;
            }
        }
        System.out.println(cnt);
    }
}
// n = int(input())

// cnt = 0
// for i in range(1, n+1):
// if i**2 <= n:
// cnt += 1
// else:
// break

// print(cnt)

// package D240229;

// import java.io.BufferedReader;
// import java.io.InputStreamReader;

// public class bj_13909 {
// public static void main(String args[]) throws Exception {

// BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
// int n = Integer.parseInt(br.readLine());
// int square = 1;
// int num = 1;
// int count = 0;
// while (square < n) {
// square = (int) Math.pow(num++, 2);
// if (square > n) {
// break;
// }
// // System.out.println(square);
// count++;
// }

// System.out.println(count);
// }

// }