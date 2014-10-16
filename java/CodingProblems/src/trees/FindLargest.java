package trees;
public class FindLargest {
	public static void main(String[] args) {
		int[] arr = {2,3,7,6,5};
		int k=2;
		findFirstKLargest(arr, k);
		for(int i= arr.length - 1; i >= arr.length - 1 - k +1; i--) {
			System.out.println(arr[i]);
		}
		
	}

	public static void findFirstKLargest(int[] arr, int k) {
		for (int i=0; i < k-1; i++) {
			int max = Integer.MIN_VALUE;
			int maxIndex = -1;
			for (int j=0; j < arr.length - i - 1; j++) {
				if( max < arr[j]) {
					max = arr[j];
					maxIndex = j;
				}
			}
			swap(arr, arr.length - i - 1,maxIndex);
		}
	}

	public static void swap(int arr[], int a, int b) {
		int temp = arr[a];
		arr[a] = arr[b];
		arr[b] = temp;
	}
}
