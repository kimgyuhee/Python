package D240227;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class bj_14425 {
    public static void main(String[] args) throws NumberFormatException, IOException {

        long beforeTime = System.currentTimeMillis(); // 코드 실행 전에 시간 받아오기

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] N_M = br.readLine().split(" ");
        int N = Integer.parseInt(N_M[0]);
        int M = Integer.parseInt(N_M[1]);

        List<String> list = new ArrayList<String>();

        int result = 0;
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            list.add(str);
        }

        for (int i = 0; i < M; i++) {
            String str = br.readLine();
            if (list.contains(str)) {
                result += 1;
            }
        }

        System.out.println(result);

        long afterTime = System.currentTimeMillis(); // 코드 실행 후에 시간 받아오기
        long diffTime = afterTime - beforeTime; // 두 개의 실행 시간
        System.out.println("실행 시간(ms): " + diffTime); // 세컨드(초 단위 변환)

    }
}
