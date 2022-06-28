from fastapi import Request, Depends

from supervisely.app.fastapi import available_after_shutdown
import src.sly_globals as g

import src.example_card


@g.app.get("/")
@available_after_shutdown
def read_index(request: Request):
    return g.templates_env.TemplateResponse('index.html', {'request': request}), g.app

