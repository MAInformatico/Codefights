int[] sortByHeight(int[] a) {
int[] result = new int[a.Length];
    Array.Copy(a,0,result,0,a.Length);
    Array.Sort(a);
    int aux=a.Where(i => i==-1).Count();
    for(int i=0;i<a.Length;i++){
        if(result[i]!=-1){
            result[i]=a[aux];
            aux++;
        }
    }
    return result;
}
