import folium
html_file_path = "run_map.html"

# create map
run_map = folium.Map(location=[49.799891255201715, 10.580801170359733], tiles="OpenStreetMap", zoom_start=5)

# create feature group
fg = folium.FeatureGroup(name="My Map")

points_coordinates = []
points_coordinates.append(([52.51555779949443, 13.367028952828266], "Berlin Marathon"))
points_coordinates.append(([53.01391155869189, 13.997051337762928], "Schorfheide marathon"))
points_coordinates.append(([48.85896612853125, 2.2935252477178847], "Eco-Trail de Paris"))
points_coordinates.append(([51.79943900260884, 10.615524864337875], "Harz Broken marathon"))
points_coordinates.append(([48.232030367113396, 16.41620554169843], "Vienna marathon"))
points_coordinates.append(([54.31626411025583, 13.126867687637457], "Rugen marathon"))

for coordinates, popup_txt in points_coordinates:
    fg.add_child(folium.Marker(location=coordinates, popup=popup_txt, icon=folium.Icon(color='green')))

run_map.add_child(fg)

# save map
run_map.save(html_file_path)