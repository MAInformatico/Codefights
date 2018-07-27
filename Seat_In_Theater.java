int seatsInTheater(int nCols, int nRows, int col, int row) {
    col--;
    int tRows=nRows-row;
    int tCols=nCols-col;
    int result=tRows*tCols;
    return result;
}
