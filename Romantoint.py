class Solution {
    public int romanToInt(String s) {
        Map<Character,Integer> map = new HashMap<>();
        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);
        int len = s.length();
        int sum=map.get(s.charAt(len-1));
        System.out.println("initial:" + sum);
        int i =len-2;
        while(i>=0){
            if (map.get(s.charAt(i)) < map.get(s.charAt(i + 1))) {
                sum -= map.get(s.charAt(i));
                    i-=1;
            } else {
                sum += map.get(s.charAt(i));
                    i-=1;;
            }
        }
        return sum;
    }
}
