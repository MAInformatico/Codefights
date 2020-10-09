function lineUp(commands) {
    let result = 0;
    let alu1Pos = 0;
    let alu1Direction = ['N', 'E', 'S', 'W']
    let alu2Pos = 0;
    let alu2Direction = ['N', 'W', 'S', 'E']
    for(let i = 0; i < commands.length; i++) {
        if(commands[i] == 'R'){
            alu1Pos = (alu1Pos + 1) % 4;
            alu2Pos = (alu2Pos + 1) % 4;
        } else if (commands[i] == 'L') {
            alu1Pos == 0 ? alu1Pos = 3 : alu1Pos -= 1;
            alu2Pos == 0 ? alu2Pos = 3 : alu2Pos -= 1;
        } else if (commands[i] == 'A') {
            alu1Pos = (alu1Pos + 2) % 4;
            alu2Pos = (alu2Pos + 2) % 4;
        }
        alu1Direction[alu1Pos] == alu2Direction[alu2Pos] ? result++ : null;
    }         
    return result;
}
