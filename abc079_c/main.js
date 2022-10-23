const toPlus = (n) => n
const toMinus = (n) => -1 * n
const operations = [toPlus, toMinus]
const toOpeStr = (ope) => ope === toPlus ? "+" : "-";
function solve(a,b,c,d) {
    for (let bOpe of operations) {
        for (let cOpe of operations) {
            for (let dOpe of operations) {
                if (a + bOpe(b) + cOpe(c) + dOpe(d) === 7) {
                    console.log(`${a}${toOpeStr(bOpe)}${b}${toOpeStr(cOpe)}${c}${toOpeStr(dOpe)}${d}=7`)
                    return
                }
            }
        }
    }
}
function Main(input) {
   tmp = input.split('\n')[0].split('');
   const a = parseInt(tmp[0], 10);
   const b = parseInt(tmp[1], 10);
   const c = parseInt(tmp[2], 10);
   const d = parseInt(tmp[3], 10);
   solve(a,b,c,d)
}
Main(require('fs').readFileSync('/dev/stdin', 'utf8'))