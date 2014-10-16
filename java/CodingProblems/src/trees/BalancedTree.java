package trees;
public class BalancedTree {
	public static void main(String[] args) {
		//int[] sortedArray = {1,2,3,4,5};
		//Node root = createBalancedTree(sortedArray, 0 , sortedArray.length);
		//inorder(root);
		Node root = Node.constructTree(3);
		Node.inorder(root);
	}

	public static Node createBalancedTree(int[] arr, int low, int high)  {
		if(low >= high)
			return null;
		int mid = ( low + high )/2;
		Node node= new Node();
		node.data = arr[mid];
		node.left = createBalancedTree(arr, low, mid);
		node.right = createBalancedTree(arr, mid+1, high);
		return node;
	} 


}
