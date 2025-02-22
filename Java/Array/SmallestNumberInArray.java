class SmallestNumberInArray {
    public static void main(String[] args) {
        int[] arr = {132, 24, 38,473,902,625,629,23,32};
        int SmallNum = Integer.MAX_VALUE;
        for(int i = 0; i< arr.length; i++)
        {
            SmallNum = Math.min(SmallNum,arr[i]);
        }
    System.out.println("The smallest number in the array is :" + SmallNum);
    }
}