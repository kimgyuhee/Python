import java.util.Scanner;

public class bj_11382 {

    public static void main(String[] args) {

        try (Scanner sc = new Scanner(System.in)) {
            String str_input = sc.nextLine();
            String[] array = str_input.split(" ");

            int result = 0;
            for (String a : array) {
                int num = Integer.parseInt(a);
                // System.out.println(num);
                result += num;
            }
            System.out.println(result);
        } catch (NumberFormatException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}