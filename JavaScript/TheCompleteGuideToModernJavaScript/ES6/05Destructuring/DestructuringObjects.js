var person  = {
  first: "Alberto",
  last: "Montalesi"
}

var first = person.first;
var last = person.last;
console.log(first,last);


const person = {
  first: "Alberto",
  last: "Montalesi"
}

const { first, last } = person;
console.log(first,last);


const person = {
  name: "Alberto",
  last: "Montalesi",
  links:{
    social: {
      facebook: "https://www.facebook.com/alberto.montalesi",
    },
    website: "http://albertomontalesi.github.io/"
  }
}

const { facebook:fb } = person.links.social;
// it will look for the property person.links.social.facebook and name the variable fb
console.log(fb); // https://www.facebook.com/alberto.montalesi
console.log(facebook); //ReferenceError: facebook is not defined

