function roundToDecimalPlace(number, decimalPlaces) {
    const round = 10 ** decimalPlaces;
    return Math.round(number * round) / round;
}

function convertWeight(weight, ounces = 0, roundTo = 2) {
    const total = weight + (ounces / 16);
    const conversion = total / 2.2;
    return roundToDecimalPlace(conversion, roundTo);
}
console.log(convertWeight(44, undefined, 2));
console.log(convertWeight(44, 11, 0));
