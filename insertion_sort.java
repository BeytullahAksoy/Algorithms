public class insertion_sort {
    public static void main(String[] args){


        int[] A={1,321,412,1,5,132,1,3,32,3,3,252,-32,234};
        A= insertion(A);
        for (int i:A) {
            System.out.println(i);
        }
    }



    public static int[] insertion(int[]A){
        int n = A.length;
        for(int i =1;i<n;i++){

            int key = A[i]; // hold the key that will be fixed
            int j = i-1; // if the key is less then the previous one it means the key should be in left side.
            // so the while loop should work

            while(j>=0 && key < A[j]  ){
                A[j+1] = A[j];// if the compared value(A[j]) is less then the key , the compared should be in right
                j--;// check if the another left one is more than our key

            }
            //if while stopped it means the value in jth index is not more than our key
            // put the key into j+1th index becuase jth value is not more than our key
            A[j+1] = key;

        }

        return A;
    }
}




