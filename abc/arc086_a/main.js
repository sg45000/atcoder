function solve (n,k,list) {
    let countList = [0]
    for (let i = 1; i <= n; i++) {
        countList[i] = 0
    }
    for(const ball of list) {
        countList[ball] ++
    }
    countList = countList.filter(c => c > 0).sort()
    let answer = 0
    for(let i = 0; i < countList.length; i++) {
        if(countList.slice(i).length <= k) {
            return answer
        }
        answer += countList[i]
    }
}


function Main(input) {
   input = input.split('\n');
   const [n, k] = input[0].split(' ');
   const list = input[1].split(' ');
   console.log(solve(Number(n), Number(k), list.map(Number)))
}
Main(require('fs').readFileSync('/dev/stdin', 'utf8'));
