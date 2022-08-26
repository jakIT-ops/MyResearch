const myPromise = new Promise((resolve, reject) => {
  resolve("The value we get from the promise");
});

myPromise.then(
  data => {
    console.log(data);
  });
// The value we get from the promise
