const game1 = {
    player: 'Jim Jonas',
    hits: 2,
    runs: 1,
    errors: 0,
};

const game2 = {
    player: 'Jim Jonas',
    hits: 3,
    runs: 0,
    errors: 1,
};

const total = {};
const stats = Object.keys(game1);

for (let i = 0; i < stats.length; i++) {
    const stat = stats[i];
    if (stat !== 'player') {
        total[stat] = game1[stat] + game2[stat];
    }
}
console.log(total);
