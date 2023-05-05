
function solve(cps, lrs) {
    // クラスそれぞれの累積和を作る
    const class1PrefixSums = cps.reduce((acc, cp) => cp[0] === 1 ? [...acc, acc[acc.length - 1] + cp[1]] : [...acc, acc[acc.length - 1]], [0])
    const class2PrefixSums = cps.reduce((acc, cp) => cp[0] === 2 ? [...acc, acc[acc.length - 1] + cp[1]] : [...acc, acc[acc.length - 1]], [0])
    for (const lr of lrs) {
        const [l, r] = lr
        // クエリに応える
        const answer1 = class1PrefixSums[r] - class1PrefixSums[l - 1]
        const answer2 = class2PrefixSums[r] - class2PrefixSums[l - 1]
        console.log(`${answer1} ${answer2}`)

    }
}

function Main(input) {
    const lines = input.split('\n');
    const n = Number(lines[0]);
    const cps = []
    for (let i = 1; i <= n; i++) {
        const a = lines[i].split(' ').map(Number);
        cps.push(a)
    }
    const q = Number(lines[n+1]);
    const lrs = []
    for (let i = n + 2; i <= n + 1 + q; i++) {
        const a = lines[i].split(' ').map(Number);
        lrs.push(a)
    }
    solve(cps, lrs)
 }
 Main(require('fs').readFileSync('/dev/stdin', 'utf8'));