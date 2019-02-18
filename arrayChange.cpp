int arrayChange(std::vector<int> inputArray) {
    int sum=0;
    for(int i=0;i<inputArray.size()-1;++i){
        if(inputArray[i]>=inputArray[i+1]){
            sum+= abs(inputArray[i+1]-inputArray[i])+1;
            inputArray[i+1]+= abs(inputArray[i+1]-inputArray[i])+1;        
        }
    }
    return sum;
}
