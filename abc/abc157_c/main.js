function isOk(num, sc) {
    return Number(num.toString()[sc[0] - 1]) === sc[1]
}


function solve(n, scList) {
    for (let i = 0; i < 1000; i++) {
        if(i.toString().length == n && scList.every(sc => isOk(i, sc))) {
            return i
        }
    }
    return "-1"
}
function Main(input) {
    const rows = input.split('\n');
    const [nm, ...scList] = rows
    const n = Number(nm.split(' ')[0])
    const m = Number(nm.split(' ')[1])
    console.log(solve(n, scList.map(sc => sc.split(' ').map(n => Number(n))).slice(0, m)))
 }
 Main(require('fs').readFileSync('/dev/stdin', 'utf8'));