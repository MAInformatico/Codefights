bool newRoadSystem(bool[][] roadRegister) {
    
            var row = new int[roadRegister.Length];
            var column = new int[roadRegister.Length];

            for (int i = 0; i < roadRegister.Length; i++)
                for (int j = 0; j < roadRegister.Length; j++)
                    if (roadRegister[i][j]){
                        column[i]++;
                        row[j]++;
                    }

            bool check = true;
            for (int i = 0; check && i < roadRegister.Length; i++)
                check = row[i] == column[i];
    
            return check;
}
