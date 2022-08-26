const firms = {
    '10': 'Ivie Group',
    '23': 'Soundscaping Source',
    '31': 'Big 6',
};

function checkConflicts(firms, isAvailable) {
    for (const id in firms) {
        if (!isAvailable(parseInt(id, 10))) {
            return `${firms[id]} is not available`;
        }
    }
    return 'All firms are available';
}

const alwaysTrue = id => id;
const soundscapeUnavailable = id => id !== 23;
console.log(checkConflicts(firms,alwaysTrue));
console.log(checkConflicts(firms,soundscapeUnavailable));
