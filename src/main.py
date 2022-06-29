import concurrent.futures
import os
import sys
import threading
import time
from pathlib import Path

import signal

from fastapi import Request, Depends

from starlette.background import BackgroundTasks
from starlette.types import Scope

from supervisely.app import StateJson, DataJson
from supervisely.app.fastapi import available_after_shutdown, run_sync
import src.sly_globals as g

import src.example_card


@g.app.get("/")
@available_after_shutdown
def read_index(request: Request = None):
    return g.templates_env.TemplateResponse('index.html', {'request': request}), g.app


@g.app.on_event("shutdown")
def shutdown():
    read_index()  # save last version of static files
