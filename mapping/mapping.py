import folium

map = folium.Map(location=[38.58, -99.09])

map.add_child(folium.Marker(
    location=[38.5, -99], popup="marker", icon=folium.Icon(color='green')))
map.save('map1.html')
