const validator = {
    message: 'is invalid.',
    setInvalidMessage(field) {
        return `${field} ${this.message}`;
    },
};
console.log(validator.setInvalidMessage('city'));
