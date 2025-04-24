// How to Use Request and Fetch API

// fetch() – Native in browsers (and available in Node via libraries)
fetch('https://forever-backend-hazel.vercel.app/api/product/list')
  .then(res => res.json())
  .then(data => {
    console.log(data);
  })
  .catch(err => console.error(err));


// axios (a great alternative)
/*const axios = require('axios');

axios.get('https://forever-backend-hazel.vercel.app/api/product/list')
  .then(response => console.log(response.data))
  .catch(err => console.error(err));*/


// Using async/await (cleaner & readable)
/*async function getData() {
  try {
    const res = await fetch('https://forever-backend-hazel.vercel.app/api/product/list');
    const data = await res.json();
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}
getData();*/

