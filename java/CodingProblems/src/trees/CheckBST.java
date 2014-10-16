package trees;

public class CheckBST {

	public static void main(String[] args) {
		Node root = Node.constructBST(0,5);
		Node.inorder(root);
		System.out.println(checkBST(root));
	}

	public static boolean checkBST(Node root) {
		return inorder(root, null, true);
	}

	public static boolean inorder(Node root, Node parent, boolean isLeft) {
		if (root == null)
			return true;
		if (parent != null) {
			if (isLeft && parent.data < root.data) {
				return false;
			}
			if (!isLeft && parent.data > root.data) {				
				return false;
			}
		}
		boolean left = inorder(root.left, root, true);
		boolean right = inorder(root.right, root, false);
		return left && right;

	}
}
