import folium
import webbrowser


class Map:
    def _init_(self, center, zoom_start, cords=[-33.6815736,-71.1998489], level_alert=0, help_message='Necesito ayuda urgente'):
        self.center = center
        self.zoom_start = zoom_start
        self.cords = cords
        self.level_alert = level_alert
        self.help_message = help_message
    
    def showMap(self):
        #Create the map
        my_map = folium.Map(location = self.center, zoom_start = self.zoom_start)
        folium.Marker(location=[-33.7004, -71.2162], icon=folium.Icon(color='lightgray', icon='home', prefix='fa')).add_to(my_map)
        folium.Marker(
            location=self.cords,
            popup=self.help_message,
            icon=folium.Icon(color='red' if self.level_alert == 1 else 'yelow', icon="info-sign"),
        ).add_to(my_map)

        #Display the map
        my_map.save("map.html")
        webbrowser.open("map.html")


#run cords... and zoom 
coords = [-33.6815736,-71.1998489]

map = Map(center = coords, zoom_start = 13, cords=coords, level_alert=1)
map.showMap()