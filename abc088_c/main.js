function solve (c) {
    a1 = c[1][1] === c[1][2] + c[2][1] - c[2][2]
    a2 = c[1][3] === c[1][2] + c[2][3] - c[2][2]
    a3 = c[3][1] === c[2][1] + c[3][2] - c[2][2]
    a4 = c[3][3] === c[3][2] + c[2][3] - c[2][2]
    a5 = c[1][1] === c[1][2] + c[3][1] - c[3][2]
    a6 = c[1][3] === c[1][2] + c[3][3] - c[3][2]
    a7 = c[1][3] === c[1][1] + c[2][3] - c[2][1]
    a8 = c[3][1] === c[2][1] + c[3][3] - c[2][3]
    a9 = c[1][1] === c[1][3] + c[3][1] - c[3][3]
    // console.log([a1,a2,a3,a4,a5,a6,a7,a8,a9])
    if ([a1,a2,a3,a4,a5,a6,a7,a8,a9].every(a=>a)) {
        console.log("Yes")
    } else {
        console.log("No")
    }
} 


function Main(input) {
   input = input.split('\n');
   input = input.map(tmp => [undefined, ...tmp.split(' ').map(n => Number(n))]);
   solve([undefined, ...input])
}
Main(require('fs').readFileSync('/dev/stdin', 'utf8'));
