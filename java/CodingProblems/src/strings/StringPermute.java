package strings;
import java.util.HashSet;
import java.util.Set;

public class StringPermute {
	public static void main(String[] args) {
		Set<String> results = permute("soo");
		System.out.println(results);
	}

	public static Set<String> permute(String letters) {
		Set<String> results = new HashSet<String>();
		if (letters.length() == 1) {
			results.add(letters);
			return results;
		} else {
			char c = letters.charAt(0);
			String subset = letters.substring(1);
			Set<String> combinations = permute(subset);
			for (String str : combinations) {
				for (int i = 0; i <= str.length(); i++) {
					String s = str.substring(0, i) + c
							+ str.substring(i, str.length());
					results.add(s);
				}
			}

			return results;
		}
	}
}
