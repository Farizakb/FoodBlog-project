import requests
from app import app
from flask import jsonify,request


blogs = [
    {
        'id': 1,
        'title': 'My Post'
    },
    {
        'id': 2,
        'title': 'My Post'
    },
    {
        'id': 3,
        'title': 'My Post'
    }
]


def create_blog(title):
    blog_data = {
        'id': len(blogs) + 1,
        'title': title
    }
    blogs.append(blog_data)
    return blog_data

def get_blogs():
    return blogs


@app.route('/api/posts', methods = ["GET", "POST"])
def posts():
    if request.method == 'POST':
        print(request.json)
        title = request.json['title']
        new_blog = create_blog(title=title)
        
        
        post_data = {
            'type':"PostCreated",
            'data':new_blog
        }
        requests.post('http://127.0.0.1:5003/api/events',json=post_data)
        
        
        return jsonify(new_blog), 201
    
    blogs = get_blogs()
    return jsonify(blogs)