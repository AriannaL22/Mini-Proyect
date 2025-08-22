import numpy as np

def cargarDatos(nombreArchivo):
    distancias = {}
    with open(nombreArchivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split("|")
            ciudad = partes[0]
            conexiones = {}
            for conexion in partes[1:]:
                ciudad2, km = conexion.split(",")
                conexiones[ciudad2] = int(km)
            distancias[ciudad] = conexiones
    return distancias


def ciudadesCercanas(distancias, km):
    lista = []
    for ciudad1, conexiones in distancias.items():
        ciudades = np.array(list(conexiones.keys()))
        distancias_array = np.array(list(conexiones.values()))
        mask = distancias_array <= km

        for c, d, m in zip(ciudades, distancias_array, mask):
            if m:
                lista.append((ciudad1, c, d))
    return lista


def guardarCiudadesCercanas(distancias, listaKms):
    for km in listaKms:
        with open(f"ciudades{km}.txt", "w", encoding="utf-8") as f:
            for c1, c2, d in ciudadesCercanas(distancias, km):
                f.write(f"{c1}, {c2}, {d}\n")


def main():
    distancias = cargarDatos("Ecuador_Distancias.txt")
    guardarCiudadesCercanas(distancias, [150, 225, 320, 555])


if __name__ == "__main__":
    main()


