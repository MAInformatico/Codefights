int largestNumber(int n) {
int result=9;
for(int i=1;i<n;i++){
        result*=10;
        result+=9;
    }
return result;
}
