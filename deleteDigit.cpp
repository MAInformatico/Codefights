int deleteDigit(int n) {
    int result = 0;
    for(int i=1;i <= n; i*=10){
        int aux = n%i + ((n/i)/10)*i;
        result = max(result,aux);
    }
    return result;
}
