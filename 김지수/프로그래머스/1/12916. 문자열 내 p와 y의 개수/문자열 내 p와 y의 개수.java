import java.util.*;
class Solution {
    boolean solution(String s) {
        Map<Character, Integer> map = new HashMap<Character, Integer>() {
            {
                put('p', 0);
                put('y', 0);
            }
        };
        
        for (char c : s.toCharArray()) {
            if (c == 'p' || c == 'P') map.put('p', map.get('p') + 1);
            if (c == 'y' || c == 'Y') map.put('y', map.get('y') + 1);
        }
        
        return (map.get('p').equals(map.get('y')));
    }
}