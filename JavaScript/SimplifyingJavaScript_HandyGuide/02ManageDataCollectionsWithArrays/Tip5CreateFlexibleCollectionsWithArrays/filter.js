const staff = [
    {
        name: 'Wesley',
        position: 'musician',
    },
    {
        name: 'Davis',
        position: 'engineer',
    },
];

function getMusicians(staff) {
    return staff.filter(member => member.position === 'musician');
}

console.log(getMusicians(staff));
