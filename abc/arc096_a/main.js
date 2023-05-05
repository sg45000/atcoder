function shouldUseAbPizza(aPrice, bPrice, cPrice) {
   return (aPrice + bPrice) >= (cPrice * 2)
}

function solve(aPrice, bPrice, cPrice, x, y) {
    if (shouldUseAbPizza(aPrice, bPrice, cPrice)) {
        let aUnitPrice = aPrice <= cPrice * 2 ? aPrice : cPrice * 2
        let bUnitPrice = bPrice <= cPrice * 2 ? bPrice : cPrice * 2

        const numOfC = Math.min(x, y) * 2
        let priceSum = x > y ? (x - y) * aUnitPrice : (y - x) * bUnitPrice
        priceSum += numOfC * cPrice
        console.log(priceSum)
    } else {
        console.log(aPrice * x + bPrice * y)
    }
}

function Main(input) {
   input = input.split(' ');
   input = input.map(m => Number(m))
   solve(input[0], input[1],input[2],input[3],input[4])
}
Main(require('fs').readFileSync('/dev/stdin', 'utf8'));
// Main("1500 2000 1900 3 2")