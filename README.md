Mini-Proyecto:
Este proyecto en Python genera archivos con ciudades conectadas directamente
según una distancia máxima, usando numpy para filtrar eficientemente.
Archivos
- Ecuador_Distancias.txt : Distancias entre ciudades.  
- Proyecto.py : Script con las funciones principales.

Funciones:
1. cargarDatos(nombreArchivo): Lee el archivo y crea un diccionario de distancias.
2. ciudadesCercanas(distancias, km): Retorna tuplas (ciudad_origen, ciudad_destino, distancia) con distancia <= km.
3. guardarCiudadesCercanas(distancias, listaKms): Crea archivos .txt para cada km en listaKms con las ciudades cercanas.

Uso:
1. Colocar Ecuador_Distancias.txt en la misma carpeta que Proyecto.py  
2. Ejecutar: python Proyecto.py  
3. Se generan archivos como: ciudades150.txt, ciudades225.txt, ciudades320.txt, ciudades555.txt

Requisitos
- Python 3.x  
- numpy: pip install numpy
