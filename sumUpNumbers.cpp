int sumUpNumbers(std::string inputString) {
    std::vector<string> numbers;
    for(int i=0;i<inputString.size();i++){
        if('0'<=inputString[i]&&inputString[i]<='9'){
            std::string newnumber="";
            while('0'<=inputString[i]&&inputString[i]<='9'){
                newnumber+=inputString[i];
                i++;
            }
            numbers.push_back(newnumber);
        }
    }
    int sum=0;
    for(string str:numbers){
        sum+=atoi(str.c_str());
    }
    return sum;
}
