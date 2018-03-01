int commonCharacterCount(String s1, String s2) {
  int count = 0;  
  char[] as= s1.toCharArray();
  char[] bs= s2.toCharArray();
  
  int[] countAs = new int[126];
  int[] countBs = new int[126];
  
  for (int i = 0; i < as.length; i++)  countAs[(int)as[i]]++;
  
  for (int i = 0; i < bs.length; i++)  countBs[(int)bs[i]]++;
  
  for (int i = 0; i < countBs.length; i++) count += Math.min(countAs[i], countBs[i]);
  
  return count;
}
