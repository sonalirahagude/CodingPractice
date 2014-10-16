package trees;

public class LeastCommonAncestorTree {
	public static void main(String[] args) {
		int[] sortedArray = {1,2,3,4,5};
		Node root = createBalancedTree(sortedArray, 0 , sortedArray.length);
		//inorder(root);
		Node a = commonAncestor(root, 1, 5);
		System.out.println(a.data);
	}

	public static Node createBalancedTree(int[] arr, int low, int high)  {
		if(low >= high)
			return null;
		int mid = ( low + high )/2;
		Node node= new LeastCommonAncestorTree().new Node();
		node.data = arr[mid];
		node.left = createBalancedTree(arr, low, mid);
		node.right = createBalancedTree(arr, mid+1, high);
		return node;
	} 

	public static void inorder(Node root) {
		if(root == null) 
			return;
		inorder(root.left);
		System.out.println(root.data);
		inorder(root.right);
	}

	public class Node {
		public Node left;
		public Node right;
		public int data;
	}


	public static Node commonAncestor(Node root, int p, int q) {
		if(covers(root.left, p) && covers(root.left, q) ) {
			return commonAncestor(root.left, p , q);
		}
		if(covers(root.right, p) && covers(root.right, q) ) {
			return commonAncestor(root.right, p , q);
		}
		return root;
	}

	public static boolean covers(LeastCommonAncestorTree.Node root, int n) {
		if(root == null) {
			return false;
		}
		if(root.data == n) {
			return true;
		}
		return covers(root.left,n) || covers(root.right,n);
}		
}
