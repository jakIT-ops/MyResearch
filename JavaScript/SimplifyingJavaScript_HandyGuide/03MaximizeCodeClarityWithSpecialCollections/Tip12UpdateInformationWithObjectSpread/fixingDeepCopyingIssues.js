const defaultEmployee = {
    name: {
        first: '',
        last: '',
    },
    years: 0,
};


const employee = {
    ...defaultEmployee,
    name: {
        ...defaultEmployee.name,
    },
};

employee.name.first = 'joe';
console.log("Employee name:");
console.log(employee.name.first);
console.log("Default employee name:");
console.log(defaultEmployee.name.first);
