function solve(n, p, q, list) {
    let cnt = 0
    for(let i = 0; i < n; i++) {
        for(let j = 0; j < i; j++) {
            for(let k = 0; k < j; k++) {
                for(let l = 0; l < k; l++) {
                    for(let m = 0; m < l; m++) {
                        if(list[i] * list[j] % p * list[k] % p * list[l] % p * list[m] % p === q) {
                            cnt++
                        }
                    }
                }
            }
        }
    }
    console.log(cnt)
}

function Main(input) {
   input = input.split('\n');
   r1 = input[0].split(' ');
   r2 = input[1].split(' ');
   solve(Number(r1[0]), Number(r1[1]), Number(r1[2]), r2.map(m => Number(m)))
}
// Main(require('fs').readFileSync('/dev/stdin', 'utf8'));
Main(`10 1 0
0 0 0 0 0 0 0 0 0 0
`)
