import folium
import geocoder
import tkinter as tk
from tkinter import messagebox
from webbrowser import open as open_in_browser

marker_data = []

def get_current_location():
    try:
        g = geocoder.ip('me')
        if g.latlng:
            return g.latlng
        return [40.6401, 22.9444]  
    except Exception:
        return [40.6401, 22.9444]

def create_marker(map_instance, location, marker_type, marker_name):
    icon_map = {
        "Blue Cloud": folium.Icon(color="blue",  icon="cloud"),
        "Red Cross":  folium.Icon(color="red",   icon="plus-sign"),
        "Green Leaf": folium.Icon(color="green", icon="leaf"),
    }
    icon = icon_map.get(marker_type)
    if icon:
        folium.Marker(
            location=location,
            popup=marker_name,
            tooltip=marker_name,
            icon=icon,
        ).add_to(map_instance)

        marker_data.append({
            "location": location,
            "type": marker_type,
            "name": marker_name
        })

def open_map_in_browser(map_instance):
    map_instance.save("map.html")
    open_in_browser("map.html")

def show_markers_created():
    if marker_data:
        print("\n--- Markers Created ---")
        for idx, marker in enumerate(marker_data):
            print(f"{idx + 1}. {marker['name']} ({marker['type']}) at {marker['location']}")
    else:
        print("No markers created yet.")

def main():
    location = get_current_location()
    m = folium.Map(location=location, zoom_start=12)

    win = tk.Tk()
    win.title("Map Marker Tool")
    win.geometry("400x340")
    win.resizable(False, False)

    marker_types = ["Blue Cloud", "Red Cross", "Green Leaf"]
    selected_marker_type = tk.StringVar(win)
    selected_marker_type.set(marker_types[0])

    def create_marker_from_input():
        # --- Validation ---
        lat_input = lat_entry.get().strip()
        lon_input = lon_entry.get().strip()

        if lat_input == "" and lon_input == "":
            # Χρήση default location όταν δεν δίνονται συντεταγμένες
            lat, lon = location[0], location[1]
        else:
            try:
                lat = float(lat_input)
                lon = float(lon_input)
            except ValueError:
                messagebox.showerror("Error", "Latitude and Longitude must be numbers!")
                return

            if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
                messagebox.showerror("Error", "Latitude must be -90 to 90, Longitude -180 to 180.")
                return

        marker_name = name_entry.get().strip()
        if not marker_name:
            messagebox.showerror("Error", "Please enter a marker name.")
            return

        marker_type = selected_marker_type.get()
        create_marker(m, [lat, lon], marker_type, marker_name)

        lat_entry.delete(0, tk.END)
        lon_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)

        # Feedback to user
        status_label.config(text=f"✓ Marker '{marker_name}' added!", fg="green")

    # --- UI ---
    tk.Label(win, text="Latitude:").pack()
    lat_entry = tk.Entry(win)
    lat_entry.pack()

    tk.Label(win, text="Longitude:").pack()
    lon_entry = tk.Entry(win)
    lon_entry.pack()

    tk.Label(win, text="Marker Name:").pack()
    name_entry = tk.Entry(win)
    name_entry.pack()

    tk.Label(win, text="Marker Type:").pack()
    tk.OptionMenu(win, selected_marker_type, *marker_types).pack()

    tk.Button(win, text="Create Marker", command=create_marker_from_input, bg="#4CAF50", fg="white").pack(pady=5)
    tk.Button(win, text="Show Markers in Console", command=show_markers_created).pack(pady=2)
    tk.Button(win, text="Open Map in Browser", command=lambda: open_map_in_browser(m), bg="#2196F3", fg="white").pack(pady=5)

    status_label = tk.Label(win, text="", fg="green")
    status_label.pack()

    win.mainloop()

if __name__ == "__main__":
    main()
