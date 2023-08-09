from fastapi import FastAPI
import uvicorn

from latin_api.api import routers as api_routers

def init_fastapi_application():
    app = FastAPI(title="Latin Learning API", docs_url='/docs')
    app.include_router(api_routers.chapter1_5.router)  #TODO: adjust names as build API out
    app.include_router(api_routers.chapter6_10.router)
    return app

def init(host:str, port:int):
    uvicorn.run('latin_api.api.webapp:init_fastapi_application', host=host, port=port)