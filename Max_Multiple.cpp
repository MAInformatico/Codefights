int maxMultiple(int divisor, int bound) {
    int result=bound;
    while(result>0 && result<=bound && result%divisor!=0)
            result--;    
    
    return result;
}