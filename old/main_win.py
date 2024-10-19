import dearpygui.dearpygui as dpg

dpg.create_context()

WIDTH = 800
HEIGHT = 600

def delete_location(loc):
    print(loc)

def load_items(loc : str):
    # the item parameter given telling me what location to load items for
    pass

locations = ["no-location"]
for i in range(10):
    locations.append("Location: {loc}".format(loc=i))

with dpg.window(tag="location_col", no_title_bar=True, width=WIDTH/2, height=HEIGHT, no_move=True):
    dpg.add_text("Locations")
    selected_location = dpg.add_listbox(locations, default_value="no-location", num_items=20)
    with dpg.group(horizontal=True):
        delete_btn = dpg.add_button(label="Delete", callback=delete_location, enabled=False)
        add_btn = dpg.add_button(label="Add")

with dpg.window(tag="item_col", no_title_bar=True, pos=(WIDTH/2, 0), width=WIDTH/2, height=HEIGHT, no_move=True):
    dpg.add_text("Items")
    dpg.add_input_text(tag="searchitem", label="Search:")
    # dpg.add_listbox(items=load_items(dpg.get_value(selected_location)))

dpg.create_viewport(title='Home_datavase', width=WIDTH, height=HEIGHT)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
# while dpg.is_dearpygui_running():
#     # insert here any code you would like to run in the render loop
#     # you can manually stop by using stop_dearpygui()
#     # print("this will run every frame")
#     dpg.render_dearpygui_frame()

dpg.destroy_context()