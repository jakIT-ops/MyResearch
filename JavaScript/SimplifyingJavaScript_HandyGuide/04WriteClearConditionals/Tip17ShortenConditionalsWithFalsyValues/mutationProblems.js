const employee = {
    name: 'Eric',
    equipmentTraining: true,
};

function listCerts(employee) {
    if (employee.equipmentTraining) {
        employee.certificates = ['Equipment'];
        // Mutation!
        delete employee.equipmentTraining;
    }
    // More code.
}

function checkAuthorization(){
    if (!employee.equipmentTraining) {
        return 'Not authorized to operate machinery';
    }
    return 'Hello, ${employee.name}'
}

listCerts(employee);
console.log(employee)
console.log(checkAuthorization());
