async function asyncFunc() {

  try {
    let response = await fetch('http:your-url');
    } catch(err) {
        console.log(err);
      }
}

asyncFunc();
// TypeError: failed to fetch
