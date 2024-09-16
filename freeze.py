import shutil
import os
from flask_frozen import Freezer
from app import create_app, db
from app.models import BlogPost

app = create_app()
freezer = Freezer(app)

# Clean the build directory
build_dir = 'build'
if os.path.exists(build_dir):
    shutil.rmtree(build_dir)

@freezer.register_generator
def url_generator():
    # Static routes
    yield 'main.index'
    yield 'main.projects'
    yield 'blog.blogs'
    yield 'blog.add_post'
    yield 'auth.login'
    yield 'auth.signup'
    yield 'auth.logout'
    yield 'profile.profile'
    yield 'contact.contact'
    yield 'admin.admin_dashboard'
    yield 'blog.search'

@freezer.register_generator
def post_urls():
    # Dynamic blog posts
    posts = BlogPost.query.all()  # Fetch all blog posts
    for post in posts:
        yield 'blog.post', {'post_id': post.id}  # Yield the URL with the post ID

if __name__ == '__main__':
    freezer.freeze()
