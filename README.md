# ADVACAM MiniPIX TPX3 - Tango Device Server

This repository contains the driver for controlling an ADVACAM MiniPIX TPX3 (Timepix3) detector with the Tango Control. The communication with the detector is done through the Pixet API (`pypixet`), whose DLLs and Python modules are in the [`PixetAPI`](PixetAPI) folder together with the API manuals (`APIManual.pdf`, `APIPythonManual.pdf`, `APIPxProcManual.pdf`).

## Installation

> **NOTE**: The Pixet API requires **Python 3.7** (the `pypixet.pyd` module is built for it). The virtual environment must be created with that version (Python 3.7.9 was used):

```
git clone https://github.com/Golp-Voxel/Tango-MiniPIX_TPX3.git
pip3.7 install virtualenv
python3.7 -m virtualenv py37-tango
```

If `python3.7` is not recognized as a command, see [this StackOverflow answer](https://stackoverflow.com/questions/39910730/python3-is-not-recognized-as-an-internal-or-external-command-operable-program).

After activating the environment (`py37-tango\Scripts\activate`), install `pytango` and `numpy`.

The Pixet API binaries are already included in the `PixetAPI` folder. The latest version can be downloaded from [ADVACAM downloads](https://advacam.com/downloads/). Note that the `lic.info` license file must match your detector.

On start-up (`init_device`) the server initializes the Pixet core, connects to the first detector found, and performs a test acquisition (`Snap`). If the acquisition fails, the device is set to the `DISABLE` state.

## Attributes

- [Image](#image)
- [Test](#test)

### Image

Read-only image attribute (`DevDouble`, up to 1800 x 1800). Reading this attribute performs an acquisition and returns the last acquired frame reshaped to the detector dimensions (256 x 256 for the MiniPIX).

```python
image = MiniPIX.Image
```

### Test

Read-only `DevEncoded` attribute holding the return code of the last test acquisition done by [Snap](#snap).

## Available commands

- [Snap](#snap)

### Snap

Performs a simple test acquisition of 1 frame with 1 second of exposure (saved as `test_2` in TPX3 pixels ASCII format) and stores the return code in the [Test](#test) attribute.

```python
Snap()
```

## Example of Tango Client code

```python
import tango
import numpy as np
import matplotlib.pyplot as plt

MiniPIX = tango.DeviceProxy(<MiniPIX_Tango_location_on_the_database>)
print(MiniPIX.state())
MiniPIX.set_timeout_millis(30000)

# Acquire and plot a frame
image = np.array(MiniPIX.Image)
plt.imshow(image)
plt.colorbar()
plt.show()
```

The notebook [`TestCom.ipynb`](TestCom.ipynb) contains a test of the communication with the device, and the `Images` folder has examples of ToA (Time of Arrival) and ToT (Time over Threshold) frames acquired with the detector.

# References

- [ADVACAM MiniPIX TPX3](https://advacam.com/camera/minipix-tpx3/)
- [Pixet API downloads](https://advacam.com/downloads/)
