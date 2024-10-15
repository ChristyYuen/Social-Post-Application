"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""

import uuid

from py4web import action, request, abort, redirect, URL, Field
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.url_signer import URLSigner

from yatl.helpers import A
from . common import db, session, T, cache, auth, signed_url
from . models import get_user_email

url_signer = URLSigner(session)

# The auth.user below forces login.
@action('index')
@action.uses('index.html', url_signer, auth.user)
def index():

    add_post = URL('add_post' , signer=url_signer)                    #ADDED
    delete_post_URL = URL('delete_post' , signer=url_signer)                    #ADDED

    return dict(
        # This is an example of a signed URL for the callback.
        get_posts_url = URL('get_posts', signer=url_signer),
        # Add other callbacks here.
        user_email = get_user_email(),
        username = auth.current_user.get('first_name') + " " + auth.current_user.get("last_name"),
        add_post_URL = add_post,                                            #ADDED
        delete_post_URL = delete_post_URL                                   #ADDED
    )

@action('get_posts')
@action.uses(url_signer.verify(), auth.user)
def get_posts():
    # Complete.
    posts = [] # Just to keep code from breaking.
    postData = db(db.post).select().as_list()                       #ADDED

    for post in postData:
        email = post['user_email']
        r = db(db.auth_user.email == email).select().first()
        name = r.first_name + " " + r.last_name if r is not None else "Unknown"
        post["name"] = name

    return dict(posts=postData)                                      #ADDED sendData

@action('add_post', method="POST")
@action.uses(url_signer.verify(), auth.user)
def add_post():
    # Complete.

    data = request.json #can'ts use request.params                    #ADDED

    #postedText = data.text                                            #ADDED

    id = db.post.insert(post_text = data.get('postText') )                           #ADDED

    return dict(id=id) # You need to fill this in.

# Complete.


@action('delete_post', method="POST")
@action.uses(url_signer.verify(), auth.user, db)
def delete_post():
    # Complete.                       
    Jdata = request.json
    postID = Jdata['postID']

    db(db.post.id == postID).delete()

    return dict() # You need to fill this in.