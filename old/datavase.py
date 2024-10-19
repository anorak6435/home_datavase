import dearpygui.dearpygui as dpg
from dataclasses import dataclass
from typing import List
from operator import attrgetter

# Schemes
@dataclass
class ProgAttrib:
    name: str
    datatype: str

@dataclass
class ProgModel:
    name: str
    attribs : List[ProgAttrib]


# App constants
WIDTH = 600
HEIGHT = 200

# Tracking global model values
models = []

dpg.create_context()

def model_creation_data_validation():
    name = dpg.get_value('model_name')
    if name == '':
        return False, ""
    return True, name
    
def attribute_ceation_data_validation():
    name = dpg.get_value('newAttrName')
    datatype = dpg.get_value('newAttrDatatype')

    current_model_name = dpg.get_value('models_list')

    if name == "" or datatype == "" or current_model_name == "":
        return False, None, None
    
    return True, name, datatype

    
def feature_creation_data_validation():
    name = dpg.get_value("feature_name")
    feat_type = dpg.get_value("new_feature_type")

    if name == "" or feat_type == "":
        return False, None, None
    
    return True, name, feat_type

def model_create():
    valid, name = model_creation_data_validation()
    if not valid:
        return
    dpg.set_value("model_name", "")
    print(f"Creating a model with name: {name}")
    models.append(ProgModel(name, []))
    update_models()

def attribute_create():
    valid, name, datatype = attribute_ceation_data_validation()
    if not valid:
        return
    
    # clear the input values
    dpg.set_value('newAttrName', "")
    dpg.set_value('newAttrDatatype', "")

    # add the attribute to the selected prog model

    current_model_name = dpg.get_value('models_list')

    edit_model_index = list(map(attrgetter('name'), models)).index(current_model_name)

    # set the attrib
    models[edit_model_index].attribs.append(ProgAttrib(name, datatype))


    load_model_attribs(edit_model_index)

def feature_create():
    valid, name, feat_type = feature_creation_data_validation()

    if not valid:
        return
    
    # clear the input values
    dpg.set_value("feature_name", "")

def attribute_delete(s, ad, index: int):
    print(f"delete attribute: {index}")

    current_model_name = dpg.get_value('models_list')

    edit_model_index = list(map(attrgetter('name'), models)).index(current_model_name)

    models[edit_model_index].attribs.pop(index)

    load_model_attribs(edit_model_index)

def delete_selected_model():
    selected_model = dpg.get_value("models_list")
    if selected_model == "":
        return
    
    model_index = list(map(attrgetter('name'), models)).index(selected_model)
    models.pop(model_index)

    update_models()

def list_selection():
    dpg.delete_item("Model_attribs", children_only=True)
    print("event!")
    selected_model = dpg.get_value("models_list")
    print(f"selected: '{selected_model}'")
    if selected_model == "":
        return

    model_index = list(map(attrgetter('name'), models)).index(selected_model)

    load_model_attribs(model_index)
    

def update_models():
    dpg.delete_item("models_hook", children_only=True)
    dpg.add_listbox(list(map(lambda m: m.name, models)), num_items=20, tag="models_list", parent="models_hook", callback=list_selection)
    dpg.add_button(label="Delete model", callback=delete_selected_model, parent="models_hook")
    list_selection()


def load_model_attribs(index=-1):
    dpg.delete_item("Model_attribs", children_only=True)
    dpg.add_table_column(tag="name_col", label="Name", parent="Model_attribs")
    dpg.add_table_column(tag="dtype", label="Datatype", parent="Model_attribs")
    dpg.add_table_column(tag="crud", label="Options", parent="Model_attribs")
    # Add model load
    if index == -1:
        return
    
    # I know there is a model selected in the models list
    attribs = models[index].attribs
    for i, attrib in enumerate(attribs):
        with dpg.table_row(parent="Model_attribs"):
            dpg.add_text(attrib.name)
            dpg.add_text(attrib.datatype)
            with dpg.group(horizontal=True):
                dpg.add_button(label="Delete", callback=attribute_delete, user_data=i)


with dpg.window(tag="Models_Overview", width=WIDTH, height=HEIGHT):
    dpg.add_text("Create a Model:")
    dpg.add_input_text(tag="model_name", hint="Name")
    dpg.add_button(label="Create model", callback=model_create)
    dpg.add_text("Models:")
    with dpg.group(horizontal=True):
        dpg.add_group(tag="models_hook")
        with dpg.group(tag="right_plane"):
            with dpg.group(tag="model_details"):
                dpg.add_text("Model Details:")
                dpg.add_text("Model Attributes:")
                dpg.add_text("Add attribute")
                dpg.add_input_text(tag="newAttrName", hint="Name")
                dpg.add_input_text(tag="newAttrDatatype", hint="Datatype")
                dpg.add_button(label="Add Attribute", callback=attribute_create)
                dpg.add_table(tag="Model_attribs")
                load_model_attribs()
            dpg.add_separator()
            with dpg.group(tag="feature_details"):
                dpg.add_text("Features:")

        update_models()

with dpg.window(tag="Features_Overview", width=WIDTH, height=HEIGHT):
    dpg.add_text("Create a Feature:")
    dpg.add_text("Features:")
    with dpg.group(horizontal=True):
        dpg.add_group(tag="features_hook")
        with dpg.group(tag="feature_details"):
                dpg.add_text("Feature Details:")
                dpg.add_text("Feature Attributes")
                dpg.add_input_text(tag="feature_name", hint="Name")
                dpg.add_combo(["IF", "OF", "UF"], tag="new_feature_type")
                dpg.add_button(label="Add Feature", callback=feature_create)

        
dpg.create_viewport(title='Home Datavase')
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Models_Overview", True)
dpg.start_dearpygui()
dpg.destroy_context()