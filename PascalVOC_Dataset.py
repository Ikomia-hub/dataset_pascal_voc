from ikomia import dataprocess


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits dataprocess.CPluginProcessInterface from Ikomia API
# --------------------
class PascalVOC_Dataset(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def getProcessFactory(self):
        from PascalVOC_Dataset.PascalVOC_Dataset_process import PascalVOC_DatasetProcessFactory
        # Instantiate process object
        return PascalVOC_DatasetProcessFactory()

    def getWidgetFactory(self):
        from PascalVOC_Dataset.PascalVOC_Dataset_widget import PascalVOC_DatasetWidgetFactory
        # Instantiate associated widget object
        return PascalVOC_DatasetWidgetFactory()
