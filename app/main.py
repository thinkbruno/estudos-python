from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routers import utils
from app.routers import age
from app.routers import battery
from app.routers import currency

app = FastAPI(title="Estudos Python API")

app.include_router(utils.router)
app.include_router(age.router)
app.include_router(battery.router)
app.include_router(currency.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def read_index():
    return FileResponse("app/static/index.html")
