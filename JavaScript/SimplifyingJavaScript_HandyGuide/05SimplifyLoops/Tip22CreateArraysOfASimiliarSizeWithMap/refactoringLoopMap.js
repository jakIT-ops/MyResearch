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

function getInstrument(member) {
    return member.instrument;
}

for (let i = 0; i < band.length; i++) {
    instruments.push(getInstrument(band[i]));
}

console.log(instruments);
