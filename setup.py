import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()    # TODO

setuptools.setup(
    name="api-jokes",
    version="1.0",
    author="Elena Cherkasova",
    author_email="cherowl@yandex.ru",
    description="RESTful API created with Flask using PostgreSQL. Generate jokes for users.",
    long_description="...",
    long_description_content_type="...",
    url="git@github.com:cherowl/api-jokes.git",
    packages=setuptools.find_packages(),
    install_requires=['flask', 'pip-tools', 'configparser', 'requests', 'flask-sqlalchemy', 'flask-exceptional', 'werkzeug', 'flask_login', 'flask_basicauth', 'itsdangerous'] 
    
)

# sqlite3 on server
# change it again to postgresql


