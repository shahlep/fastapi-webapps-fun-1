import fastapi

router = fastapi.APIRouter()


@router.get("/account")
def index():
    pass


@router.get("/account/login")
def login():
    pass


@router.get("/account/logout")
def logout():
    pass


@router.get("/account/registration")
def register():
    pass
