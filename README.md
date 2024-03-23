# create-markers-in-map-python-
#i didnt post for a year because i am studying for school since i want to go to a university.I will post projects every month because i like it
#here is the code and i will explain how i made it!
#we need folium so we can use a map
import folium 
#geocoder to get location
import geocoder
#tkinter for user GUI
import tkinter as tk
#to open browser when placing the marker
from webbrowser import open as open_in_browser
#store multiple markers
marker_data = []
#here we use geocoder
def get_current_location():
    try:
        g = geocoder.ip('me')
        return g.latlng
    except Exception as e:
        return None
#here we add the options for the markers 
def create_marker(map_instance, location, marker_type, marker_name):
    if location:
        icon = None
        if marker_type == "Blue Cloud":
            icon = folium.Icon(color="blue", icon="cloud")
        elif marker_type == "Red Cross":
            icon = folium.Icon(color="red", icon="cross")
        elif marker_type == "Green Leaf":
            icon = folium.Icon(color="green", icon="leaf")
        
        if icon:
            folium.Marker(
                location=location,
                popup=marker_name,
                icon=icon,
            ).add_to(map_instance)
            marker_data.append({"location": location, "type": marker_type, "name": marker_name})
    else:
        print("couldnt do it find a real location.")
#here we open the map
def open_map_in_browser(map_instance):
    map_instance.save("map.html")
    open_in_browser("map.html")
#the markers created are shown in the console
def show_markers_created():
    if marker_data:
        print("Markers Created:")
        for idx, marker in enumerate(marker_data):
            print(f"{idx + 1}. {marker['name']} ({marker['type']}) at {marker['location']}")
    else:
        print("No markers created yet.")
#with this the GUI opens
def main():
    location = get_current_location()
    if location:
        m = folium.Map(location=location, zoom_start=12)
        
        win = tk.Tk()
        win.geometry("400x300")
        
        marker_types = ["Blue Cloud", "Red Cross", "Green Leaf"]
        selected_marker_type = tk.StringVar(win)
        selected_marker_type.set(marker_types[0])  # default value
      #here we create the markers in the tk  
        def create_marker_from_input():
            lat = float(lat_entry.get())
            lon = float(lon_entry.get())
            marker_type = selected_marker_type.get()
            marker_name = name_entry.get()
            create_marker(m, [lat, lon], marker_type, marker_name)
            lat_entry.delete(0, tk.END)
            lon_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
        
        lat_label = tk.Label(win, text="Latitude:")
        lat_label.pack()
        lat_entry = tk.Entry(win)
        lat_entry.pack()
        
        lon_label = tk.Label(win, text="Longitude:")
        lon_label.pack()
        lon_entry = tk.Entry(win)
        lon_entry.pack()
        
        name_label = tk.Label(win, text="Marker Name:")
        name_label.pack()
        name_entry = tk.Entry(win)
        name_entry.pack()
        
        marker_type_label = tk.Label(win, text="Marker Type:")
        marker_type_label.pack()
        
        marker_type_menu = tk.OptionMenu(win, selected_marker_type, *marker_types)
        marker_type_menu.pack()
        
        create_marker_button = tk.Button(
            win,
            text='Create Marker',
            command=create_marker_from_input
        )
        create_marker_button.pack()
        
        show_markers_button = tk.Button(
            win,
            text='Show Markers Created',
            command=show_markers_created
        )
        show_markers_button.pack()
        
        def on_show_map_click():
            open_map_in_browser(m)
        
        show_map_button = tk.Button(
            win,
            text='Show Map in Browser',
            command=on_show_map_click
        )
        show_map_button.pack()
        
        win.mainloop()
    else:
        print("Couldn't find location")
#to run the program
if __name__ == "__main__":
    main()
