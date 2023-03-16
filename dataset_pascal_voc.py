from ikomia import dataprocess


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits dataprocess.CPluginProcessInterface from Ikomia API
# --------------------
class IkomiaPlugin(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def get_process_factory(self):
        from dataset_pascal_voc.dataset_pascal_voc_process import DatasetPascalVocFactory
        # Instantiate process object
        return DatasetPascalVocFactory()

    def get_widget_factory(self):
        from dataset_pascal_voc.dataset_pascal_voc_widget import DatasetPascalVocWidgetFactory
        # Instantiate associated widget object
        return DatasetPascalVocWidgetFactory()
