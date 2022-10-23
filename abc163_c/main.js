function solve(n, bossIds) {
    const numOfAssistantGraph = [...Array(n)].map(_ => 0)
    for (const bossId of bossIds) {
        const staffIndex = bossId - 1
        numOfAssistantGraph[staffIndex]++
    }
    return numOfAssistantGraph
}


function Main(input) {
    input = input.split('\n');
    const n = Number(input[0])
    const bossIds = input[1].split(' ').map(Number)
    const graph = solve(n, bossIds)
    for(const a of graph) {
        console.log(a)
    }
}
Main(require('fs').readFileSync('/dev/stdin', 'utf8'));