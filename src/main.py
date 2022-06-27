from fastapi import Request, Depends

import src.sly_globals as g

import src.example_card


# @g.app.get("/")
# def read_index(request: Request):
#     template = g.templates_env.TemplateResponse('index.html', {'request': request})
#     with open('/Users/qanelph/Desktop/work/supervisely/dev-save-offline-session/rendered.html', 'wb') as file:
#         file.write(template.body)
#
#     print(template)
#     return g.templates_env.TemplateResponse('index.html', {'request': request})

template = g.templates_env.TemplateResponse('index.html', {'request': None})
with open('/Users/qanelph/Desktop/work/supervisely/dev-save-offline-session/rendered.html', 'wb') as file:
    file.write(template.body)
