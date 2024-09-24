import pytest
from masoniteorm.migrations import Migration
from models.User import User
from models.Post import Post
from models.Comment import Comment

@pytest.fixture(autouse=True)
def setup_database():
    config_path = "config/test_config.py"

    migrator = Migration(config_path=config_path)
    migrator.create_table_if_not_exists()

    migrator.refresh()


@pytest.fixture(scope="function")
def user():
    user = User()
    user.name = "John Doe"
    user.email = "jdoe@mail.com"
    user.address = "POB MU 2672, Kanda"
    user.phone_number = "0249715263"
    user.sex = "male"
    user.save()

    return user


@pytest.fixture(scope="function")
def post(user):
    post = Post()
    post.title = "Software Performance"
    post.body = "Most developers do not very \
                    much worry about the performance of their"
    post.user_id = user.id
    post.save()

    user.attach("posts", post)


@pytest.fixture(scope="function")
def comment(user, post):
    comment = Comment()
    comment.body = "Nice post"
    comment.user_id = user.id
    comment.post_id = post.id
    comment.save()

    user.attach("comments", comment)
    post.attach("comments", comment)

    return comment