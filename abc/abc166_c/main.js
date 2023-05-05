function solve (n, m, towerHighs, loads) {
    const towerLossCount = [...Array(n)].map(_ => 0)
    for (let i = 0; i < m; i++) {
        const load = loads[i]
        const aHigh = towerHighs[load.a - 1]
        const bHigh = towerHighs[load.b - 1]
        if (aHigh === bHigh) {
            towerLossCount[load.a - 1] ++
            towerLossCount[load.b - 1] ++
        } else if (aHigh > bHigh) {
            towerLossCount[load.b - 1] ++
        } else if (aHigh < bHigh) {
            towerLossCount[load.a - 1] ++
        }
    }
    return towerLossCount.filter(lossCount => lossCount === 0).length

}


function Main(input) {
    input = input.split('\n');
    const [line1, line2, ...others] = input
    const n = Number(line1.split(' ')[0])
    const m = Number(line1.split(' ')[1])
    const towerHighs = line2.split(' ').map(Number)

    const loads = others.map(load => {
        const pointA = load.split(' ')[0]
        const pointB = load.split(' ')[1]
        return {
            a: Number(pointA),
            b: Number(pointB)
        }
    })
    const answer = solve(n, m, towerHighs, loads)
        console.log(answer)
}
Main(require('fs').readFileSync('/dev/stdin', 'utf8'));