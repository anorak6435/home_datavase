import dearpygui.dearpygui as dpg
# Feat: window settings
WIDTH = 600
HEIGHT = 200

dpg.create_context()
# Feat: Models window
with dpg.window(tag="Models_Overview", width=WIDTH, height=HEIGHT):
    dpg.add_text("Models:")
    with dpg.group(horizontal=True):
        dpg.add_group(tag="models_hook")
        with dpg.group(tag="right_plane"):
            with dpg.group(tag="model_details"):
                dpg.add_text("Create a Model:")
                dpg.add_input_text(tag="model_name", hint="Name")
                dpg.add_button(label="Create model")
                dpg.add_text("Model Details:")
                dpg.add_text("Model Attributes:")
                dpg.add_text("Add attribute")
                dpg.add_input_text(tag="newAttrName", hint="Name")
                dpg.add_input_text(tag="newAttrDatatype", hint="Datatype")
                dpg.add_button(label="Add Attribute")
                dpg.add_table(tag="Model_attribs")
                # load_model_attribs()
            dpg.add_separator()
            with dpg.group(tag="feature_details"):
                dpg.add_text("Features:")
# Feat: Scheme dataclasses
from dataclasses import dataclass
from typing import List
# Schemes
@dataclass
class ProgAttrib:
    name: str
    datatype: str

@dataclass
class ProgModel:
    name: str
    attribs : List[ProgAttrib]
# Feat: List_models
from operator import attrgetter
models = []
def list_selection():
    dpg.delete_item("Model_attribs", children_only=True)
    print("event!")
    selected_model = dpg.get_value("models_list")
    print(f"selected: '{selected_model}'")
    if selected_model == "":
        return

    model_index = list(map(attrgetter('name'), models)).index(selected_model)

def update_models():
    dpg.delete_item("models_hook", children_only=True)
    dpg.add_listbox(list(map(lambda m: m.name, models)), num_items=20, tag="models_list", parent="models_hook", callback=list_selection)
    # dpg.add_button(label="Delete model", callback=delete_selected_model, parent="models_hook")
    list_selection() # update the attribute values

update_models()
# Feat: display window

dpg.create_viewport(title='Home Datavase')
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Models_Overview", True)
dpg.start_dearpygui()
dpg.destroy_context()
