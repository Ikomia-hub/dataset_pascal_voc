from ikomia import utils, core, dataprocess
from ikomia.utils import pyqtutils, qtconversion
from PascalVOC_Dataset.PascalVOC_Dataset_process import PascalVOC_DatasetParam
# PyQt GUI framework
from PyQt5.QtWidgets import *


# --------------------
# - Class which implements widget associated with the process
# - Inherits core.CProtocolTaskWidget from Ikomia API
# --------------------
class PascalVOC_DatasetWidget(core.CWorkflowTaskWidget):

    def __init__(self, param, parent):
        core.CWorkflowTaskWidget.__init__(self, parent)

        if param is None:
            self.parameters = PascalVOC_DatasetParam()
        else:
            self.parameters = param

        # Create layout : QGridLayout by default
        self.grid_layout = QGridLayout()

        self.browse_ann_folder = pyqtutils.append_browse_file(grid_layout=self.grid_layout, label="Annotation folder",
                                                              path=self.parameters.annotation_folder_path,
                                                              mode=QFileDialog.Directory)

        self.browse_img_folder = pyqtutils.append_browse_file(grid_layout=self.grid_layout, label="Image folder",
                                                              path=self.parameters.image_folder_path,
                                                              mode=QFileDialog.Directory)

        self.browse_instance_seg_folder = pyqtutils.append_browse_file(grid_layout=self.grid_layout,
                                                                       label="Instance segmentation folder",
                                                                       path=self.parameters.instance_seg_folder_path,
                                                                       mode=QFileDialog.Directory)

        self.browse_class_file = pyqtutils.append_browse_file(grid_layout=self.grid_layout, label="Classes file",
                                                              path=self.parameters.class_path,
                                                              mode=QFileDialog.ExistingFile)

        # PyQt -> Qt wrapping
        layout_ptr = qtconversion.PyQtToQt(self.grid_layout)

        # Set widget layout
        self.setLayout(layout_ptr)

    def onApply(self):
        # Apply button clicked slot
        # Get parameters from widget
        self.parameters.annotation_folder_path = self.browse_ann_folder.path
        self.parameters.image_folder_path = self.browse_img_folder.path
        self.parameters.instance_seg_folder_path = self.browse_instance_seg_folder.path
        self.parameters.class_path = self.browse_class_file.path

        # Send signal to launch the process
        self.emitApply(self.parameters)


# --------------------
# - Factory class to build process widget object
# - Inherits dataprocess.CWidgetFactory from Ikomia API
# --------------------
class PascalVOC_DatasetWidgetFactory(dataprocess.CWidgetFactory):

    def __init__(self):
        dataprocess.CWidgetFactory.__init__(self)
        # Set the name of the process -> it must be the same as the one declared in the process factory class
        self.name = "PascalVOC_Dataset"

    def create(self, param):
        # Create widget object
        return PascalVOC_DatasetWidget(param, None)
