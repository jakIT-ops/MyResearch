function validateCharacterCount(max, items) {
    return items.every(item => item.length < max);
}
console.log(validateCharacterCount(10, ['Hobbs', 'Eagles']));
