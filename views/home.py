import fastapi
import fastapi_chameleon
from fastapi_chameleon import template

router = fastapi.APIRouter()

fastapi_chameleon.global_init("templates")


@router.get("/")
@template(template_file="home/index.pt")
def index():
    return {"user_name": "Shah Rahman"}


@router.get("/about")
@template(template_file="home/about.pt")
def about():
    return {}
