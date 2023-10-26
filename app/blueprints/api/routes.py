from flask import request
from . import api


from app import db
from app.models import Post


## Enpoints to get all posts
@api.route('/posts')
def get_posts():
    posts = db.session.execute(db.select(Post)).scalars().all()
    return [post.to_dict() for post in posts]

#endpoint to get post by ID
@api.route('/posts/<post_id>')
def get_post(post_id):
    post = db.session.get(Post, post_id)
    if not post:
        return ['error:' f'Post with an ID of {post_id} does not exist'],404
    return post.to_dict()

# Endpoint to create a new post
@api.route('/posts', methods=['POST'])
def create_post():
    # Check to see that the request body is JSON
    if not request.is_json:
        return {'error': 'Your content type must be application/json'}, 400
    # Get the data from the request body
    data = request.json
    #Validate incoming data
    required_fields = ['title', 'body']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)} must be in the request body"}, 400
    # Get data from body
    title = data.get('title')
    title = data.get('body')
    title = data.get('image_url')
    # Create a new post to add to the database
    new_post = Post(title=title, body=body, image_url=image_url, user_id=1)
    db.session.add(new_post)
    db.session.commit
    return new_post.to_dict(), 201