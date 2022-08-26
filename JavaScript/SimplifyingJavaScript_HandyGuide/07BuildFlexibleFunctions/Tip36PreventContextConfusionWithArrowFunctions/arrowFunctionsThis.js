const validator = {
    message: 'is invalid.',
    setInvalidMessages(...fields) {
        return fields.map(field => {
            return `${field} ${this.message}`;
        });
    },
};
console.log(validator.setInvalidMessages('city'));
