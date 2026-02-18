from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routers import utils
from app.routers import age
from app.routers import battery
from app.routers import currency
from app.routers import json_generator
from app.routers import discover_mobile_operator
from app.routers import download_file
from app.routers import pdf_generator
from app.routers import speedtest_router
from app.routers import qrcode_generator
from app.routers import qrcode_reader

app = FastAPI(title="Estudos Python API")

app.include_router(utils.router)
app.include_router(age.router)
app.include_router(battery.router)
app.include_router(currency.router)
app.include_router(json_generator.router)
app.include_router(discover_mobile_operator.router)
app.include_router(download_file.router)
app.include_router(pdf_generator.router)
app.include_router(speedtest_router.router)
app.include_router(qrcode_generator.router)
app.include_router(qrcode_reader.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
def read_index():
    return FileResponse("app/static/index.html")
