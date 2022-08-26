// fetch a user from github
fetch('api.github.com/user/AlbertoMontalesi').then( res => {
  // return the data in json format
  return res.json();
}).then(res => {
  // if everything went well, print the data
  console.log(res);
}).catch( err => {
  // or print the error
  console.log(err);
})
