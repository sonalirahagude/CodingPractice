package strings;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;


public class MatchLongestStrings {

		public static void main(String[] args) {
			char[] letters = {'l','o','o','n'};
			int[] limits = new int[26];
			for(char c : letters) {
				limits[c - 'a']++;
			}
			Scanner sc = null;
			try {
				sc = new Scanner(new File("/home/sonali/workspace/FullTimePractice/src/a.txt"));
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			List<String> words = new ArrayList<String>();
			while(sc.hasNext()) {
				words.add(sc.next());
			}
			System.out.println("Matches: ");
			System.out.println(getLongMatches(words, limits, letters));
			sc.close();
 		}
		
		public static List<String> getLongMatches(List<String> words,int[] limits, char[] letters ) {
			Collections.sort(words, new LengthComparator());
			System.out.println(words);
			int maxLen = words.get(0).length();
			List<String> longMatches = new ArrayList<String>();
			for(String word: words) {
				boolean isMatch = checkMatch(word, limits, letters, maxLen);
				if(isMatch == true) {
					// this will remain constant once set
					maxLen = word.length();
					longMatches.add(word);					
				}
			}
			return longMatches;
		}
		
		private static boolean checkMatch(String word, int[] limits, char[] letters, int maxLen) {
			if(maxLen > word.length())
				return false;
			int[] index = new int[26];
			for(char c : word.toCharArray()) {
				index[c - 'a'] ++;
			}
			
			for(char c : letters) {
				if(index[c-'a'] > 0 && index[c-'a'] <= limits[c-'a']) {
					
				}
				else {
					return false;
				}
			}
			return true;
		}

		static class LengthComparator implements Comparator<String> {

			@Override
			public int compare(String o1, String o2) {
				if(o1.length() > o2.length())
					return -1;
				else if(o1.length() <  o2.length())
					return 1;
				return 0;
			}
			
		}
}
