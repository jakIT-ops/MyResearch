const firms = new Map()
    .set(10, 'Ivie Group')
    .set(23, 'Soundscaping Source')
    .set(31, 'Big 6');

function checkConflicts(firms, isAvailable) {
    const entries = [...firms];
    for (let i = 0; i < entries.length; i++) {
        const [id, name] = entries[i];
        if (!isAvailable(id)) {
            return `${name} is not available`;
        }
    }
    return 'All firms are available';
}

const soundscapeUnavailable = id => id !== 23;
console.log(checkConflicts(firms,soundscapeUnavailable));
