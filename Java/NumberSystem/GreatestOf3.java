import java.util.Scanner;

public class GreatestOf3 {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        System.out.println("Enter the first number :");
        int num1 = sc.nextInt();
        System.out.println("Enter the second number :");
        int num2 = sc.nextInt();
        System.out.println("Enter the third number :");
        int num3 = sc.nextInt();
        System.out.println("The greatest among the three numbers is :" +Math.max(num1, +Math.max(num2, num3)));

    }
    
}
