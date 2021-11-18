public class merge_sort{


    public static void mergeSort(int[]A ,int p ,int r){
        if(p<r) {
            int m = ((p + r)-1) / 2;
            mergeSort(A,p,m);
            mergeSort(A,m+1,r);
            merge(A,p,m,r);
        }
    }

    public static void merge(int[] A,int l , int m , int r) {

        int [] left = new int[m-l+2];
        left[m-l+1]= Integer.MAX_VALUE;
        int[] right = new int [r-m+2];
        right[r-m+1] = Integer.MAX_VALUE;

        for(int i=0;i<left.length-1;i++){
            left[i] = A[i];

        }
        for(int i=0;i<right.length-1;i++){
            right[i] = A[i+m+1];

        }

        for (int i:right){
            System.out.println(i);
        }
        System.out.println("---------------");
        for (int i:left){
            System.out.println(i);
        }
        int lindex =0;
        int rindex=0;

        for(int i =0;i<A.length;){
            if(right[rindex]<=left[lindex]){
                A[i] = right[rindex];
                rindex++;
                i++;
            }

            if(left[lindex]<right[rindex]){
                A[i] = left[lindex];
                lindex++;
                i++;
            }

        }
        for(int i : A){
            System.out.println(i);
        }

    }


}