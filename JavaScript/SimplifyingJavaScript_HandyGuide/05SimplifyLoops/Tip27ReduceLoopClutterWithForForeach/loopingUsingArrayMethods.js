const firms = new Map()
  .set(10, 'Ivie Group')
  .set(23, 'Soundscaping Source')
  .set(31, 'Big 6');


function checkConflicts(firms, isAvailable) {
  const message = [...firms].reduce((availability, firm) => {
    const [id, name] = firm;
    if (!isAvailable(id)) {
      return `${name} is not available`;
    }
    return availability;
  }, 'All firms are available');
  return message;
}

const soundscapeUnavailable = id => id !== 23;
console.log(checkConflicts(firms,soundscapeUnavailable));
