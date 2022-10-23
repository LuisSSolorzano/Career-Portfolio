//Luis Solorzano

package symboltable;
import DataStructures2.StdIn;
import DataStructures2.StdOut;
import DataStructures2.BSTEssential;

public class TranslateCodonToAA {
	public static void main(String[] args) {
		BSTEssential<String,String> DNA = new BSTEssential<>();
		
		StdIn.fromFile("data/codontranslation.txt");
		String lines = StdIn.readLine();
		String[] divided = lines.split("\t");
		DNA.put(divided[0], divided[1]);
		
		while (!StdIn.isEmpty()) {
				lines = StdIn.readLine();
				divided = lines.split("\t");
				DNA.put(divided[0], divided[1]);
		}
		
		StdIn.fromFile("data/SARSCoV2-S-gene-CA.txt");
		String codon = StdIn.readLine();
		
		for (int i = 3; i < codon.length(); i += 3)	
			StdOut.println(DNA.get(codon.substring(i-3, i)));
	}
}
