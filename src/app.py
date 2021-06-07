from .object_mgr import ObjectMgr
from flask import Flask
from flask_graphql import GraphQLView
from .schema import schema
from .storage_handler import StorageHdl 


def create_app():
    app = Flask(__name__)
    StorageHdl.create_dummy_dataset(ObjectMgr.create_list())
    app.add_url_rule(
    '/object',
    view_func=GraphQLView.as_view(
            'object',
            schema=schema,
            graphiql=True 
        )
    )

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    return app

app = create_app()


