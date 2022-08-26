function getTimePermissions({ title }) {
    if (title === 'manager') {
        return ['time', 'overtimeAuthorization', 'pay'];
    }
    if (title === 'supervisor') {
        return ['time', 'overtimeAuthorization'];
    }
    return ['time'];
}
const permissions = getTimePermissions({ title: 'employee' });
console.log(permissions);
