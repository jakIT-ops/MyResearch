const team = [
    'Michelle B',
    'Dave L',
    'Dave C',
    'Courtney B',
    'Davina M',
];

const daves = [];

for (let i = 0; i < team.length; i++) {
    if (team[i].match(/Dav/)) {
        daves.push(team[i]);
    }
}
console.log(daves);
