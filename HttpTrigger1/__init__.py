from app import app as flask_app
import azure.functions as func
from azure.functions import WsgiMiddleware

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return WsgiMiddleware(flask_app).handle(req, context)
