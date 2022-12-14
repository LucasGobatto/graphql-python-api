from ariadne import load_schema_from_path, make_executable_schema, \
  graphql_sync, snake_case_fallback_resolvers 
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from src.app import app
from src.api import query, mutation

type_defs = load_schema_from_path("src/data/graphql/schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
  return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
  data = request.get_json()
  success, result = graphql_sync(
    schema,
    data,
    context_value=request,
    debug=app.debug
  )
  status_code = 200 if success else 400
  return jsonify(result), status_code