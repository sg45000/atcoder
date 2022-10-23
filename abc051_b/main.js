function solve(k ,s) {
    let ans = 0
    for (let x = 0; x <= k; x++) {
        for(let y = 0; y <= k; y++) {
            const z = s - x - y
            if(0 <= z && z <= k) {
                ans += 1
            }
        }
    }
    console.log(ans)
}
function Main(input) {
   input = input.split(' ');
   solve(Number(input[0]), Number(input[1]))
}
Main(require('fs').readFileSync('/dev/stdin', 'utf8'));