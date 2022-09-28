from src.data.entity.post_entity import Post
from ariadne import convert_kwargs_to_snake_case
from datetime import date
from src.data.db.config import db

class PostResolver:
  @staticmethod
  @convert_kwargs_to_snake_case
  def list_posts(obj, info):
    try:
      posts = [post.to_dict() for post in Post.query.all()]
      payload = {
        "success": True,
        "posts": posts
      }
    except Exception as error:
      payload = {
        "success": False,
        "errors": [str(error)]
      }
    return payload

  @staticmethod
  @convert_kwargs_to_snake_case
  def get_post(obj, info, id):
    try:
      post = Post.query.get(id)
      payload = {
        "success": True,
        "post": post.to_dict()
      }
    except AttributeError:  # todo not found
      payload = {
        "success": False,
        "errors": ["Post item matching {id} not found"]
      }
    return payload

  @staticmethod
  @convert_kwargs_to_snake_case
  def create_post(obj, info, title, description):
    try:
      today = date.today()
      post = Post(
        title=title, description=description, created_at=today.strftime("%b-%d-%Y")
      )
      db.session.add(post)
      db.session.commit()
      payload = {
        "success": True,
        "post": post.to_dict()
      }
    except ValueError:  # date format errors
      payload = {
        "success": False,
        "errors": [f"Incorrect date format provided. Date should be in "
                    f"the format dd-mm-yyyy"]
      }
    return payload


  @staticmethod
  @convert_kwargs_to_snake_case
  def update_post(obj, info, id, title, description):
    try: 
      post = Post.query.get(id)
      if post:
        post.title = title
        post.description = description

      db.session.add(post)
      db.session.commit()

      payload = {
        "success": True,
        "post": post.to_dict()
      }
    except ValueError:
      payload = {
        "success": False,
        "errors": ["item matching id {id} not found"]
      }
    finally:
      return payload
      
  @staticmethod
  @convert_kwargs_to_snake_case
  def delete_post(obj, info, id):
    try:
      post = Post.query.get(id)
      db.session.delete(post)
      db.session.commit()
      payload = {"success": True, "post": post.to_dict()}
    except AttributeError:
      payload = {
        "success": False,
        "errors": ["Not found"]
      }
    return payload
