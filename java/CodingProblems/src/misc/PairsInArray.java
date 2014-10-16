package misc;
public class PairsInArray {
	public static void main(String[] args) {
		int[] arr = { 1, 2, 3, 4, 5 };
		findPairs(arr, 4);
	}

	public static void findPairs(int[] arr, int reqSum) {
		int start = 0, end = arr.length - 1;
		while (start < end) {
			if (arr[start] + arr[end] == reqSum) {
				System.out.println(arr[start] + "," + arr[end]);
				start++;
				end--;
			} else if (arr[start] + arr[end] > reqSum) {
				end--;
			} else {
				start++;
			}
		}

	}
}
