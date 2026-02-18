# PEP8 OK
# -*- coding: utf-8 -*-

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.services.pc_info import get_pc_info

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/pc-info")
def pc_info():
    try:
        return get_pc_info()
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao obter informações do PC")


@router.get("/pc-info-page", response_class=HTMLResponse)
def pc_info_page(request: Request):
    return templates.TemplateResponse("pc_info.html", {"request": request})
