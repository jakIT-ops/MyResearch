//
const greeting = name => `hello ${name}`;  


//
const oldFunction = function(name){
  return `hello ${name}`
}

const arrowFunction = name => `hello ${name}`;   

//  
const arrowFunction = (name) => {
  return `hello ${name}`;
}

//
const race = "100m dash";
const runners = [ "Usain Bolt", "Justin Gatlin", "Asafa Powell" ];

const results = runners.map((runner, i) =>  ({ name: runner, race, place: i + 1}));

console.log(results);
