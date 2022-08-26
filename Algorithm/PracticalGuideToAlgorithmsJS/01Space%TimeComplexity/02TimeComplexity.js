var countChars = function(str) {
    var count = 0;

    for(var i = 0; i < str.length; i++) {
        count++;
    }
    // retunr str.length;
    return count;
};

console.log(countChars("dance"));
console.log(countChars("walkreallyfast"));

var myList = ['hello', 'hola'];
myList.push('bonjour');
myList.unshift()

// calculate the time complexity for the
// native methods aboce (separately)