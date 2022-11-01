import requests
from app import app
from flask import jsonify,request

blog_comment = [
    {
        'id': 1,
        'title': 'My Post',
        'comments':[
            {
                'id':1,
                'content':"Comment 1"
            },
            {
                'id':2,
                'content':"Comment 2"
            },
        ]
    },
    {
        'id': 2,
        'title': 'My Post',
        'comments':[
            {
                'id':3,
                'content':"Comment 3"
            },
            {
                'id':4,
                'content':"Comment 4"
            },
        ]
    },
]

def get_blogs():
    return blog_comment

@app.route('/api/queries', methods = ["GET",])
def posts():
    blogs = get_blogs()
    return jsonify(blogs)





def create_blog(data):
    data.update({
        'comments': []
    })
    blog_comment.append(data)
    return data

def create_comment(data):
    for blog in blog_comment:
        if blog['id'] == data['blog_id']:
            blog['comments'].append(data)
            break
    
    
@app.route('/api/events', methods = ['POST'])
def events():
    body = request.json
    event_type = body['type'] 
    if event_type == 'PostCreated':
        create_blog(data=body['data'])
    if event_type == 'CommentCreated':
        create_comment(data=body['data'])
        
    return jsonify(message = 'success')