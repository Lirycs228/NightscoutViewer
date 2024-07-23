# Import StreamController modules
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder

# Import actions
from .actions.NightscoutLabelAction.NightscoutLabel import NightscoutLabel
from .actions.NightscoutGraphAction.NightscoutGraph import NightscoutGraph

# Import Library Objects
from .library.NightscoutConnector.NightscoutConnector import NightscoutConnector

import os
from loguru import logger as log 

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        # Register Library Objects
        self.NightscoutConnector = NightscoutConnector()

        ## Launch backend
        backend_path = os.path.join(self.PATH, "backend", "backend.py") 
        log.debug("Launching backend: ", backend_path)
        self.launch_backend(backend_path=backend_path, open_in_terminal=False)
        log.debug("Backend launched")

        ## Register actions
        self.nightscout_label_action_holder = ActionHolder(
            plugin_base = self,
            action_base = NightscoutLabel,
            action_id = "dev_lirycs_NightscoutViewer::NightscoutLabel", # Change this to your own plugin id
            action_name = "Nightscout Label",
        )
        self.add_action_holder(self.nightscout_label_action_holder)

        self.nightscout_graph_action_holder = ActionHolder(
            plugin_base = self,
            action_base = NightscoutGraph,
            action_id = "dev_lirycs_NightscoutViewer::NightscoutGraph", # Change this to your own plugin id
            action_name = "Nightscout Graph",
        )
        self.add_action_holder(self.nightscout_graph_action_holder)


        # Register plugin
        self.register(
            plugin_name = "Nightscout Viewer",
            github_repo = "https://github.com/Lirycs228/NightscoutViewer",
            plugin_version = "0.2.0",
            app_version = "1.0.0-alpha"
        )