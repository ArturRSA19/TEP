import java.util.Scanner;

public class teste
{
	public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();

        System.out.println((x == 1) ? "vale 1" : "vale 0");

        sc.close();
	}
}