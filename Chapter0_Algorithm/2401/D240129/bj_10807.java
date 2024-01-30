package D240129;

// import java.io.BufferedReader;
// import java.io.InputStreamReader;
// import java.util.Scanner;

// import java.util.*;
// import java.io.*;

// public class bj_10807 {
//     public static void main(String[] args) {

//         int N;
//         Scanner sc = new Scanner(System.in);
//         N = sc.nextInt();
//         sc.nextInt();
//         String str = sc.nextLine();
//         String[] array = new String[N];
//         array = str.split(" ");
//         int V = sc.nextInt();
//         int result = 0;
//         System.out.println(array.length);

//         for (int i = 0; i < N; i++) {
//             if (array[i].equals(V + ""))
//                 result += 1;
//         }

//         System.out.println(result);
//     }
// }

/*
 * import java.io.IOException;
 * import java.util.*;
 * 
 * 
 * public class Main {
 * public static void main(String[] args) throws IOException {
 * 
 * Scanner sc= new Scanner(System.in);
 * int number = sc.nextInt();
 * sc.nextInt(); // 이거를 추가했다
 * String str = sc.nextLine();
 * StringTokenizer st=new StringTokenizer(str," ");
 * int[] arr=new int[number];
 * for(int i=0;i<arr.length;i++){
 * arr[i] = Integer.parseInt(st.nextToken());
 * }
 * int search = sc.nextInt();
 * int ans=0;
 * for(int i=0;i<arr.length;i++){
 * if(search==arr[i]){
 * ans++;
 * }
 * }
 * System.out.println(ans);
 * }
 * }
 * 
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_10807 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int find = Integer.parseInt(br.readLine());

        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == find)
                count++;
        }
        System.out.println(count);
        br.close();
    }
}