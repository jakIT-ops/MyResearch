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

const findByLibrary = library => instructor => {
    return instructor.libraries.includes(library);
};

const librarian = instructors.find(findByLibrary('MERIT'));
console.log(librarian);
