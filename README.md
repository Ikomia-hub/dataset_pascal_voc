<div align="center">
  <img src="https://raw.githubusercontent.com/Ikomia-hub/dataset_pascal_voc/main/icons/logo_voc.png" alt="Algorithm icon">
  <h1 align="center">dataset_pascal_voc</h1>
</div>
<br />
<p align="center">
    <a href="https://github.com/Ikomia-hub/dataset_pascal_voc">
        <img alt="Stars" src="https://img.shields.io/github/stars/Ikomia-hub/dataset_pascal_voc">
    </a>
    <a href="https://app.ikomia.ai/hub/">
        <img alt="Website" src="https://img.shields.io/website/http/app.ikomia.ai/en.svg?down_color=red&down_message=offline&up_message=online">
    </a>
    <a href="https://github.com/Ikomia-hub/dataset_pascal_voc/blob/main/LICENSE.md">
        <img alt="GitHub" src="https://img.shields.io/github/license/Ikomia-hub/dataset_pascal_voc.svg?color=blue">
    </a>    
    <br>
    <a href="https://discord.com/invite/82Tnw9UGGc">
        <img alt="Discord community" src="https://img.shields.io/badge/Discord-white?style=social&logo=discord">
    </a> 
</p>

Load PascalVOC dataset. This algorithm converts a given dataset in PascalVOC 2012 format to Ikomia format.


## :rocket: Use with Ikomia API

#### 1. Install Ikomia API

We strongly recommend using a virtual environment. If you're not sure where to start, we offer a tutorial [here](https://www.ikomia.ai/blog/a-step-by-step-guide-to-creating-virtual-environments-in-python).

```sh
pip install ikomia
```

#### 2. Create your workflow

```python
import ikomia
from ikomia.dataprocess.workflow import Workflow

# Init your workflow
wf = Workflow()

# Add algorithm
algo = wf.add_task(name="dataset_pascal_voc")

algo.set_parameters({
    "annotation_folder": "path/to/annotation/folder",
    "dataset_folder": "path/to/image/folder",
    "class_file": "path/to/classes/file.txt",
})

train = wf.add_task(name="train_yolo_v8", auto_connect=True)

# Run on your image  
wf.run()
```

## :sunny: Use with Ikomia Studio

Ikomia Studio offers a friendly UI with the same features as the API.

- If you haven't started using Ikomia Studio yet, download and install it from [this page](https://www.ikomia.ai/studio).

- For additional guidance on getting started with Ikomia Studio, check out [this blog post](https://www.ikomia.ai/blog/how-to-get-started-with-ikomia-studio).

## :pencil: Set algorithm parameters


- **annotation_folder** (str): Path to the folder containing the annotation .xml files.
- **dataset_folder** (str): Path to the image folder.
- **instance_seg_folder** (str, *optional*): Path to segmentation masks folder‍.
- **class_file** (str) = Path to text file (.txt) containing class names.


**Parameters** should be in **strings format**  when added to the dictionary.


