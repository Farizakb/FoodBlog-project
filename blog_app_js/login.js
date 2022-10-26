let form = document.querySelector('#login-form');

form.addEventListener('submit', async function(event){
    event.preventDefault();
    console.log(event.target,'here')

    let Data = {
        'username': form.username.value,
        'password': form.password.value
    }

    let response = await fetch('http://localhost:8000/api/token/',{
        method: 'POST',
        headers:{
            "Content-Type": "application/json",
            },
        body:JSON.stringify(Data)
    });
     
    
    if(response.ok){
        let data = await response.json()
        console.log(data)
        localStorage.setItem('User-detail', JSON.stringify(data));

    }
    else{
        alert("something went wrong")
    }
});

