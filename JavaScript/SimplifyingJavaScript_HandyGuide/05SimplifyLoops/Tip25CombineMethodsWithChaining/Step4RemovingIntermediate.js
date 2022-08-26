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
sailors
.filter(sailor => sailor.active)
.map(sailor => sailor.email || `${sailor.name}@wiscsail.io`)
.forEach(sailor => sendEmail(sailor));
