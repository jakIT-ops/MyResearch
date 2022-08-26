const sailors = [
    {
        name: 'yi hong',
        active: true,
        email: 'yh@yhproductions.io',
    },
    {
        name: 'alex',
        active: true,
        email: '',
    },
    {
        name: 'nathan',
        active: false,
        email: '',
    },
];

const active = sailors.filter(sailor => sailor.active);
const emails = active.map(member => member.email || `${member.name}@wiscsail.io`);
console.log(emails);

