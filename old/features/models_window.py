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
