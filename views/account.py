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
@template()
def login():
    return {}


@router.get("/account/logout")
@template()
def logout():
    return {}


@router.get("/account/registration")
@template()
def register():
    return {}
