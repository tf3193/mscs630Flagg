
/**
 * file:Driver_lab1.java author: Troy Flagg course: MSCS630 assignment: lab 1
 * due date: January 27, 2018 version: 1
 *
 * This file contains the driver for lab1 which converts letters to numbers
 */
import java.io.IOException;
import java.util.HashMap;

public class Driver_lab1 {

  //This will hold the cypher map of alpha chars to numbers
  private static final HashMap<Character, Integer> CYPHERMAP = new HashMap<>();

  public static void main(String[] args) throws IOException {
    int numberOfLines = args.length;
    //Ensure we are passed input
    if (numberOfLines != 0) {
      createMap();
      //for each line that is passed in run str2int
      for (int i = 0; i < numberOfLines; i++) {
        int[] encryptedLine;
        encryptedLine = str2int(args[i]);
        //Print out the line, this could be handled in str2int for efficency sake
        for (int j = 0; j < encryptedLine.length; j++) {
          int LENGTHTOADDSPACES = encryptedLine.length - 1;
          if (j != LENGTHTOADDSPACES) {
            System.out.print(encryptedLine[j] + " ");
          } else {
            System.out.println(encryptedLine[j]);
          }
        }
      }
    }

  }

  /**
   * A method to convert a string to integers
   *
   * @param plainText a string that we will encrypt
   * @return an array of integers based on the string
   */
  public static int[] str2int(String plainText) {
    int[] encryptedText = new int[plainText.length()];
    for (int i = 0; i < plainText.length(); i++) {
      encryptedText[i] = CYPHERMAP.get(
        Character.toUpperCase(plainText.charAt(i)));
    }
    return encryptedText;
  }

  /**
   * Initalize the static CYPHERMAP
   */
  public static void createMap() {
    CYPHERMAP.put('A', 0);
    CYPHERMAP.put('B', 1);
    CYPHERMAP.put('C', 2);
    CYPHERMAP.put('D', 3);
    CYPHERMAP.put('E', 4);
    CYPHERMAP.put('F', 5);
    CYPHERMAP.put('G', 6);
    CYPHERMAP.put('H', 7);
    CYPHERMAP.put('I', 8);
    CYPHERMAP.put('J', 9);
    CYPHERMAP.put('K', 10);
    CYPHERMAP.put('L', 11);
    CYPHERMAP.put('M', 12);
    CYPHERMAP.put('N', 13);
    CYPHERMAP.put('O', 14);
    CYPHERMAP.put('P', 15);
    CYPHERMAP.put('Q', 16);
    CYPHERMAP.put('R', 17);
    CYPHERMAP.put('S', 18);
    CYPHERMAP.put('T', 19);
    CYPHERMAP.put('U', 20);
    CYPHERMAP.put('V', 21);
    CYPHERMAP.put('W', 22);
    CYPHERMAP.put('X', 23);
    CYPHERMAP.put('Y', 24);
    CYPHERMAP.put('Z', 25);
    CYPHERMAP.put(' ', 26);
  }
}
