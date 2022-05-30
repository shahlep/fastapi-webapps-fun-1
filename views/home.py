import fastapi
import fastapi_chameleon
from fastapi_chameleon import template

router = fastapi.APIRouter()

fastapi_chameleon.global_init("templates")


@router.get("/")
@template(template_file="home/index.html")
def index():
    return {"user_name": "Shah Rahman"}


@router.get("/about")
def about():
    pass
