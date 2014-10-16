package trees;
public class FibonacciMemoized {
	public static void main(String[] args) {
		int n = 8;
		int[] fib = new int[n + 1];
		fibonacci(n, fib);
		for(int i =0; i < fib.length; i++)
			System.out.println(fib[i]);
	}

	public static int fibonacci(int n, int[] fib) {
		if (n < 2) {
			fib[n] = n;
			return fib[n];
		}
		if (fib[n - 2] == 0)
			fib[n] = fibonacci(n - 1,fib) + fibonacci(n - 2,fib);
		else if (fib[n - 1] == 0)
			fib[n] = fibonacci(n - 1,fib) + fib[n - 2];
		else
			fib[n] = fib[n - 1] + fib[n - 2];
		return fib[n];
	}
}
