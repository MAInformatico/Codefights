function constructSubmatrix(matrix, rowsToDelete, columnsToDelete) {
	var result = [], newRow = [], newColumn = [];
    
	for (var i = 0; i < matrix.length; i++) 
		newRow.push(true);
	
	for (var i = 0; i < matrix[0].length; i++) 
		newColumn.push(true);
	
	for (var i = 0; i < rowsToDelete.length; i++) 
		newRow[rowsToDelete[i]] = false;
	
	for (var i = 0; i < columnsToDelete.length; i++) 
		newColumn[columnsToDelete[i]] = false;
	
	for (var i = 0; i < matrix.length; i++) {
		if (newRow[i]) {
			result.push([]);
			for (var j = 0; j < matrix[0].length; j++) {
				if (newColumn[j]) 
					result[result.length - 1].push(matrix[i][j]);
				
			}
		}
	}
	return result;
}
