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
