int equalPairOfBits(int n, int m) {
  return Integer.lowestOneBit(~(n^m));
}
