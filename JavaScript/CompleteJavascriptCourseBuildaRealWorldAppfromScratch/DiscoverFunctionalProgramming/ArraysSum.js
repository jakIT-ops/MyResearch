var inputs = [[2, 4], [11], [3, 5, 7]];

function findSum(array) {
    var sum = 0;
    for(x of array){
  		for(y of x){
      			sum += y;
      	}
  	}
	console.log(sum);
}
findSum(inputs);
