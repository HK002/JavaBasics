
public class StaticMethods {

	public static void main(String[] args) {
		System.out.println("Inside Main Method.");
		StaticMethods.method1();
	}

	static void method1() {
		System.out.println("Inside Static Method 1");
	}
	
	static {
		System.out.println("Inside static Block");
		StaticMethods.method1();
	}
}
