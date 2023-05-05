
function solve(a,b,c,n) {
    let min = Infinity
    for (let ai = 0; ai < 10000; ai++) {
        for (let bi = 0; bi < (10000 - ai); bi++) {
            const aSum = ai * a;
            const bSum = bi * b;
            const cSum = n - aSum - bSum;
            if (cSum >= 0 && cSum % c === 0) {
                const ci = cSum / c;
                const count = ai + bi + ci;
                min = Math.min(count, min)
            }
        }
    }
    console.log(min)
}
function Main(input) {
   input = input.split('\n');
   tmp = input[1].split(' ');
   const n = parseInt(input[0], 10);
   const a = parseInt(tmp[0], 10);
   const b = parseInt(tmp[1], 10);
   const c = parseInt(tmp[2], 10);
   solve(a,b,c,n)
}
Main(require('fs').readFileSync('/dev/stdin', 'utf8'));