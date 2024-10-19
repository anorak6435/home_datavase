# connect the different features
from dataclasses import dataclass
from typing import List

@dataclass
class FeatureFile:
    name: str

@dataclass
class Feature:
    name: str
    path: FeatureFile
    requires: List['Feature']

    def display(self, indent=0):
        print("  " * indent + self.name)
        for req in self.requires:
            req.display(indent+1)



def implement_features(features):
    combo = []
    for feature in features:
        # load the required features before the features that need them
        for req in feature.requires:
            combo = load_requirement(combo, req)
            
        # load the contents of the feature itself
        with open(feature.path.name, "r") as f:
            combo.extend(f.readlines())
    
    # when all the features are loaded in this way we can do the following.
    # write the combination of the files out to the 
    with open("./bin/output.py", "w") as wf:
        wf.write("".join(combo))
        

def load_requirement(combo, feature) -> list[str]:
    for req in feature.requires:
        combo = load_requirement(combo, req)
    
    # when it's requirements are loaded it itself is loaded
    with open(feature.path.name, "r") as f:
        combo.extend(f.readlines())


    # the combined result is given back to the top.
    return combo

features = []

import_dearpygui = Feature("import dearpygui", FeatureFile("./features/import_deargui.py"), [])

window_settings = Feature("window settings", FeatureFile("./features/window_settings.py"), [])

schemes = Feature("scheme dataclasses", FeatureFile("./features/schemes.py"), [])

list_models = Feature("list models", FeatureFile("./features/list_models.py"), [schemes])

models_window = Feature("Models window", FeatureFile("./features/models_window.py"), [])

show_window = Feature("show window", FeatureFile("./features/display_window.py"), [import_dearpygui, window_settings, models_window, list_models])



features.append(show_window)

print("Overview of the features to output:")
for feature in features:
    feature.display()

implement_features(features)