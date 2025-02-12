# -*- coding: utf-8 -*-

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [GraduatedColorsRenderer]


###############DONT FORGET LINE 137

class GraduatedColorsRenderer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "graduatedcolor"
        self.description = "Creates a graduated colored map based on one of the attributes in a layer"
        self.canRunInBackground = False
        self.category = "MapTools"

    def getParameterInfo(self):
        """Define the tool parameters."""

        #original project name
            param0 = arcpy.Parameter(
                displayName="Input ArcGIS Pro Project Name",
                name="aprxInputName",
                datatype="DEFile",
                parameterType="Required",
                direction="Input"
            )
        
        #which layer you want to classify to create the color map
            param1 = arcpy.Parameter(
                displayName="Layer to Classify",
                name="LayertoClassify",
                datatype="GPLayer",
                parameterType="Required",
                direction="Input"
            )
        
        #output folder location
            param2 = arcpy.Parameter(
                displayName="Output Location",

            )
        params = None
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
