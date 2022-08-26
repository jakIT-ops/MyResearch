const myPromise = new Promise((resolve,reject) => {
  resolve();

})
myPromise
  .then(result => {
    console.log('still working');
  })
  .catch(error => {
    console.log('there was an error');
  })
  .finally(()=> {
    console.log('Done!');
  })
