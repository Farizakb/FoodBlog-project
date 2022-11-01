import requests
from app import app
from flask import jsonify,request, render_template

comments = [
    {
        'id': 1,
        'content': 'Comment',
        'blog_id': 1
    },
    {
        'id': 2,
        'content': 'Comment 2',
        'blog_id': 1
    },
    {
        'id': 3,
        'content': 'Comment 3',
        'blog_id': 2
    }
]

def create_comment(content, blog_id): 
    comment_data = {
        'id': len(comments) + 1,
        'content': content,
        'blog_id': blog_id
    }
    comments.append(comment_data)
    return comment_data


def get_comments(blog_id):
    

    return list(filter(lambda a: a['blog_id'] == blog_id, comments))


@app.route("/api/posts/<int:post_id>/comments",methods= ["GET","POST"])
def post_comments(post_id):
    if request.method == "POST":
        content = request.json["content"]
        new_comment = create_comment(content, post_id)
        
        
        post_data = {
            'type':"CommentCreated",
            'data':new_comment
        }
        requests.post('http://127.0.0.1:5003/api/events',json=post_data)
        
        
        return jsonify(new_comment)
    comments = get_comments(int(post_id))
    return jsonify(comments), 200
    