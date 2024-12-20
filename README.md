# agregar_superindices

Agrega superíndices secuenciales al inicio de cada línea: Ejemplo ² Texto.

## Uso

1. Instalar el programa

   ```sh
   git clone https://github.com/victorbondaruk/agregar_superindices.git
   ```

2. Asignar texto

Insertar en el archivo `entrada.txt` el texto.

```sh
 Ejemplo de una oración
 Otra oración.
```

3. Ejecutar programa

En la consola, dentro de la misma ubicacion de este proyecto, ejecutar el script:

```sh
python3 agregar_superindices.py
```

4. Resultado

El texto formateado de esta manera `¹ Oracion`, se almacenara en el archivo `salida.txt`

```sh
¹ Ejemplo de una oración
² Otra oración.
```
