function solve (n) {
    let max = 1;
    for (let b = 1; b < n; b++) {
        for (let p= 2; p < 10; p++) {
            const a = b ** p;
            if (n < a) {
                break;
            }
            if (max < a) {
                max = a;
            }
        }
    }
    return max
}
function Main(input) {
   const n = input.split('\n')[0];
   console.log(solve(Number(n))) 
}
Main(require('fs').readFileSync('/dev/stdin', 'utf8'));
// console.log(solve(999))
