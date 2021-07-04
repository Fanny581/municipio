cabecera  = {
    "Copan" : "Santa Rosa de Copan" ,
    "Cortes" : "San Pedro Sula" ,
    "Choluteca" : "Choluteca" ,
    "Santa Barbara" : "Santa Barbara" ,
    "Valle" : "Nacaome" ,
    "Yoro" : "Yoro"
}
try:
    print ("Cabeceras de Honduras")
    print ("Ingrese Nombre de Un Departamento para Ver la Cabecera Correspondiente")
    departamento = input("Ingresar: ")
    print("La Cebecera de {} es  {} .".format(departamento, format(cabecera[departamento],)))
except KeyError:
    print("El Pais no existe") 