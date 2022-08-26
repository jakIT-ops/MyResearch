
const runners = ["Tom", "Paul", "Mark", "Luke"];
const [first,second,...losers] = runners;

console.log(...losers);
// Mark Luke
