function comfortableNumbers(l, r) {
    
    function s(x) {
        return String(x).split('').map(Number).reduce((a, b) => a + b);
    }
    
    var list = [];
    for (let i = l; i <= r; i++) {
        for (let j = i + 1; j <= Math.min(r, i + s(i)); j++) {
            if (i === j)
                continue;
            if (i >= j - s(j) && i <= j + s(j)) {
                list.push([i, j]);
            }
        }
    }
    return list.filter((element, index, array) => index === array.findIndex(
        function (fl) {
            return element[0] === fl[0] && element[1] === fl[1];
        }
    )).length;
}
