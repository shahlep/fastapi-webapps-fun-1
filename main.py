import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get('/')
def index():
    content = """
    
    <h1>Web app fun experiment </h1>
    <div>html template </div>
    """
    resp = fastapi.responses.HTMLResponse(content)
    return resp


if __name__ == '__main__':
    uvicorn.run(app)
