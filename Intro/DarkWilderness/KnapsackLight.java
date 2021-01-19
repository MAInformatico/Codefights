int knapsackLight(int value1, int weight1, int value2, int weight2, int maxW) {
   return weight1 + weight2 <= maxW? value1 + value2: value1 > value2 && weight1 <= maxW? value1: weight2 <= maxW? value2: weight1 <= maxW? value1: 0; 
}
