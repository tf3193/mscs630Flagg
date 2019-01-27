import java.util.HashMap;
public class Driver_lab1 {

  public static void main(String[] args) {
    private static HashMap<Character, Integer> CYPHERMAP = new HashMap<Character, String>();

  }

  int[] str2int(String plainText){
    int[] encryptedText = new int[plainText.length()];
    int forEachItter = 0;
    for(char c: plainText) {
      encryptedText[forEachItter] = CYPHERMAP.get(Character.toUpperCase(c));
      forEachItter++;
    }
    return encryptedText;
  }

  public static void createMap(){
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
