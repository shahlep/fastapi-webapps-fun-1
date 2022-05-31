import fastapi
import fastapi_chameleon
from fastapi_chameleon import template

router = fastapi.APIRouter()

fastapi_chameleon.global_init("templates")


@router.get("/")
@template()
def index():
    return {"user_name": "Shah Rahman"}


@router.get("/about")
@template()
def about():
    return {}
