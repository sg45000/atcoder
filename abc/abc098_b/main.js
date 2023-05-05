function solve(n,s) {
    let max = 0;
    let x = {}
    let y = {}
    // 文字をキー、文字の個数を値にしたオブジェクト作成
    for (let char of s.split("")) {
        y[char] = y.hasOwnProperty(char) ? y[char] + 1 : 1;
    }
    // 先頭から一文字ずつyからxに移動していき、2つの文字列への分割を再現
    for (let i = 0; i < n; i++) {
        const char = s[i];
        x[char] = x.hasOwnProperty(char) ? x[char] + 1 : 1;
        y[char] = y[char] - 1
        if (y[char] === 0) {
            delete y[char]
        }

        // 「X と Y のどちらにも含まれている文字」の個数を計算
        let bothExistCount = 0;
        for (const key of Object.keys(x)) {
            if(y.hasOwnProperty(key)) {
                bothExistCount += 1
            }
        }
        max = Math.max(bothExistCount, max)
    }
    console.log(max)
}

function Main(input) {
   input = input.split('\n');
   n = input[0].split(' ')[0];
   s = input[1].split(' ')[0];
   solve(n,s)
}
Main(require('fs').readFileSync('/dev/stdin', 'utf8'));
