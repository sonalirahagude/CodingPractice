package misc;
import java.util.ArrayList;
import java.util.List;

public class SubsetsOfSet {
	public static void main(String[] args) {
		int[] arr = {1,2,3};
		List<List<Integer>> subsets = subsets(arr,0);
		for(List<Integer> l : subsets) {
				System.out.println(l);
		}
		
	}

	public static List<List<Integer>> subsets(int[] array, int index) {
		List<List<Integer>> newLists = new ArrayList<List<Integer>>();
		if (index == array.length) {
			List<Integer> list = new ArrayList<Integer>();
			// put empty list
			newLists.add(list);
			return newLists;
		}
		List<List<Integer>> lists = subsets(array, index + 1);
		//newLists.addAll(lists);
		for (List<Integer> list : lists) {
			newLists.add(list);
			List<Integer> newList = new ArrayList<Integer>(list);
			newList.add(array[index]);
			newLists.add(newList);
		}
		return newLists;
	}
}
