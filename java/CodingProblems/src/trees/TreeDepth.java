package trees;
public class TreeDepth {

	public class Node {
		public Node left;
		public Node right;
		public int data;
	}

	public static void main(String[] args) {
		Node root = constructTree(2);
		inorder(root);
		System.out.println("Depth: " + findDepth(root));
	}

	public static Node constructTree(int count) {
		if (count == 0) {
			return null;
		}
		Node node = new TreeDepth().new Node();
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

	public static int findDepth(Node root) {
		if (root == null)
			return 0;
		int ldepth = findDepth(root.left);
		int rdepth = findDepth(root.right);
		if (ldepth > rdepth)
			return ldepth + 1;
		return rdepth + 1;
	}

}
