const instructors = [
    {
        name: 'Jim',
        libraries: ['MERIT'],
    },
    {
        name: 'Sarah',
        libraries: ['Memorial', 'SLIS'],
    },
    {
        name: 'Eliot',
        libraries: ['College Library'],
    },
];

const librarian = instructors.find(instructor => {
    return instructor.libraries.includes('Memorial');
});

console.log(librarian);
