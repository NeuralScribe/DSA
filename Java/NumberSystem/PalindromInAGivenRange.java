import java.util.*;
public class PalindromInAGivenRange{
    public static void main (String args[]){
    
        // for Input
      Scanner sc = new Scanner(System.in);
      String inputStr = sc.nextLine(); // "10 30"
      String[] inputStrArr= inputStr.split(" "); //["10","30"] removes the space and returnd the string as an array
      int[] inputArr = new int[inputStrArr.length];
      for(int i=0;i<inputStrArr.length; i++){ //to traverse the str arr and convert it into int
        inputArr[i]=Integer.parseInt(inputStrArr[i]);
       }
      System.out.println(inputArr);// [10,30]
       int min = inputArr[0];
       int max= inputArr[1];
    
          // for Input taking 
       
       // Run a loop between max and min 
        for( int i=min; i<=max;i++){
           if(checkPalindromeOrNot(i)){
                System.out.print(i+" ");
           }
        }
        
    }
    public static boolean checkPalindromeOrNot(int num){ //1221
        int rev = 0; 
        int temp= num;
        while(temp>0){
            int digit = temp%10;
            rev= rev*10+digit;
            temp=temp/10;  //terminate
        }
        if(rev==num){
            return true;
        }else{
            return false;
        }
    }
}