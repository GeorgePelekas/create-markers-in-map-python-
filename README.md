# create-markers-in-map-python-
#i didnt post for a year because i am studying for school since i want to go to a university.I will post projects every month because i like it
#here is the code and i will explain how i made it!
#need folium to create map
import folium 
#need geocoder to find location
import geocoder
#need tkinter so i can create an user input
import tkinter as tk
#so when you run the programm the browser opens automatically
from webbrowser import open as open_in_browser

#getting your location
def get_current_location():
    try:
        g = geocoder.ip('me')
        return g.latlng
    except Exception as e:
        return None
#creating markers 
def create_marker(map_instance, location):
    if location:
        folium.Marker(
            location=location,
            popup="Marker",
            icon=folium.Icon(color="blue", icon="cloud"),
        ).add_to(map_instance)
    else:
        print("location isn't available.")
#opening map
def open_map_in_browser(map_instance):
    map_instance.save("map.html")
    open_in_browser("map.html")

def main():
    location = get_current_location()
    if location:
        m = folium.Map(location=location, zoom_start=12)
        
        win = tk.Tk()
        win.geometry("300x150")
        
        def create_marker_from_input():
            lat = float(lat_entry.get())
            lon = float(lon_entry.get())
            create_marker(m, [lat, lon])
        
        lat_label = tk.Label(win, text="Latitude:")
        lat_label.pack()
        lat_entry = tk.Entry(win)
        lat_entry.pack()
        
        lon_label = tk.Label(win, text="Longitude:")
        lon_label.pack()
        lon_entry = tk.Entry(win)
        lon_entry.pack()
        
        create_marker_button = tk.Button(
            win,
            text='Create Marker',
            command=create_marker_from_input
        )
        create_marker_button.pack()
        
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
        print("couldnt find location")

if __name__ == "__main__":
    main()
