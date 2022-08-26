const defaultEmployee = {
    name: {
        first: '',
        last: '',
    },
    years: 0,
};

const employee = Object.assign(
    {},
    defaultEmployee,
    {
        name: Object.assign({}, defaultEmployee.name),
    },
);

employee.name.first = 'Joe';
console.log("Employee:");
console.log(employee);
console.log("\n");
console.log("Default employee:");
console.log(defaultEmployee);
