import java.util.Scanner;

public class GreatestOf2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first number :");
        int num1 = sc.nextInt();
        System.out.println("Enter the second number :");
        int num2 = sc.nextInt();
        System.out.println("The Greatest among the 2 numbers is :" +Math.max(num1, num2));

    }
    
}
