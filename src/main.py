from fastapi import Request

import src.sly_globals as g
from supervisely.app.fastapi import available_after_shutdown


@g.app.get("/")
@available_after_shutdown
def read_index(request: Request = None):
    return g.templates_env.TemplateResponse('index.html', {'request': request}), g.app


@g.app.on_event("shutdown")
def shutdown():
    read_index()  # save last version of static files
