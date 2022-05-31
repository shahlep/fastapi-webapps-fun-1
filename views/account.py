import fastapi
import fastapi_chameleon
from fastapi_chameleon import template

router = fastapi.APIRouter()

fastapi_chameleon.global_init("templates")


@router.get("/account")
@template()
def index():
    return {}


@router.get("/account/login")
def login():
    pass


@router.get("/account/logout")
def logout():
    pass


@router.get("/account/registration")
def register():
    pass
