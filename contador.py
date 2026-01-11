# Programa para contar las palabras en un archivo de texto
# 1. Pedir al usuario la ruta de un archivo de texto
# 2. Leer el contenido del archivo
# 3. Separar en palabras
# 4. Contar número total de palabras
# 5. (Opcional) Mostrar las 10 palabras más frecuentes y su contenido
import re
from collections import Counter


class ContadorDePalabras:
    def __init__(self):
        self.texto = None
    
    def leer_archivo(self, ruta):
        """Lee el contenido de un archivo de texto."""
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                self.texto = f.read()
                return self.texto
        except FileNotFoundError:
            print(f"El archivo {ruta} no existe")
            raise
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            raise
    
    def contar_palabras(self, texto=None):
        """
        Cuenta las palabras en el texto y retorna el total y un Counter de frecuencias.
        Optimizado para construir el Counter directamente sin listas intermedias.
        
        Args:
            texto: Texto a analizar. Si es None, usa self.texto
        
        Returns:
            (total_palabras, contador_frecuencias) donde contador_frecuencias es un Counter
        """
        if texto is None:
            texto = self.texto
        
        if texto is None:
            raise ValueError("No hay texto disponible. Use leer_archivo primero o proporcione un texto.")
        
        # Usar finditer en lugar de findall: más eficiente en memoria
        # Construir el Counter directamente desde el generador
        texto_lower = texto.lower()
        palabras_iter = re.finditer(r'\w+', texto_lower)
        contador_frecuencias = Counter(match.group() for match in palabras_iter)
        total_palabras = sum(contador_frecuencias.values())
        
        return total_palabras, contador_frecuencias


# Uso de la clase
if __name__ == "__main__":
    archivo = input("Introduzca la ruta del archivo de texto: ")
    
    contador = ContadorDePalabras()
    texto = contador.leer_archivo(archivo)
    
    total_palabras, contador_frecuencias = contador.contar_palabras()
    print(f"Total palabras: {total_palabras}")
    
    mas_comunes = contador_frecuencias.most_common(10)
    print(f"Las 10 palabras más frecuentes son:")
    for palabra, freq in mas_comunes:
        print(f"{palabra}: {freq}")

