# Contador de Palabras

Un programa simple en Python para analizar archivos de texto, contar el número total de palabras y mostrar las palabras más frecuentes.

## Descripción

Este proyecto proporciona una herramienta de análisis de texto que permite:
- Leer archivos de texto
- Contar el número total de palabras
- Identificar y mostrar las palabras más frecuentes

El programa está implementado como una clase reutilizable (`ContadorDePalabras`) que puede integrarse fácilmente en otros proyectos o ejecutarse como script independiente.

## Características

- ✅ Lectura de archivos de texto con codificación UTF-8
- ✅ Conteo preciso de palabras usando expresiones regulares
- ✅ Análisis de frecuencia de palabras
- ✅ Visualización de las 20 palabras más frecuentes
- ✅ Manejo de errores para archivos no encontrados
- ✅ Optimizado para memoria (usa generadores)
- ✅ Solo utiliza bibliotecas estándar de Python (sin dependencias externas)

## Requisitos

- Python 3.6 o superior
- Solo utiliza bibliotecas estándar (`re` y `collections`)

## Instalación

No se requiere instalación de dependencias adicionales, ya que el proyecto solo utiliza bibliotecas estándar de Python.

1. Clona o descarga este repositorio
2. Asegúrate de tener Python 3.6+ instalado
3. (Opcional) Crea un entorno virtual para aislar el proyecto:

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

## Uso

### Ejecución como Script

Ejecuta el archivo `contador.py` desde la línea de comandos:

```bash
python contador.py
```

El programa te pedirá que introduzcas la ruta del archivo de texto que deseas analizar. Una vez proporcionada, mostrará:
- El total de palabras encontradas
- Las 20 palabras más frecuentes con su número de apariciones

**Ejemplo de uso:**
```
Introduzca la ruta del archivo de texto: ejemplo.txt
Total palabras: 1250
Las 20 palabras más frecuentes son:
el: 45
la: 38
de: 32
...
```

### Uso como Módulo

También puedes importar la clase `ContadorDePalabras` en tus propios scripts:

```python
from contador import ContadorDePalabras

# Crear una instancia
contador = ContadorDePalabras()

# Leer un archivo
contador.leer_archivo("mi_archivo.txt")

# Contar palabras
total, frecuencias = contador.contar_palabras()

# Trabajar con los resultados
print(f"Total de palabras: {total}")
print(f"Palabras únicas: {len(frecuencias)}")

# Obtener las 10 más frecuentes
top_10 = frecuencias.most_common(10)
for palabra, cantidad in top_10:
    print(f"{palabra}: {cantidad}")
```

## Estructura del Proyecto

```
contador_palabras/
│
├── contador.py          # Archivo principal con la clase ContadorDePalabras
├── README.md            # Este archivo
└── venv/                # Entorno virtual (opcional)
```

## Métodos de la Clase

### `leer_archivo(ruta)`
Lee el contenido de un archivo de texto y lo almacena en la instancia.

**Parámetros:**
- `ruta` (str): Ruta al archivo de texto a leer

**Retorna:**
- `str`: Contenido del archivo leído

**Lanza:**
- `FileNotFoundError`: Si el archivo no existe
- `Exception`: Para otros errores de lectura

### `contar_palabras(texto=None)`
Cuenta las palabras en el texto y retorna el total y un Counter de frecuencias.

**Parámetros:**
- `texto` (str, opcional): Texto a analizar. Si es `None`, usa el texto almacenado en la instancia

**Retorna:**
- `tuple`: `(total_palabras, contador_frecuencias)` donde:
  - `total_palabras` (int): Número total de palabras
  - `contador_frecuencias` (Counter): Objeto Counter con las frecuencias de cada palabra

**Lanza:**
- `ValueError`: Si no hay texto disponible para analizar

## Notas

- El programa trata todas las palabras en minúsculas para el conteo de frecuencias
- Utiliza expresiones regulares (`\w+`) para identificar palabras, lo que incluye letras, dígitos y guiones bajos
- El análisis es case-insensitive para las frecuencias (todas las palabras se convierten a minúsculas)
- El programa está optimizado para manejar archivos grandes usando generadores

## Licencia

Este proyecto es de código abierto y está disponible para uso libre.

## Autor

Proyecto desarrollado como herramienta educativa para análisis de texto.
