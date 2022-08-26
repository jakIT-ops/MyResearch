const capitalize = name => {
    return name[0].toUpperCase() + name.slice(1);
};

const formatUser = name => `${capitalize(name)} is logged in.`;

console.log(formatUser('joe'));
