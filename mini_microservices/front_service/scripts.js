let postList = document.querySelector('#posts');

document.addEventListener('DOMContentLoaded', function() {
    getPost();

});


async function getPost(){
    let res = await fetch('http://127.0.0.1:5002/api/queries');
    let posts = await res.json();
    for (const post of posts) {
         await renderPost(post);
        
    }


}


async function renderPost(post){
    let comments = post.comments || []


    //await getComments(post_id = post.id);
    // let listComment = ''
    // for (const comment of comments) {
    //     listComment += `<li>${comment.content}</li>`
    // }

    postList.innerHTML += `
    <div class="col-5 m-5">
                <div class="card p-4">
                    <h3>${post.title}</h3>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium neque quasi repudiandae asperiores eum enim maxime officia fugiat veritatis dolor eaque ad commodi rem ab, eos, adipisci vero provident autem.</p>

                    <div class="comments">
                        <ul>
                            ${comments.map(comment => `<li>${comment.content}</li>`).join("")}
                        </ul>


                        <form post-id=${post.id} class="comment_from" action="" method="post">
                            <div class="form-group mb-3">
                                <label for="">Comment</label>
                                <input class="form-control" type="text" name="comment">
                            </div>
                            <input class="btn btn-primary" type="submit" value="Yarat">
                        </form>

                    </div>
                </div>
            </div>
    `
}


// async function getComments(post_id){
//     let res = await fetch(`http://127.0.0.1:5001/posts/${post_id}/comments`);
//     let comments = await res.json()
//     return comments
// }








let createPost = document.querySelector('#blog_form');

createPost.addEventListener('submit', async function(event){
    event.preventDefault();
    let postData = {
        'title': createPost.title.value
    };
 
    let res = await fetch('http://127.0.0.1:5000/api/posts',{
        method: 'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(postData),

    });
    let post = await res.json()
    renderPost(post)

})



document.addEventListener('submit',async function(event){
    event.preventDefault();
    let commentForm = event.target;
    if (commentForm.classList.contains('comment_from')){

        let postId = commentForm.getAttribute('post-id');
        let postData = {
            'content': commentForm.comment.value
        };
     
        let res = await fetch(`http://127.0.0.1:5001/api/posts/${postId}/comments`,{
            method: 'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify(postData),
    
        });
        let comment = await res.json()
        if (res.ok){
            commentForm.previousSibling.previousSibling.innerHTML += `<li>${comment.content}</li>` 
        }
        else{
            alert('Something went wrong')
        }
        console.log(comment);
    }
});




// function assignComment(){
//     let commentForms = document.querySelectorAll('.comment_from');

//     commentForms.forEach((commentForm)=>{
//         commentForm.addEventListener('submit',function(event){
//             event.preventDefault();
//             alert("worked")
//         })
//     })
//     console.log('Assigned to',commentForms.length,'form')
// }
// createComment.addEventListener('submit', async (event)=>{
//     event.preventDefault();
//     let postData={
//         'comment':createComment.comment.value
//     };
//     let res = await fetch(`http://127.0.0.1:5001/posts/${post_id}/comments`)
// })