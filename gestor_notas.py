# Importación de las librerías instaladas
import sys
import os
import requests
#para easter egg
import random
# cargo el .env
from dotenv import load_dotenv

from rich.console import Console #para la consola
from rich.panel import Panel #para el menu
from rich.table import Table #para las tablas

# Token y el ID de la BBDD de notion
load_dotenv()
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

# Creación de la consola de rich
consola = Console()

# Menú
def mostrar_menu():
    #para que no me mueva los caracteres uso r"""
    cinnamoroll = r"""
⠀⠀⡠⠂⠉⠉⠐⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀
⠀⠸⠀⠀⠀⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠃⠀⠀⠀⢄⠀⠀
⠀⠇⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠈⡆⠀
⢀⡃⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⢰⠄
⠈⢡⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠸⠄
⠀⠀⠡⡀⠀⠀⠀⠀⠀⠀⠑⠦⡤⠖⠊⠉⠀⠀⠀⠀⠀⠉⠑⠢⣄⣀⡠⠴⠃⠀⠀⠀⠀⠀⢀⠇⠀
⠀⠀⠀⠁⢀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠁⠀⠀⠀⠀⠀⠀⢀⡘⠀⠀
⠀⠀⠀⠀⠀⠁⠢⠄⣀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⡀⠀⠀⠀⢀⠀⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠰⠁⠀⢠⢶⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⢦⠀⠀⠙⡒⠒⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠈⠉⠁⠀⠀⠰⠤⠤⡴⠀⠀⠀⠈⠙⠀⠀⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⣼⠋⢳⠀⠀⠀⠀⠈⠒⠀⠀⠀⠀⢠⠊⠙⣤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠑⠒⠒⠒⠒⠒⠒⠒⠒⠒⠋⡀⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    #imprimo al chili morron con color azulito
    consola.print(cinnamoroll, style="bold light_cyan3")
    
    #Menú principal
    menu_texto = (
        "[bold pink1]1. [/bold pink1] Añadir una nota\n"
        "[bold pink1]2. [/bold pink1] Ver todas las notas\n"
        "[bold pink1]3. [/bold pink1] Buscar una nota por palabra clave\n"
        "[bold pink1]4. [/bold pink1] Eliminar una nota\n"
        "[bold pink1]5. [/bold pink1] Modificar una nota\n"
        "[bold pink1]6. [/bold pink1] Salir\n"
    )
    consola.print(Panel(menu_texto, title="☁️ Menú Principal ☁️", border_style="pink1", expand=False))

# IMPLEMENTACIÓN DE OPCIONES DEL MENÚ

# Ver notas:
def ver_notas(notas):
    # Si la lista está vacía, avisamos y salimos de la función
    if not notas:
        consola.print("[bold yellow]Aún no tienes ninguna nota guardada. ¡Anímate a escribir la primera![/bold yellow]\n")
        return

    # Si hay notas, creamos una tabla chulísima
    tabla = Table(title="🌸 Tus Notas 🌸", border_style="pink1", header_style="bold light_cyan3")
    
    # Definimos las columnas
    tabla.add_column("Nº", justify="center", style="cyan")
    tabla.add_column("Título", style="bold magenta")
    tabla.add_column("Categoría", justify="center", style="pink1")
    tabla.add_column("Contenido", style="white")

    # Variable para calcular la longitud media
    total_longitud = 0

    # Rellenamos la tabla recorriendo la lista con un for
    for i, nota in enumerate(notas, start=1):
        tabla.add_row(
            str(i), 
            nota["titulo"], 
            nota.get("categoria", "General"), 
            nota["contenido"]
        )
        total_longitud += len(nota["contenido"])

    # Imprimimos la tabla
    consola.print(tabla)

    # Estadísticas
    media = total_longitud / len(notas)
    consola.print(f"[italic pink1]Estadísticas: {len(notas)} notas guardadas | Longitud media: {media:.0f} caracteres[/italic pink1]\n")
    
# Funcion para subir las notas a notion
def subir_a_notion(titulo, categoria, contenido):
    # con una peticion post envio la nota a la bbdd de notion
    url = "https://api.notion.com/v1/pages"
    
    # Las cabeceras obligatorias que exige Notion:
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    
    # El diccionario con la estructura exacta que espera Notion (q es un json montao con la estructura q pide notion)
    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Título": {
                "title": [{"text": {"content": titulo}}]
            },
            "Categoría": {
                "rich_text": [{"text": {"content": categoria}}]
            },
            "Contenido": {
                "rich_text": [{"text": {"content": contenido}}]
            }
        }
    }
    
    # Intentamos hacer el envío y capturamos si hay errores
    try:
        respuesta = requests.post(url, headers=headers, json=data)
        if respuesta.status_code == 200:
            consola.print("[italic green]Nota sincronizada en tu Notion ☁️[/italic green]\n")
        else:
            consola.print(f"[italic red]Algo falló al subir a Notion. Código de error: {respuesta.status_code}[/italic red]\n")
    except Exception as e:
        consola.print(f"[italic red]Error de conexión: {e}[/italic red]\n")

#Función para bajar las notas de notion y leerlas en terminal
def descargar_de_notion():
    consola.print("[italic cyan]☁️ Sincronizando con Notion...[/italic cyan]")
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    
    notas_descargadas = []
    try:
        # Para leer una BBDD en Notion hacemos un POST al endpoint query
        respuesta = requests.post(url, headers=headers)
        
        if respuesta.status_code == 200:
            datos = respuesta.json()
            resultados = datos.get("results", [])
            
            for pagina in resultados:
                props = pagina["properties"]
                
                # Extraemos los datos con .get() por si alguna celda en Notion está vacía (así no peta)
                titulo_data = props.get("Título", {}).get("title", [])
                titulo = titulo_data[0]["text"]["content"] if titulo_data else "Sin título"
                
                cat_data = props.get("Categoría", {}).get("rich_text", [])
                categoria = cat_data[0]["text"]["content"] if cat_data else "General"
                
                cont_data = props.get("Contenido", {}).get("rich_text", [])
                contenido = cont_data[0]["text"]["content"] if cont_data else "Sin contenido"
                
                # Inyectamos la nota recuperada a nuestra lista
                notas_descargadas.append({
                    "titulo": titulo,
                    "categoria": categoria,
                    "contenido": contenido
                })
            
            consola.print(f"[bold green]¡Listo! Se han cargado {len(notas_descargadas)} notas desde la nube 🌸[/bold green]\n")
            return notas_descargadas
        else:
            consola.print(f"[italic red]No se pudieron descargar las notas. Código: {respuesta.status_code}[/italic red]\n")
            return []
    except Exception as e:
        consola.print(f"[italic red]Error de conexión al descargar: {e}[/italic red]\n")
        return []

# Fuyncion para editar las notas
def actualizar_en_notion(titulo_original, nuevo_titulo, nueva_categoria, nuevo_contenido):
    consola.print("[italic cyan]☁️ Buscando la nota en Notion para actualizarla...[/italic cyan]")
    
    # Buscar el ID exacto de la página (query)
    url_query = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    
    # Le decimos a Notion que busque exactamente el título antiguo
    filtro = {
        "filter": {
            "property": "Título",
            "title": {"equals": titulo_original}
        }
    }
    
    try:
        respuesta_query = requests.post(url_query, headers=headers, json=filtro)
        if respuesta_query.status_code == 200:
            resultados = respuesta_query.json().get("results", [])
            
            if not resultados:
                consola.print("[italic yellow]No se encontró la nota original en la nube. Solo se modificará en local.[/italic yellow]")
                return
            
            # Cogemos el ID de la primera coincidencia
            page_id = resultados[0]["id"]
            
            # Actualizo la página usando PATCH
            url_update = f"https://api.notion.com/v1/pages/{page_id}"
            
            datos_nuevos = {
                "properties": {
                    "Título": {"title": [{"text": {"content": nuevo_titulo}}]},
                    "Categoría": {"rich_text": [{"text": {"content": nueva_categoria}}]},
                    "Contenido": {"rich_text": [{"text": {"content": nuevo_contenido}}]}
                }
            }
            
            # Hacemos la petición PATCH para inyectar los datos nuevos
            respuesta_update = requests.patch(url_update, headers=headers, json=datos_nuevos)
            
            if respuesta_update.status_code == 200:
                consola.print("[italic green]☁️ Nota actualizada en tu Notion ☁️[/italic green]\n")
            else:
                consola.print(f"[italic red]Falló la actualización en Notion (Código: {respuesta_update.status_code}).[/italic red]\n")
        else:
            consola.print(f"[italic red]Error al buscar en Notion (Código: {respuesta_query.status_code}).[/italic red]\n")
            
    except Exception as e:
        consola.print(f"[italic red]Error de conexión: {e}[/italic red]\n")

# funcion para borrar tb de notion:
def borrar_de_notion(titulo):
    # buscamos el ID exacto de la nota en la base de datos
    url_query = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    
    # Le pedimos a Notion que filtre y nos traiga solo la nota con este título
    filtro = {
        "filter": {
            "property": "Título",
            "title": {
                "equals": titulo
            }
        }
    }
    
    try:
        # Hacemos la busqueda
        respuesta_busqueda = requests.post(url_query, headers=headers, json=filtro)
        resultados = respuesta_busqueda.json().get("results", [])
        
        # Si encuentra la nota, sacamos su ID oculto
        if resultados:
            page_id = resultados[0]["id"]
            
            # ahora que tenemos el ID, le decimos a Notion que la archive
            url_delete = f"https://api.notion.com/v1/pages/{page_id}"
            data_delete = {"archived": True}
            
            # Usamos PATCH para actualizar el estado de la página
            respuesta_borrado = requests.patch(url_delete, headers=headers, json=data_delete)
            
            if respuesta_borrado.status_code == 200:
                consola.print("[italic cyan]☁️ Registro eliminado también de tu Notion ☁️[/italic cyan]\n")
            else:
                consola.print(f"[italic red]No se pudo borrar de la nube. Código: {respuesta_borrado.status_code}[/italic red]\n")
    except Exception as e:
        consola.print(f"[italic red]Error místico al intentar borrar en la nube: {e}[/italic red]\n")

# Añadir notas:
def add_nota(notas):
    consola.print("\n[bold pink1]🗒️ Nueva Nota 🗒️[/bold pink1]")
    
    # Pedimos los datos al usuario
    titulo = consola.input("[light_cyan3]Título de la nota:[/light_cyan3] ").strip()
    categoria = consola.input("[light_cyan3]Categoría (ej: DAW, Poryectos, Tareas, Compras...):[/light_cyan3] ").strip()
    contenido = consola.input("[light_cyan3]Contenido:[/light_cyan3] ").strip()

    # Filtro de validación antiborrachines HAHAHHA
    if "cubata" in contenido.lower() or "cubata" in titulo.lower():
        consola.print("\n[bold red]⚠️  ¡ALERTA DE BORRACHÍN/A! ⚠️[/bold red]")
        alerta = consola.input("[bold red]¿Estás intentando salir de fiesteo con la de cosas que tienes que hacer? ¿Seguro/a que quieres guardar esta nota? (s/n): [/bold red]").strip().lower()
        if alerta != 's':
            consola.print("[yellow]Has hecho bien. Nota descartada, las fiestas cuando termine el curso 👀[/yellow]\n")
            return

    # Comprobar si el título ya existe
    for nota in notas:
        if nota["titulo"].lower() == titulo.lower():
            sobreescribir = consola.input(f"\n[bold yellow]⚠️ Ya existe una nota con el título '{titulo}'. ¿Quieres sobreescribirla? (s/n): [/bold yellow]").strip().lower()
            if sobreescribir == 's':
                nota["categoria"] = categoria
                nota["contenido"] = contenido
                consola.print("[bold green]¡Nota actualizada con éxito! 🌸[/bold green]\n")
            else:
                consola.print("[yellow]Operación cancelada. La nota original sigue intacta.[/yellow]\n")
            return # Salimos de la función porque ya hemos gestionado el duplicado

    # confirmación final antes de guardar
    confirmacion = consola.input("\n[bold light_cyan3]¿Guardar esta nota definitivamente? (s/n): [/bold light_cyan3]").strip().lower()
    if confirmacion == 's':
        # Creamos el diccionario y lo metemos en la lista
        nueva_nota = {
            "titulo": titulo,
            "categoria": categoria,
            "contenido": contenido
        }
        notas.append(nueva_nota)
        consola.print("[bold green]¡Nota guardada con éxito! 🌸[/bold green]\n")
        
        # para subirlo a notion:
        subir_a_notion(titulo, categoria, contenido)
    else:
        consola.print("[yellow]Operación cancelada. No se ha guardado nada.[/yellow]\n")

# Buscar notas:
def buscar_nota(notas):
    # buscamos las notas por palabra clave y muestra los reseultado sen una tabla
    consola.print("\n[bold pink1]🔍 Buscar Nota🔍 [/bold pink1]")
    
    # Foltro rápido por si no hay notas, y si no las hay que se salga
    if not notas:
        consola.print("[bold yellow]Aún no tienes notas guardadas.[/bold yellow]")
        return
        
    #Pedimos la palabra clave y la pasamos a minúsculas para comparar bien
    palabra = consola.input("[light_cyan3]Introduce la palabra clave a buscar: [/light_cyan3]").strip().lower()
    
    # Creamos una lista para guardar los resultados que coincidan
    encontradas = []
    
    # Recorremos todas las notas usando enumerate para no perder su número original
    for i, nota in enumerate(notas, start=1):
        # Buscamos el titulo 0 en el contenido pasandolo todo a minúsculas
        if palabra in nota["titulo"].lower() or palabra in nota["contenido"].lower():
            # lo guardamos con el número original y el diccionario de la nota
            encontradas.append((i, nota))
    
    # Muestro los resultados
    if encontradas:
        consola.print(f"\n[bold green]Se ha encontrado {len(encontradas)} coincidencia(s)! 🌸[/bold green]")
        
        # Reutilizamos la tabla cuki de rich
        tabla = Table(border_style="pink1", header_style="bold light_cyan3")
        tabla.add_column("Nº Original", justify="center", style="cyan")
        tabla.add_column("Título", style="bold magenta")
        tabla.add_column("Categoría", justify="center", style="pink1")
        tabla.add_column("Contenido", style="white")
        
        for num_original, nota in encontradas:
            tabla.add_row(
                str(num_original),
                nota["titulo"],
                nota.get("categoria", "General"),
                nota["contenido"]
            )
        
        consola.print(tabla)
        print("\n")
    
    else:
        consola.print(f"\n[bold red]No se han encontrado coincidencias con '{palabra}'.[/bold red]\n")
        
# eliminar notas:
def eliminar_nota(notas):
    #Muestra las notas y permite eliminar una de forma segura validando la entrada
    consola.print("\n[bold pink1]🗑️ Eliminar Nota🗑️[/bold pink1]")
    
    # El filtro por si no hubieran notas
    if not notas:
        consola.print("[bold yellow]Aún no tienes notas guardadas.[/bold yellow]")
        return
    
    # Mostramos las notas reutilizando la funcion que ya tenemos
    ver_notas(notas)
    
    # Pedimos el numero y le damos la opcion d echarse para atras :P
    entrada = consola.input("[light_cyan3]Introduce el número de la nota que quieres borrar (o 'c' para cancelar): [/light_cyan3]").strip().lower()
    
    if entrada == 'c':
        consola.print("[yellow]Operación cancelada. Tus notas están a salvo ☁️[/yellow]\n")
        return
    
    # Valido que el usuario no haya metido letras por error
    if not entrada.isdigit():
        consola.print("[bold red]¡Error! Debes introducir un número válido, no letras ni símbolos.[/bold red]\n")
        return
    
    # Si apasmos el filtro anterior ya podemos convertirlo a entero de forma segura
    numero = int(entrada)
    
    # Comprobamos si el número existe en nuestra lista
    if 1 <= numero <= len(notas):
        # Sacamos el título de la nota antes de borrarla para ponerlo enn el menú del mensaje
        nota_a_borrar = notas[numero - 1]
        titulo = nota_a_borrar["titulo"]
        
        #confirmacioon final
        confirmacion = consola.input(f"[bold red]⚠️ ¿Seguro/a que quieres borrar PARA SIEMPRE la nota '{titulo}'? (s/n): [/bold red]").strip().lower()
        
        if confirmacion == 's':
            notas.pop(numero - 1)
            consola.print(f"[bold green]¡Nota '{titulo}' eliminada con éxito![/bold green]\n")
            # para borrar d notion tb
            borrar_de_notion(titulo)
        else:
            consola.print("[yellow]Operación cancelada. La nota sigue guardada.[/yellow]\n")
        
    else:
        # Si mete un número superior al que existe d numeros de notas...
        consola.print(f"[bold red]¡Error! No existe ninguna nota con el número {numero}.[/bold red]\n")

# funcion para modificar una nota
def modificar_nota(notas):
    consola.print("\n[bold pink1]✏️ Modificar Nota ✏️[/bold pink1]")
    
    if not notas:
        consola.print("[bold yellow]Aún no tienes notas guardadas para modificar.[/bold yellow]\n")
        return
    #reutilizo mi tablita
    ver_notas(notas)
    
    entrada = consola.input("[light_cyan3]Introduce el número de la nota que quieres editar (o 'c' para cancelar): [/light_cyan3]").strip().lower()
    
    if entrada == 'c':
        consola.print("[yellow]Operación cancelada. Todo se queda como estaba.[/yellow]\n")
        return
        
    if not entrada.isdigit():
        consola.print("[bold red]¡Error! Debes introducir un número válido.[/bold red]\n")
        return
        
    numero = int(entrada)
    
    if 1 <= numero <= len(notas):
        nota = notas[numero - 1]
        titulo_antiguo = nota["titulo"]
        
        consola.print(f"\n[bold pink1]Editando: '{titulo_antiguo}'[/bold pink1]")
        consola.print("[italic cyan](Pulsa Enter sin escribir nada para mantener lo que ya había)[/italic cyan]")
        
        # Pedimos los nuevos datos. Si el input está vacío (""), usamos el valor antiguo
        nuevo_t = consola.input(f"[light_cyan3]Nuevo título [/light_cyan3][white]({nota['titulo']})[/white]: ").strip()
        nuevo_titulo = nuevo_t if nuevo_t else nota["titulo"]
        
        nueva_c = consola.input(f"[light_cyan3]Nueva categoría [/light_cyan3][white]({nota.get('categoria', 'General')})[/white]: ").strip()
        nueva_categoria = nueva_c if nueva_c else nota.get("categoria", "General")
        
        nuevo_con = consola.input(f"[light_cyan3]Nuevo contenido [/light_cyan3][white]({nota['contenido']})[/white]: ").strip()
        nuevo_contenido = nuevo_con if nuevo_con else nota["contenido"]
        
        # mandamos pa notion
        actualizar_en_notion(titulo_antiguo, nuevo_titulo, nueva_categoria, nuevo_contenido)
        
        # actualizamos nuestro diccionario local
        nota["titulo"] = nuevo_titulo
        nota["categoria"] = nueva_categoria
        nota["contenido"] = nuevo_contenido
        
        consola.print("[bold green]¡Nota modificada con éxito en tu terminal![/bold green]\n")
    else:
        consola.print(f"[bold red]¡Error! No existe ninguna nota con el número {numero}.[/bold red]\n")

#menu secretillo pokedex
def abrir_pokedex():
    consola.print("\n[bold yellow]🦭 ¡Has descubierto la Pokédex Secreta! 🦭[/bold yellow]")
    
    # Creamos un bucle infinito exclusivo para la Pokédex
    while True:
        pokemon = consola.input("\n[yellow]Dime el nombre de un Pokémon o su número (escribe 'c' para volver al menú): [/yellow]").strip().lower()
        
        if pokemon == 'c':
            consola.print("[italic yellow]Cerrando la Pokédex... ¡Volviendo a las notas! ☁️[/italic yellow]\n")
            break # Rompemos este bucle y volvemos al menú principal
            
        if not pokemon:
            continue

        # Llamada a la API pública de Pokémon
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
        
        try:
            respuesta = requests.get(url)
            
            if respuesta.status_code == 200:
                datos = respuesta.json()
                
                # Extraemos la info (la API devuelve todo en minúsculas y medidas raras)
                nombre = datos["name"].capitalize()
                n_pokedex = datos["id"]
                peso = datos["weight"] / 10 # Viene en hectogramos, lo pasamos a kg
                altura = datos["height"] / 10 # Viene en decímetros, lo pasamos a m
                
                # Juntamos los tipos si tiene más de uno
                tipos = ", ".join([t["type"]["name"].capitalize() for t in datos["types"]])
                
                # Montamos un panel wapardo con rich
                info = (
                    f"🔢 [bold]Nº Pokédex:[/bold] {n_pokedex}\n"
                    f"🌟 [bold]Nombre:[/bold] {nombre}\n"
                    f"🔥 [bold]Tipo:[/bold] {tipos}\n"
                    f"📏 [bold]Altura:[/bold] {altura} m\n"
                    f"⚖️ [bold]Peso:[/bold] {peso} kg"
                )
                
                consola.print(Panel(info, title=f"💻 POKÉDEX DATA", border_style="yellow", expand=False))
                
            else:
                consola.print(f"[bold red]¡Oh no! El Pokémon '{pokemon}' no aparece. O no existe, o se ha escondido de ti.[/bold red]")
                
        except Exception as e:
            consola.print(f"[italic red]Error de conexión con la Liga Pokémon: {e}[/italic red]")

#menu secretillo 2 suerte
def tirar_carta_suerte():
    consola.print("\n[bold purple]☁️ Conectando con las nubes de Clouds & Arcana... ☁️[/bold purple]")
    
    # saco la url de la api q he creado en el otro proyecto
    url = "https://cloudsandarcana.vercel.app/api/tarot"
    
    try:
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            cartas = respuesta.json()
            
            # elegimos una carta al azar de toda mi lista
            carta_hoy = random.choice(cartas)
            
            nombre = carta_hoy["nombre"]
            mensaje = carta_hoy["mensaje"]
            
            info = (
                f"🃏 [bold]Tu Carta:[/bold] {nombre}\n"
                f"🔮 [bold]Mensaje:[/bold] {mensaje}"
            )
            
            consola.print(Panel(info, title="☁️ ENERGÍA DE HOY ☁️", border_style="purple", expand=False))
            consola.print("[italic purple]Recuerda: El oráculo solo guía, tú tienes el poder de tu destino.[/italic purple]\n")
            
        else:
            consola.print(f"[bold red]Error de conexión con la API: (Código: {respuesta.status_code}).[/bold red]\n")
            
    except Exception as e:
        consola.print(f"[italic red]Error de conexión astral: {e}[/italic red]\n")

#MAIN
def main():
    #Bucle principal para que llame al resto de ufnciones
    #notas = []
    #en vez de empezar la lista vacia llamamos a notion nada mas abrir el gestor jeje
    notas = descargar_de_notion()
    
    #voy a hardcodear para ver el resultado, lo dejare todo comentado en el futuro para q veas el proceso jeje
    #notas = [
    #    {"titulo": "Prueba nota 1", "categoria": "Proyectos", "contenido": "Probando como se visualiza en la terminal"},
    #    {"titulo": "hola mundo", "categoria": "Ocio", "contenido": "hello wordl"}
    #]
    
    while True:
        mostrar_menu()
        #Uso el input para recoger la opcion
        opcion = consola.input("[bold light_cyan3]Elige una opción (1 a 6 o prueba suerte a ver si encuentras los comandos secretos): [/bold light_cyan3]").strip().lower()
        
        if opcion == '1':
            add_nota(notas)
        elif opcion == '2':
            ver_notas(notas)
        elif opcion == '3':
            buscar_nota(notas)
        elif opcion == '4':
            eliminar_nota(notas)
        elif opcion == '5':
            modificar_nota(notas)
        elif opcion == '6':
            consola.print("[yellow]Cerrando el gestor de notas. ¡Hasta prontooo! ☁️[/yellow]")
            break
        elif opcion == 'pokemon':
            abrir_pokedex()
        elif opcion == 'suerte':
            tirar_carta_suerte()
        else:
            consola.print("[bold red]Opción no válida, inténtalo de nuevo![/bold red]")
            
        #frenar bucle hasta que el usuario pulse enter
        #se me hacia muy molesto q saltara el menu mientras revisaba como se veian las notas
        consola.input("\n[italic cyan]Presiona Enter para continuar...[/italic cyan]")
        
if __name__ == "__main__":
    main()