int candies(int n, int m) {
    if(m%n==0){
        return m;
    }        
    else{
        while(m%n!=0){
            m--;
        }
        return m;
    }
}