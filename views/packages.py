import fastapi

router = fastapi.APIRouter()


@router.get("/")
def index():
    pass
