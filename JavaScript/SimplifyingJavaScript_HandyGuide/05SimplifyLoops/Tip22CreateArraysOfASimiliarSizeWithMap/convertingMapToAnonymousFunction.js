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


const instruments = band.map(member => member.instrument);
console.log(instruments);
