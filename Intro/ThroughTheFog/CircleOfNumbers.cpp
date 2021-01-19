int circleOfNumbers(int n, int firstNumber) {
    int result=0;
    result=firstNumber+(n/2);
    if(result>=n){
        result-=n;
        return result;
    }
    else{
        return result;    
    }
}