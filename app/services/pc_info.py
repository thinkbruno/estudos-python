import platform
import psutil
from fastapi import APIRouter

router = APIRouter()


@router.get("/pc-info")
def get_pc_info():

    return {
        "fabricante": platform.node() if platform.node() else "N/A",
        "sistema_operacional": platform.system(),
        "versao_sistema": platform.version(),
        "arquitetura": platform.machine(),
        "processador": platform.processor(),
        "nucleos_cpu": psutil.cpu_count(logical=False),
        "nucleos_logicos": psutil.cpu_count(logical=True),
        "memoria_total_gb": round(psutil.virtual_memory().total / (1024**3), 2),
        "memoria_usada_percentual": psutil.virtual_memory().percent,
    }
