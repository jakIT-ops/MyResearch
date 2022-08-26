function getBirds(...states) {
  return ['meadowlark', 'robin', 'roadrunner'];
}

const zip = (...left) => (...right) => {
    return left.map((item, i) => [item, right[i]]);
};

const birds = getBirds('kansas', 'wisconsin', 'new mexico');
console.log(zip('kansas', 'wisconsin', 'new mexico')(...birds));
