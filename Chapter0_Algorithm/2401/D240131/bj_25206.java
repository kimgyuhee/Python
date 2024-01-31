package D240131;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class bj_25206 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        double sum = 0.0; // 학점의 총합
        double total = 0.0; // 학점 × 과목평점

        Map<String, Double> map = new HashMap<>();
        map.put("A+", 4.5);
        map.put("A0", 4.0);
        map.put("B+", 3.5);
        map.put("B0", 3.0);
        map.put("C+", 2.5);
        map.put("C0", 2.0);
        map.put("D+", 1.5);
        map.put("D0", 1.0);

        for (int i = 0; i < 20; i++) {
            String[] subject = br.readLine().split(" ");

            Double grade = Double.parseDouble(subject[1]);

            if (subject[2].equals("P")) {
                continue;
            } else if (subject[2].equals("F")) {
                sum += grade;
            } else {
                // System.out.println("\n\n\n" + subject[2] + "\n");
                // System.out.println(map.get(subject[2]) + "dsdsds");
                total += (map.get(subject[2]) * grade);
                sum += grade;
            }

        }

        System.out.printf("%.6f", total / sum);
    }
}
