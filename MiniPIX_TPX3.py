# -*- coding: utf-8 -*-
#
# This file is part of the MiniPIX_TPX3 project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

"""
MiniPIX_TPX3

"""

# PROTECTED REGION ID(MiniPIX_TPX3.system_imports) ENABLED START #
# PROTECTED REGION END #    //  MiniPIX_TPX3.system_imports

# PyTango imports
import tango
from tango import DebugIt
from tango.server import run
from tango.server import Device
from tango.server import attribute, command
from tango import AttrQuality, DispLevel, DevState
from tango import AttrWriteType, PipeWriteType
# Additional import
# PROTECTED REGION ID(MiniPIX_TPX3.additionnal_import) ENABLED START #
import os
import PixetAPI.pypixet as pypixet
import PixetAPI.pypxproc as pypxproc
# PROTECTED REGION END #    //  MiniPIX_TPX3.additionnal_import

__all__ = ["MiniPIX_TPX3", "main"]


class MiniPIX_TPX3(Device):
    """
    """
    # PROTECTED REGION ID(MiniPIX_TPX3.class_variable) ENABLED START #
    dev = None
    pixet = None
    # PROTECTED REGION END #    //  MiniPIX_TPX3.class_variable

    # ----------
    # Attributes
    # ----------

    Test = attribute(
        dtype='DevEncoded',
    )

    Image = attribute(
        dtype=(('DevDouble',),),
        max_dim_x=1800, max_dim_y=1800,
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        """Initializes the attributes and properties of the MiniPIX_TPX3."""
        Device.init_device(self)
        self._test = ['', '']
        self._image = ((0.0,),)
        # PROTECTED REGION ID(MiniPIX_TPX3.init_device) ENABLED START #
        # PROTECTED REGION END #    //  MiniPIX_TPX3.init_device

    def always_executed_hook(self):
        """Method always executed before any TANGO command is executed."""
        # PROTECTED REGION ID(MiniPIX_TPX3.always_executed_hook) ENABLED START #
        # PROTECTED REGION END #    //  MiniPIX_TPX3.always_executed_hook

    def delete_device(self):
        """Hook to delete resources allocated in init_device.

        This method allows for any memory or other resources allocated in the
        init_device method to be released.  This method is called by the device
        destructor and by the device Init command.
        """
        # PROTECTED REGION ID(MiniPIX_TPX3.delete_device) ENABLED START #
        # PROTECTED REGION END #    //  MiniPIX_TPX3.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def read_Test(self):
        # PROTECTED REGION ID(MiniPIX_TPX3.Test_read) ENABLED START #
        """Return the Test attribute."""
        return self._test
        # PROTECTED REGION END #    //  MiniPIX_TPX3.Test_read
    def read_Image(self):
        # PROTECTED REGION ID(MiniPIX_TPX3.Image_read) ENABLED START #
        """Return the Image attribute."""
        return self._image
        # PROTECTED REGION END #    //  MiniPIX_TPX3.Image_read
    # --------
    # Commands
    # --------


    @command(
    )
    @DebugIt()
    def Snap(self):
        # PROTECTED REGION ID(MiniPIX_TPX3.Snap) ENABLED START #
        """
        :rtype: PyTango.DevVoid
        """
        self._test = self.get_Sepectrum(3,1)
        pass
        # PROTECTED REGION END #    //  MiniPIX_TPX3.Snap

# ----------
# Run server
# ----------

# PROTECTED REGION ID(MiniPIX_TPX3.custom_code) ENABLED START #
    def get_Sepectrum(self, NumbFrame, Time_Frame):
        rc = self.dev.doSimpleAcquisition(NumbFrame, Time_Frame, self.pixet.PX_FTYPE_TPX3_PIXELS_ASCII, "test_2")
        return rc
# PROTECTED REGION END #    //  MiniPIX_TPX3.custom_code


def main(args=None, **kwargs):
    """Main function of the MiniPIX_TPX3 module."""
    # PROTECTED REGION ID(MiniPIX_TPX3.main) ENABLED START #
    return run((MiniPIX_TPX3,), args=args, **kwargs)
    # PROTECTED REGION END #    //  MiniPIX_TPX3.main

# PROTECTED REGION ID(MiniPIX_TPX3.custom_functions) ENABLED START #
# PROTECTED REGION END #    //  MiniPIX_TPX3.custom_functions


if __name__ == '__main__':
    main()
