std::vector<int> alternatingSums(std::vector<int> a) {
    vector<int> result;
    int p=0;
    int ip=0;
    for(int i=0; i<a.size();i++){
        if(i%2==0) p+=a[i];
        if(i%2!=0) ip+=a[i];
    }
    result.push_back(p);
    result.push_back(ip);
    return result;
}
