package misc;
public class LongestIncreasingSeq {
	public static void main(String[] args) {
		int[] arr = { -2, -1, 4, 3,1, -4, 1,9,-4 };
		String s = "sonali";
		int c = 1;
		int t = c >> 1;
		System.out.println(t);
		//findLongestSub(arr);
	}

	public static void findLongestSub(int arr[]) {
		int start = 0, maxStart = 0, maxEnd = 0;
		int maxSum = 0;
		int sum = 0;
		int i = 0;
		while (arr[i] <= 0) {
			i++;
			start = i;
		}
		while (i < arr.length) {
		//System.out.println(sum);
			if (sum > sum + arr[i]) { // this a seq.
				if (maxSum < sum) {
					maxStart = start;
					maxEnd = i;
					maxSum = sum;
					start = i;
					sum =0;
					while (arr[i] <= 0) {
						i++;
						if(i == arr.length)
							break;
						start = i;
					}
				}
			} else {
				sum += arr[i];
				i++;	
			}
		}
		if (sum > maxSum) {
			maxStart = start;
			maxEnd = i;
			maxSum = sum;
		}
		for (i = maxStart; i < maxEnd; i++)
			System.out.println(arr[i]);
	}
}
