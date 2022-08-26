const capitalize = name => {
    return name[0].toUpperCase() + name.slice(1);
};

function applyCustomGreeting(name, callback) {
  return callback(capitalize(name));
}

const greeting = applyCustomGreeting('mark', name => `Oh, hi ${name}!`);
console.log(greeting);
