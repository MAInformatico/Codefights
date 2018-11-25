boolean reachNextLevel(int experience, int threshold, int reward) {    
    int result=(threshold-experience)-reward;
    if(result<=0)
        return true;
    else
        return false;    
}
