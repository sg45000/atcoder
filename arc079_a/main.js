function solve(n, m, ships) {
    const fromStartMidpoints = []
    const toTerminalMidpoints = []
    for (const ship of ships) {
        if(ship.a === 1) {
            fromStartMidpoints.push(ship.b)
        }
        if (ship.b === n) {
            toTerminalMidpoints.push(ship.a)
        }
    }
    return new Set(fromStartMidpoints.concat(toTerminalMidpoints)).size !== fromStartMidpoints.length + toTerminalMidpoints.length
}


function Main(input) {
    input = input.split('\n');
    const [line1, ...others] = input
    const n = Number(line1.split(' ')[0])
    const m = Number(line1.split(' ')[1])

    const ships = others.map(ship => {
        const pointA = ship.split(' ')[0]
        const pointB = ship.split(' ')[1]
        return {
            a: Number(pointA),
            b: Number(pointB)
        }
    })
    const answer = solve(n, m, ships)
        console.log(answer ? 'POSSIBLE': 'IMPOSSIBLE')
}
Main(require('fs').readFileSync('/dev/stdin', 'utf8'))