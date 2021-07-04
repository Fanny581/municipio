municipios = {
    "la lima": 28000,
    "san Manuel": 180989,
    "la paz": 9000,
    "San Pedro Sula": 1200000,
    "la guadalupe": 94500,
    
}

try:
    municipios2 = input("Ingrese municipio: ")
    print("La poblacion de {} tiene {} habitantes.".format(municipios2, format(municipios[municipios2], ",d")))
except KeyError:
    print("El municipio no existe.")