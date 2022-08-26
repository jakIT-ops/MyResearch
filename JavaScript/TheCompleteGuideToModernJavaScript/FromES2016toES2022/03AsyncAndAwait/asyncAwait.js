function walk(amount) {
  return new Promise((resolve,reject) => {
    if (amount < 500) {
      reject ("the value is too small");
    }
    setTimeout(() => resolve(`you walked for ${amount}ms`),amount);
  });
}

// create an async function
async function go() {
  // use the keyword `await` to wait for the response
  const res = await walk(500);
  console.log(res);
  const res2 = await walk(900);
  console.log(res2);
  const res3 = await walk(600);
  console.log(res3);
  const res4 = await walk(700);
  console.log(res4);
  const res5 = await walk(400);
  console.log(res5);
  console.log("finished");
}

go();

// you walked for 500ms 
// you walked for 900ms 
// you walked for 600ms 
// you walked for 700ms 
// uncaught exception: the value is too small
