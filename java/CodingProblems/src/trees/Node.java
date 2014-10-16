package trees;


public class Node {

		public Node left;
		public Node right;
		public int data;



	public static Node constructTree(int count) {
		if (count == 0) {
			return null;
		}
		Node node = new Node();
		node.data = count;
		node.left = constructTree(count - 1);
		node.right = constructTree(count - 1);
		return node;
	}

	public static void inorder(Node root) {
		if (root == null)
			return;
		inorder(root.left);
		System.out.println(root.data);
		inorder(root.right);
	}
	
	public static Node constructBST(int low, int high) {
		if (low >= high)
			return null;
		int mid = (low + high)/2;
		Node node = new Node();
		node.data = mid;
		node.left = constructBST(low, mid); 
		node.right = constructBST(mid + 1, high);
		return node;
	}

	
}
