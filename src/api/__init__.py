from ariadne import ObjectType
from .graphql.post_resolver import PostResolver

query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("listPosts", PostResolver.list_posts)
query.set_field("getPost", PostResolver.get_post)
mutation.set_field("createPost", PostResolver.create_post)
mutation.set_field("updatePost", PostResolver.update_post)
mutation.set_field("deletePost", PostResolver.delete_post)
