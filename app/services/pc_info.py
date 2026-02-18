# PEP8 OK
# -*- coding: utf-8 -*-

import platform

try:
    import wmi
except ImportError:
    wmi = None


def get_pc_info():
    if wmi:
        c = wmi.WMI()
        system = c.Win32_ComputerSystem()[0]

        return {
            "manufacturer": system.Manufacturer,
            "model": system.Model,
            "name": system.Name,
            "cpu_count": system.NumberOfProcessors,
            "architecture": system.SystemType,
            "family": system.SystemFamily,
        }

    # fallback para outros sistemas
    return {
        "manufacturer": "N/A",
        "model": platform.machine(),
        "name": platform.node(),
        "cpu_count": platform.processor(),
        "architecture": platform.architecture()[0],
        "family": platform.system(),
    }
