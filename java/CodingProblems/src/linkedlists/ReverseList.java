package linkedlists;
public class ReverseList {

	public class Node {
		public int data;
		public Node next;
	}

	public static void main(String[] args) {
		Node head = constructList();
		Node node = head;
		while (node != null) {
			System.out.println(node.data);
			node = node.next;
		}
		head = reverse(head);
		while (head != null) {
			System.out.println(head.data);
			head = head.next;
		}
	}

	public static Node reverse(Node n) {
		if (n == null) // empty list
			return null;
		if (n.next == null)
			return n;
		Node last = reverse(n.next);
		n.next.next = n;
		n.next = null;
		return last;
	}

	public static Node constructList() {
		Node head = new ReverseList().new Node();
		head.data = 1;
		Node node = head;
		for (int i = 2; i < 6; i++) {
			Node newNode = new ReverseList().new Node();
			newNode.data = i;
			head.next = newNode;
			newNode.next = null;
			head = newNode;
		}
		return node;
	}

}
