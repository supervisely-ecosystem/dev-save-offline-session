from fastapi import Request

import src.sly_globals as g
from supervisely.app.fastapi import available_after_shutdown

import src.example_card


@g.app.get("/")
@available_after_shutdown(app=g.app)
def read_index(request: Request = None):
    return g.templates_env.TemplateResponse('index.html', {'request': request})


@g.app.on_event("shutdown")
def shutdown():
    read_index()  # save last version of static files
