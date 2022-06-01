import fastapi
import fastapi_chameleon
from fastapi_chameleon import template

router = fastapi.APIRouter()

fastapi_chameleon.global_init("templates")


@router.get("/packages")
@template()
def index():
    return {}


@router.get("/packages/info")
@template()
def info():
    return {}
