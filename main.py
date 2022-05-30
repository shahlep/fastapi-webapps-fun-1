import fastapi
import uvicorn
from views import home, account, packages

app = fastapi.FastAPI()

app.include_router(home.router)
app.include_router(account.router)
app.include_router(packages.router)

if __name__ == "__main__":
    uvicorn.run(app)
