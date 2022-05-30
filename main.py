import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get('/')
def index():
    return f'Web app fun experiment'


uvicorn.run(app)
