//Luis Solorzano
package symboltable;

import DataStructures2.AVLTreeST;
import DataStructures2.StdIn;
import DataStructures2.StdOut;

public class MultisequenceCodonFrequencies {
	public static void main(String[] args) {
		AVLTreeST<String, AVLTreeST<String, Integer>> frequencies = new AVLTreeST<>();
		AVLTreeST<String, Integer> textLengths = new AVLTreeST<>();
		
		String[] filenames = {"data/SARSCoV2-S-gene-CA.txt", "data/SARSCoV2-S-gene-WH.txt", "data/SARSCoV2-S-gene-IL.txt"};
		
		for (String filename: filenames) {
			StdIn.fromFile(filename);
			frequencies.put(filename, new AVLTreeST<String, Integer>());
			String text = StdIn.readAll();
			textLengths.put(filename, text.length());
			
			for (int i = 3; i < text.length(); i += 3) {
				String codon = text.substring(i - 3, i);
				Integer frequency = frequencies.get(filename).get(codon);
				if (frequency == null) 
					frequency = 0;
				frequencies.get(filename).put(codon, frequency+1);
			}
		}
		
		String[] leucineCodon = {"ctt", "ctc", "cta", "ctg", "tta", "ttg"};
		for (String leucine: leucineCodon) {
			StdOut.println("Frequencies for '" + leucine + "'");
			for (String filename: filenames) {
				Integer frequency = frequencies.get(filename).get(leucine);
				double numOfCodons = textLengths.get(filename) / 3;
				double percentage = 100.0 * frequency / numOfCodons;
				StdOut.printf("%-25s\t%6.2f\n", filename, percentage);
			}
		}
	}
}
