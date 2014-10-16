package strings;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
 The second interview asks to substitute *s in a string by binary numbers. For example, input aa*bbb*c, the output should be four strings: aa0bbb0c, aa0bbb1c, aa1bbb0c, aa1bbb1c 
 */

// count the number of *'s and create those many binary numbers like if no of * is 4. 2^ 4 -1 
// will give all the possible combinations.
public class StringSubstitute {
	public static void main(String[] args) {
		String str = "aa*b**";
		substitute(str);
	}

	public static void substitute(String s) {
		int count = 0;
		for (char c : s.toCharArray()) {
			if (c == '*') {
				count++;
			}
		}
		// now generate all the combinations
		int start = 0;
		int end = (int) Math.pow(2, count) - 1;
		System.out.println("end: " + end);
		List<String> list = new ArrayList<String>();
		for (int number = 0; number <= end; number++) {
			char[] strArray = s.toCharArray();
			int c = number;
			for (int i = 0; i < s.length(); i++) {
				if (strArray[i] == '*') {
					strArray[i] = Character.forDigit((c & 1),10);
					c = c >> 1;
				}
			}
			list.add(Arrays.toString(strArray).replace(",", ""));
		}
		for (String str : list)
			System.out.println(str);
	}
}
