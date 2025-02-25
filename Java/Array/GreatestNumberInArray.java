class GreatestNumberInArray {
    public static void main(String[] args) {
        int[] arr = {132, 24, 38,473,902,625,629,23,32};
        int GreatNum = Integer.MIN_VALUE;
        for(int i = 0; i< arr.length; i++)
        {
            GreatNum = Math.max(GreatNum,arr[i]);
        }
    System.out.println("The smallest number in the array is :" + GreatNum);
    }
}






















