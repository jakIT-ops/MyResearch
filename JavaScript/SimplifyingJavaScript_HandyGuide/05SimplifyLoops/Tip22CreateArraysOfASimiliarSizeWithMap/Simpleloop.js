const band = [
    {
        name: 'corbett',
        instrument: 'guitar',
    },
    {
        name: 'evan',
        instrument: 'guitar',
    },
    {
        name: 'sean',
        instrument: 'bass',
    },
    {
        name: 'brett',
        instrument: 'drums',
    },
];

const instruments = [];

for (let i = 0; i < band.length; i++) {
    const instrument = band[i].instrument;
    instruments.push(instrument);
}
console.log(instruments);
