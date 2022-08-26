const errors = {
    100: 'Invalid name',
    110: 'Name should only contain letters',
    200: 'Invalid color'
};

function isDataValid(data) {
    if (data.length < 10) {
        return errors.100
    }
    return true;
}

console.log(isDataValid("cat"));
