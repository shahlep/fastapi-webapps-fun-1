import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get('/')
def index():
    return f'Web app fun experiment'


if __name__ == '__main__':
    uvicorn.run(app)
