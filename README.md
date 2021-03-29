# Run Map
#### A map of all places where I took part in running events.


<p align="left">
  <a href="https://media.nathanael3d.com/dev/run_map/run_map.html" target="_blank"><img src="readme_preview.jpg" width="600" title="See full map"></a>
</p>

*Click picture to display full map*

The map is using the **Folium** python library. The base layer relies on **OpenStreetMap**.
https://python-visualization.github.io/folium/
https://www.openstreetmap.org/

All run events are loaded from a **CSV** file using read_csv() from the **Pandas** library. The CSV file contains all the pop-up informations, as well as event geographical coordinates (longitude, lattitude) used to place a marker on the map.
https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

When clicking on markers, a **pop-up** gives additonal information about the race (name, place, date, distance, time, event link, blog post, etc). The pop-up is using an **HTML template** from an external file and replaces its contents based on infos from the CSV file.

Events are color-coded based on the distance and a **legend** offers to blend them in and out.
