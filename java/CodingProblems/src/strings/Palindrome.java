package strings;
	public class Palindrome {
		public static void main(String[] args) {
			System.out.println(checkPalindrome("abba"));
		}
	
		public static boolean checkPalindrome(String str) {
			int start = 0, end = str.length() - 1;
			while (start < end) {
				if (str.charAt(start) != str.charAt(end)) {
					return false;
				}
				start++;
				end--;
			}
			return true;
		}
	}
