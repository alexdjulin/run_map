import folium
import pandas
import webbrowser

# define paths to external files
run_map_html = "run_map.html"
popup_contents_html = "popup_contents.html"
events_cst = "events.csv"

# define race colors based on distance and store them in a dictionnary
race_color_dict = {
'5.0': "beige",
'10.0': "blue",
'21.1': "green",
'42.2': "red",
'ultra': "black",
'misc': "lightgray"
}

# load html popup contents
with open(popup_contents_html) as f:
    html_popup = f.read()

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
post_list = list(data["Post"])
pic_list = list(data["Picture"])

# calculate center of map based on race locations
start_lat = (min(lat_list)+max(lat_list))/2
start_lon = (min(lon_list)+max(lon_list))/2
run_map = folium.Map(location=[start_lat, start_lon], tiles="openstreetmap", zoom_start=6)

# create feature group
fg = folium.FeatureGroup(name="My Map")

# add markers based on csv file data
for date, race, loc, lt, ln, typ, dist, time, notes, link, post, pic in zip(date_list, race_list, loc_list, lat_list, lon_list, type_list, dist_list, time_list, notes_list, link_list, post_list, pic_list):
    
    # define race_color icon and title based on the distance
    str_dist = str(dist)
    race_color = ""
    
    if str_dist in race_color_dict.keys():
        race_color = race_color_dict[str_dist]
    elif dist > 42.2:
        race_color = race_color_dict['ultra']
    else:
        race_color = race_color_dict['misc']

    # delete the blog post line if link not in csv file
    if not str(post).lower().startswith('http'):
        html_contents = html_popup.replace("Read Blog Post", "")
    else:
        html_contents = html_popup

    iframe = folium.IFrame(html=html_contents.format(race=race, date=date, loc=loc, typ=typ, dist=str_dist+' km', time=time, notes=notes, link=link, post=post, pic=pic, race_clr=race_color), width=500, height=350)
    
    # add marker to feature group
    fg.add_child(folium.Marker(location=[lt, ln], tooltip=race, popup=folium.Popup(iframe), icon = folium.Icon(color = race_color)))

# add feature group to map
run_map.add_child(fg)

# save map
run_map.save(run_map_html)
print("###### MAP SAVED #######")

# open html map in browser
webbrowser.open(run_map_html)