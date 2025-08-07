from jinja2 import Environment, FileSystemLoader
import frontmatter
import markdown
import os

env = Environment(loader=FileSystemLoader('templates'))
index_template = env.get_template('index.html')
post_template = env.get_template('post.html')

posts = []
for md_file in os.listdir('content'):
    if md_file.endswith('.md'):
        with open(f'content/{md_file}') as f:
            post = frontmatter.load(f)
            html_content = markdown.markdown(post.content)
            posts.append({
                'title': post.get('title'),
                'slug': md_file[:-3],
                'content': html_content
            })

# Render index.html with links to posts
with open('index.html', 'w') as f:
    f.write(index_template.render(posts=posts))

# Render each post page
os.makedirs('output/posts', exist_ok=True)
for post in posts:
    with open(f"output/posts/{post['slug']}.html", 'w') as f:
        f.write(post_template.render(post=post))
