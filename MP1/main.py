# Parte 1: Cargar los datos

def cargar_datos():
    with open('pokemon.csv','r',encoding='utf-8') as archivo:
        pokemones=[]
        for line in archivo:
            pokemones.append(line.strip().split(','))
        variables = pokemones.pop(0)
        
        tipos_pokemon_rep = []
        pokemon_por_tipo = dict()
        info_pokemon = dict()
        
        for pokemon in pokemones:
            tipos_pokemon_rep.append(pokemon[2])
            info_pokemon[pokemon[0]] = dict()
            for i in range(1,len(pokemon)):
                info_pokemon[pokemon[0]][variables[i]] = pokemon[i]
        tipos_pokemon = set(tipos_pokemon_rep)
        
        
        for tipo in tipos_pokemon:
            pokemon_por_tipo[tipo] = []
            for pokemon in pokemones:
                if pokemon[2]==tipo:
                    pokemon_por_tipo[tipo].append(pokemon[0])
            pokemon_por_tipo[tipo] = list(set(pokemon_por_tipo[tipo]))
            
    return tipos_pokemon, pokemon_por_tipo, info_pokemon



# Parte 2: Completar las consultas
tipos_pokemon, pokemon_por_tipo, info_pokemon = cargar_datos()

def obtener_ataque_y_defensa(nombre_pokemon):
    for id in info_pokemon:
        if info_pokemon[id]['nombre'] == nombre_pokemon:
            tupla = (info_pokemon[id]['ataque'],info_pokemon[id]['defensa'])
    return tupla

def filtrar_y_ordenar(tipo_pokemon, criterio):
    pokemones_del_tipo = pokemon_por_tipo[tipo_pokemon]
    lista_pokemones = []
    for id in pokemones_del_tipo:
        lista_pokemones.append((info_pokemon[id]['nombre'],int((info_pokemon[id][criterio]))))
    lista_ordenada = sorted(lista_pokemones, key=lambda x:x[1], reverse=True)
    lista_ordenada_solo_nombres = []
    for pokemon in lista_ordenada: 
        lista_ordenada_solo_nombres.append(pokemon[0])
    return lista_ordenada_solo_nombres

def obtener_estadisticas(tipo_pokemon, criterio):
    pokemones_del_tipo = pokemon_por_tipo[tipo_pokemon]
    lista_pokemones = []
    lista_criterio =[]
    for id in pokemones_del_tipo:
        lista_pokemones.append(info_pokemon[id]['nombre'])
        lista_criterio.append(int((info_pokemon[id][criterio])))
    return {'max': max(lista_criterio),'min':min(lista_criterio),'prom':sum(lista_criterio)/len(lista_criterio)}


def solicitar_accion():
    print("\n¿Qué desea hacer?\n")
    print("[0] Revisar estructuras de datos")
    print("[1] Obtener ataque y defensa de un pokemon")
    print("[2] Filtrar y ordenar pokemons")
    print("[3] Obtener estadísticas de pokemons")
    print("[4] Salir")

    eleccion = input("\nIndique su elección (0, 1, 2, 3, 4): ")
    while eleccion not in "01234":
        eleccion = input("\nElección no válida.\nIndique su elección (0, 1, 2, 3, 4): ")
    eleccion = int(eleccion)
    return eleccion


def revisar_estructuras(tipos_pokemon, pokemon_por_tipo, info_pokemon):
    print("\nTipos de pokemon:")
    for tipo in tipos_pokemon:
        print(f"    - {tipo}")

    print("\nId de pokemons por tipo:")
    for tipo in pokemon_por_tipo:
        print(f"    Tipo: {tipo}")
        for id_ in pokemon_por_tipo[tipo]:
            print(f"        - {id_}")

    print("\nInformación de cada pokemon:")
    for id_ in info_pokemon:
        print(f"    Id: {id_}")
        for llave in info_pokemon[id_]:
            print(f"        - {llave}: {info_pokemon[id_][llave]}")


def solicitar_nombre():
    nombre = input("\nIngrese el nombre del pokemon: ")
    return nombre


def solicitar_tipo_y_criterio():
    tipo = input("\nIndique el tipo de pokemon: ")
    criterio = input("\nIndique el criterio (hp, ataque, defensa): ")
    return tipo, criterio


def main():
    datos_cargados = True
    try:
        tipos_pokemon, pokemon_por_tipo, info_pokemon = cargar_datos()
    except TypeError as error:
        if 'cannot unpack non-iterable NoneType object' in repr(error):
            print("\nTodavía no puedes ejecutar el programa ya que no has cargado los datos\n")
            datos_cargados = False
    if datos_cargados:
        salir = False
        print("\n********** ¡Bienvenid@! **********")
        while not salir:
            accion = solicitar_accion()

            if accion == 0:
                revisar_estructuras(tipos_pokemon, pokemon_por_tipo, info_pokemon)

            elif accion == 1:
                nombre_pokemon = solicitar_nombre()
                ataque, defensa = obtener_ataque_y_defensa(nombre_pokemon)
                print(f"\nObteniendo ataque y defensa de {nombre_pokemon}")
                print(f"    - Ataque: {ataque}")
                print(f"    - Defensa: {defensa}")

            elif accion == 2:
                tipo, criterio = solicitar_tipo_y_criterio()
                nombres_pokemon = filtrar_y_ordenar(tipo, criterio)
                print(f"\nNombres de pokemon tipo {tipo} ordenados segun {criterio}:")
                for nombre in nombres_pokemon:
                    print(f"    - {nombre}")

            elif accion == 3:
                tipo, criterio = solicitar_tipo_y_criterio()
                estadisticas = obtener_estadisticas(tipo, criterio)
                print(f"\nEstadísticas de {criterio} de pokemon tipo {tipo}:")
                print(f"    - Máximo: {estadisticas['max']}")
                print(f"    - Mínimo: {estadisticas['min']}")
                print(f"    - Promedio: {estadisticas['prom']}")

            else:
                salir = True
        print("\n********** ¡Adiós! **********\n")


if __name__ == "__main__":
    main()
