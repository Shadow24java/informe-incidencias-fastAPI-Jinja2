from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

INCIDENCIAS = [
    {"id": 1, "titulo": "Corte intermitente WiFi", "categoria": "red", "gravedad": 3, "resuelta": True, "equipo": "AP-2F"},
    {"id": 2, "titulo": "Servidor no arranca", "categoria": "hardware", "gravedad": 5, "resuelta": False, "equipo": "SRV-01"},
    {"id": 3, "titulo": "Error 500 en facturacion", "categoria": "software", "gravedad": 4, "resuelta": False, "equipo": "APP-FACT"},
    {"id": 4, "titulo": "Latencia elevada en VPN", "categoria": "red", "gravedad": 4, "resuelta": False, "equipo": "VPN-GW"},
    {"id": 5, "titulo": "SSD no detectado", "categoria": "hardware", "gravedad": 4, "resuelta": True, "equipo": "PC-22"},
    {"id": 6, "titulo": "Drivers impresora no instalan", "categoria": "software", "gravedad": 2, "resuelta": True, "equipo": "PRN-OFI"},
    {"id": 7, "titulo": "Switch con CPU alta", "categoria": "red", "gravedad": 2, "resuelta": True, "equipo": "SW-CORE"},
]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "base.html",
        {
            "request": request,
            "contenido": "<p>Ve a <a href='/informe'>/informe</a> para ver el informe.</p>",
        },
    )


@app.get("/informe", response_class=HTMLResponse)
async def informe(
    request: Request,   
    categoria: Optional[str] = Query(None, description="Filtrar por categoria: red / hardware / software"),  #query params
    min_gravedad: int = Query(1, ge=1, le=5, description="Gravedad minima (1-5)"),
):
    incidencias_filtradas = []
    for inc in INCIDENCIAS:
        if categoria is not None and inc["categoria"] != categoria:
            continue
        if inc["gravedad"] < min_gravedad:
            continue
        incidencias_filtradas.append(inc)

    total_incidencias = len(incidencias_filtradas)
    resueltas = sum(1 for inc in incidencias_filtradas if inc["resuelta"])
    porcentaje_resueltas = (resueltas / total_incidencias * 100) if total_incidencias > 0 else 0

    resumen = {
        "total": total_incidencias,
        "resueltas": resueltas,
        "porcentaje_resueltas": round(porcentaje_resueltas, 2),
    }

    categorias_posibles = ["red", "hardware", "software"]
    labels_categoria = categorias_posibles
    values_categoria = [sum(1 for inc in incidencias_filtradas if inc["categoria"] == c) for c in categorias_posibles]

    gravedades_posibles = [1,2,3,4,5]
    labels_gravedad = [str(g) for g in gravedades_posibles]
    values_gravedad = [sum(1 for inc in incidencias_filtradas if inc["gravedad"] == g) for g in gravedades_posibles]

    return templates.TemplateResponse(
        "informe.html",
        {
           "request": request,
            "incidencias": incidencias_filtradas,
            "resumen": resumen,
            "labels_categoria": labels_categoria,
            "values_categoria": values_categoria,
            "labels_gravedad": labels_gravedad,
            "values_gravedad": values_gravedad,
            "categoria": categoria,
            "min_gravedad": min_gravedad,
        },
    )


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
