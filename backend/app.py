import folium

# Crear mapa centrado en una ubicación
mapa = folium.Map(location=[-31.24735587063069, -61.51029371921464], zoom_start=16)  # Rafela, como ejemplo.

#Puto el que lee version 2

# Guardar el mapa
mapa.save("mapa.html")

