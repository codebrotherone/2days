import folium
import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/codebrotherone/2days/master/data/locations.csv")

m = folium.Map(location=[31.6, 99.9], tiles="Mapbox Bright", zoom_start=3, min_zoom=3, max_zoom=10, max_bounds=True)
# I can add marker one by one on the map
for i in range(0,len(data)):
	folium.Marker([data.iloc[i]['latitude'], data.iloc[i]['longitude']], popup=data.iloc[i]['details']).add_to(m)
 
# Save it as html
m.save('folium_map.html')
