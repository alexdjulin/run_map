import folium
import pandas
import webbrowser

# define paths to external files
run_map_html = "run_map.html"
popup_contents_html = "popup_contents.html"
events_cst = "events.csv"

# define race colors based on distance and store them in a dictionnary
race_color_dict = {
'5': "rgb(155, 255, 0)",
'10': "rgb(55, 175, 255)",
'21.1': "rgb(135, 55, 255)",
'42.2': "rgb(192,0,0)",
'ultra': "rgb(0,0,0)",
'misc': "rgb(255,213,0)"
}

# load html popup contents
with open(popup_contents_html) as f:
    html_popup = f.read()

# create map centered on West Europe
# IMPROVEMENT: Calculate center of map based on race locations
run_map = folium.Map(location=[49.799891255201715, 10.580801170359733], tiles="OpenStreetMap", zoom_start=5)

# get data from csv file
data = pandas.read_csv(events_cst)
date_list = list(data["Date"])
race_list = list(data["Race"])
loc_list = list(data["Location"])
lat_list = list(data["Latitude"])
lon_list = list(data["Longitude"])
type_list = list(data["Type"])
dist_list = list(data["Distance"])
time_list = list(data["Time"])
notes_list = list(data["Notes"])
link_list = list(data["Link"])
pic_list = list(data["Picture"])

# create feature group
fg = folium.FeatureGroup(name="My Map")

# points_coordinates.append(([52.51555779949443, 13.367028952828266], "Berlin Marathon"))
# points_coordinates.append(([53.01391155869189, 13.997051337762928], "Schorfheide marathon"))
# points_coordinates.append(([48.85896612853125, 2.2935252477178847], "Eco-Trail de Paris"))
# points_coordinates.append(([51.79943900260884, 10.615524864337875], "Harz Broken marathon"))
# points_coordinates.append(([48.232030367113396, 16.41620554169843], "Vienna marathon"))
# points_coordinates.append(([54.31626411025583, 13.126867687637457], "Rugen marathon"))

# add markers based on csv file data
for date, race, loc, lt, ln, typ, dist, time, notes, link, pic in zip(date_list, race_list, loc_list, lat_list, lon_list, type_list, dist_list, time_list, notes_list, link_list, pic_list):
    
    # define race_color icon and title based on the distance
    str_dist = str(dist)
    if str_dist in race_color_dict.keys():
        race_color = race_color_dict[str_dist]
    elif dist > 42.2:
        race_color = race_color_dict['ultra']
    else:
        race_color = race_color_dict['misc']
    
    # create the iFrame
    iframe = folium.IFrame(html=html_popup.format(race=race, date=date, loc=loc, typ=typ, dist=str_dist+' km', time=time, notes=notes, link=link, pic=pic, race_clr=race_color), width=450, height=300)
    
    # add marker to feature group
    fg.add_child(folium.Marker(location=[lt, ln], tooltip=race, popup=folium.Popup(iframe), icon = folium.Icon(color = race_color)))

# add feature group to map
run_map.add_child(fg)

# save map
run_map.save(run_map_html)
print("###### MAP SAVED #######")

# open html map in browser
webbrowser.open(run_map_html)