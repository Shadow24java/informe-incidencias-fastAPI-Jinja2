#Práctica DI - RA5
## informe-incidencias-fastAPI-Jinja2

Web sencilla que genera un informe HTML de incidencia del sistema usando FastAPI y Jinja2. El informe incluye filtros, resumen, tabla y gráficos.

Estructura del informe:
Filtros:
Selector de categoría
Campo numérico de gravedad mínima

Resumen:
Total de incidencias
Número de incidencias resueltas
Porcentaje de incidencias resueltas

Tabla:
Listado de incidencias filtradas con: ID, título, categoría, gravedad, equipo y estado (Abierta/Resuelta)

Gráficos:
Gráfica 1: Incidencias por categoría.
Gráfica 2: Incidencias por gravedad.

Tambien muestra los calculos totales de las incidencias que se hayan filtrado.

<img width="1903" height="346" alt="Captura de pantalla 2026-01-15 164855" src="https://github.com/user-attachments/assets/5b7ffaf5-2840-4e34-876c-6ec55b5792e4" />
En esta primera imagen podemos ver donde se aplican los filtros.

<img width="1880" height="753" alt="Captura de pantalla 2026-01-15 164906" src="https://github.com/user-attachments/assets/167f71f0-4efe-4464-aa5c-8b92b5cb43ef" />
En esta otra vemos el primer gráfico que indica las incidencias filtradas por categoría.

<img width="909" height="408" alt="image" src="https://github.com/user-attachments/assets/97f67b5f-3b29-45c2-a11a-997d61ac2dc5" />
Y en esta última se puede ver el segundo gráfico con las incidencias de gravedad.


