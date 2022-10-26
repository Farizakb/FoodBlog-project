let userDetail = JSON.parse(localStorage.getItem('User-detail')) 

window.addEventListener('load', async function(){
    if(!userDetail || !userDetail.access){
        window.location = 'login.html'
    }

    let response = await fetch('http://localhost:8000/api/catagories/');
    categories = await response.json();
    // console.log(categories);
    for(cat of categories) {
        document.querySelector('[name="catagory"]').innerHTML += `
            <option value="${cat.id}">${cat.title}</option>
  
        `
    }
})

let form = document.querySelector('#blog-form');

form.addEventListener('submit', async function(event){
    event.preventDefault();
    console.log(event.target,'here')

    let Data = new FormData(form)

    let response = await fetch('http://localhost:8000/api/recipes/',{
        method: 'POST',
        headers:{
            // 'Accept': '*/*',
            'Authorization':`Bearer ${userDetail.access}`
            },
        body:Data
    });
     
    
    if(response.ok){
        window.location = '/'

    }
    else{
        alert("something went wrong")
    }
});

