
public class StaticBlock {

	public static void main(String[] args) {
		System.out.println("Hello Kartik. This is a basic java program.");
	}

	static {
		System.out.println("Static Block. This is executed once, when the class is loaded, even before main method is called.");
	}

}
