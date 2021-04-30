from ikomia import core, dataprocess
from ikomia.dnn import datasetio, dataset
import copy
# Your imports below

# --------------------
# - Class to handle the process parameters
# - Inherits core.CProtocolTaskParam from Ikomia API
# --------------------
class PascalVOC_DatasetParam(core.CProtocolTaskParam):

    def __init__(self):
        core.CProtocolTaskParam.__init__(self)
        # Place default value initialization here
        self.annotation_folder_path = ""
        self.image_folder_path = ""
        self.instance_seg_folder_path = ""
        self.class_path = ""

    def setParamMap(self, paramMap):
        # Set parameters values from Ikomia application
        # Parameters values are stored as string and accessible like a python dict
        self.annotation_folder_path = paramMap["annotation_folder_path"]
        self.image_folder_path = paramMap["image_folder_path"]
        self.instance_seg_folder_path = paramMap["instance_seg_folder_path"]
        self.class_path = paramMap["class_path"]

    def getParamMap(self):
        # Send parameters values to Ikomia application
        # Create the specific dict structure (string container)
        paramMap = core.ParamMap()
        paramMap["annotation_folder_path"] = self.annotation_folder_path
        paramMap["image_folder_path"] = self.image_folder_path
        paramMap["instance_seg_folder_path"] = self.instance_seg_folder_path
        paramMap["class_path"] = self.class_path
        return paramMap


# --------------------
# - Class which implements the process
# - Inherits core.CProtocolTask or derived from Ikomia API
# --------------------
class PascalVOC_DatasetProcess(core.CProtocolTask):

    def __init__(self, name, param):
        core.CProtocolTask.__init__(self, name)
        # Add input/output of the process here
        self.addOutput(datasetio.IkDatasetIO("pascal_voc"))
        self.addOutput(dataprocess.CDblFeatureIO())

        # Create parameters class
        if param is None:
            self.setParam(PascalVOC_DatasetParam())
        else:
            self.setParam(copy.deepcopy(param))

    def getProgressSteps(self, eltCount=1):
        # Function returning the number of progress steps for this process
        # This is handled by the main progress bar of Ikomia application
        return 1

    def run(self):
        # Core function of your process
        # Call beginTaskRun for initialization
        self.beginTaskRun()

        # Get parameters :
        param = self.getParam()

        # Get dataset output :
        output = self.getOutput(0)
        output.has_bckgnd_class = True
        output.data = dataset.load_pascalvoc_dataset(param.annotation_folder_path,
                                                       param.image_folder_path,
                                                       param.instance_seg_folder_path,
                                                       param.class_path)

        # Class labels output
        numeric_out = self.getOutput(1)
        numeric_out.clearData()
        numeric_out.setOutputType(dataprocess.NumericOutputType.TABLE)

        class_ids = []
        for i in range(len(output.data["metadata"]["category_names"])):
            class_ids.append(i)

        numeric_out.addValueList(class_ids, "Id", list(output.data["metadata"]["category_names"].values()))

        # Step progress bar:
        self.emitStepProgress()

        # Call endTaskRun to finalize process
        self.endTaskRun()


# --------------------
# - Factory class to build process object
# - Inherits dataprocess.CProcessFactory from Ikomia API
# --------------------
class PascalVOC_DatasetProcessFactory(dataprocess.CProcessFactory):

    def __init__(self):
        dataprocess.CProcessFactory.__init__(self)
        # Set process information as string here
        self.info.name = "PascalVOC_Dataset"
        self.info.shortDescription = "Load PascalVOC dataset"
        self.info.description = "Load PascalVOC dataset. " \
                                "This plugin converts a given dataset in PascalVOC 2012 format to Ikomia format. " \
                                "Once loaded, all images can be visualized with their respective annotations. " \
                                "Then, any training algorithms from the Ikomia marketplace can be connected " \
                                "to this converter."
        self.info.authors = "Ikomia team"
        self.info.license = "MIT License"
        self.info.documentationLink = "http://host.robots.ox.ac.uk/pascal/VOC/"
        self.info.repo = "https://github.com/Ikomia-dev"
        # relative path -> as displayed in Ikomia application process tree
        self.info.path = "Plugins/Python/Dataset"
        self.info.iconPath = "icons/logo_voc.png"
        self.info.version = "1.1.0"
        self.info.keywords = "PascalVOC,dataset,annotation,train,dnn"

    def create(self, param=None):
        # Create process object
        return PascalVOC_DatasetProcess(self.info.name, param)
