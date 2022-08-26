const employee = {
    name: 'Eric',
    equipmentTraining: true,
};


function checkAuthorization() {
    if (employee.equipmentTraining !== true) {
        return 'Not authorized to operate machinery';
    }
    return `Hello, ${employee.name}`
}

employee.equipmentTraining = 'Not Trained';
console.log(checkAuthorization());
