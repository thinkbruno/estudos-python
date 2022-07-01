# PEP8 OK
# -*- coding: utf-8 -*-

import wmi

c = wmi.WMI()
my_system = c.WIN32_ComputerSystem()[0]

obj = {
    "Marca": my_system.Manufacturer,
    "Modelo": my_system.Model,
    "Nome": my_system.Name,
    "Qtde CPU": my_system.NumberOfProcessors,
    "Arquitetura": my_system.SystemType,
    "Família": my_system.SystemFamily
}

print(obj)
