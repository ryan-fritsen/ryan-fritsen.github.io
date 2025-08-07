from flask import Flask, send_from_directory
import os

app = Flask(__name__)
root_dir = os.path.dirname(os.path.abspath(__file__))           # Project root, contains index.html
output_dir = os.path.join(root_dir, 'output')                    # Folder with posts/ and other assets
posts_dir = os.path.join(output_dir, 'posts')

@app.route('/')
def index():
    # Serve index.html from root_dir (not inside output/)
    return send_from_directory(root_dir, 'index.html')

# Checks /output/ directory, returns everything from output, drops "posts" folder since it's the onl
@app.route('/posts/<path:path>')
def posts(path):
    # Serve post pages from output/posts/
    return send_from_directory(posts_dir, path)

@app.route('/assets/<path:path>')
def assets(path):
    # Serve assets (css, js, images) from output/assets/
    return send_from_directory(os.path.join(output_dir, 'assets'), path)

@app.route('/<path:path>')
def static_proxy(path):
    # Catch-all: try to serve any other static files from output_dir
    return send_from_directory(output_dir, path)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
