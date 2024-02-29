package D240229;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 17103번 골드바흐 파티션
public class bj_17103v2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        // 소수 구하기 = 소수 false
        boolean[] num = new boolean[1000001];
        num[0] = num[1] = true;
        for (int i = 2; i * i <= 1000000; i++) {
            if (!num[i]) {
                for (int j = i + i; j <= 1000000; j += i) {
                    num[j] = true;
                }
            }
        }

        while (t-- > 0) {
            int temp = Integer.parseInt(br.readLine());
            int ans = 0;
            for (int j = 2; j <= temp / 2; j++) {
                if (!num[j] && !num[temp - j])
                    ans++;
            }
            System.out.println(ans);
        }
    }

}

// 다음으로 a와 b가 N을 구성하는 소수라면, a를 N/2이하까지만 탐색한다.(절반을 넘어가면 수가 겹치므로)
// 앞쪽에 있는 소수 그리고 뒤쪽에 있는 소수를 탐색하여 둘다 소수이면=골드바흐이면=N이 소수의 합이면 카운트를 증가시킨다.