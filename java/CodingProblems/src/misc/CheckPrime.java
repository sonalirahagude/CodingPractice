package misc;
public class CheckPrime {
	public static void main(String[] args) {
		System.out.println(isPrime(21));
	}

	public static boolean isPrime(int n) {
		if(n == 2)
			return true;
		for (int i = 2; i <= Math.floor(Math.sqrt(n)); i++) {
			if (n % i == 0)
				return false;
		}
		return true;
	}

}
