# -*- coding: utf-8 -*-

import arcpy
import time

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [GraduatedColorsRenderer]

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
            name="OutputLocation",
            datatype="DEFolder",
            direction="Input"
        )

        #output project name
        param3 = arcpy.Parameter(
            displayName="Output Project Name",
            name="OutputProjectName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
    
        params = [param0, param1, param2, param3]
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
        #Define Progressor Variables
        readTime = 3 #the time for users to read progress
        start = 0 #beginning position of the progressor
        max = 100 #end position
        step = 33 #the progresso interval to move the progressor along 

        #Setup Progressor
        arcpy.SetProgressor("step", "Validating Project File...", start, max, step)
        time.sleep(readTime) # pause the execution for 2.5 seconds 
        #Add message to the results pain
        arcpy.AddMessage("Validating Project File...")

        #Project File
        project = arcpy.mp.ArcGISProject(parameters[0].valueAsText) #param0 is the input project file

        #Grabs the First Instance of a Map from the .aprx
        campus = project.listMaps('Map')[0] #access to the first map

        #Increment Progressor
        arcpy.SetProgressorPosition(start + step)
        arcpy.SetProgressorLabel("Finding your map layer...")
        time.sleep(readTime)
        arcpy.AddMessage("Finding your map layer...")

        #Loop through the layers of the map
        for layer in campus.listLayers():
            #Check if the Layer is a Feature Layer
            if layer.isFeatureLayer:
                #Copy the layer's symbology
                symbology = layer.symbology
                #Make sure the symbology has renderer attribute
                if hasattr(symbology, 'renderer'):
                    #Check layer name
                    if layer.name == parameters[1].valueAsText: #check if the layer name matches the input later 

                        #Increment Progressor
                        arcpy.SetProgressorPosition(start + step*2) #now is 66%
                        arcpy.SetProgressorLabel("Calculating and classifying...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Calculating and classifying...")

                        #Update the Copy's Renderer to "Graduated Colors Renderer"
                        symbology.updateRenderer('GraduatedColorsRenderer')

                        #Tell arcpy which field we want to base our chloropleth off of 
                        symbology.renderer.classificationField = "Shape_Area"

                        #Increment Progressor
                        arcpy.SetProgressorPosition(start + step*2) #now is 66%
                        arcpy.SetProgressorLabel("Cleaning up...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Cleaning up...")

                        #Set how many classes in the map
                        symbology.renderer.breakCount = 5
                        symbology.renderer.colorRamp = project.listColorRamps('Blues (5 Classes)')[0]

                        #Set the Layer's Actual Symbology Equal to the Copy;s
                        layer.symbology = symbology

                        arcpy.AddMessage("Finish Generating Layer...")
                    else:
                        print("NO layers found")

        #Increment Progressor
        arcpy.SetProgressorPosition(start + step*3) #now is 99% completed
        arcpy.SetProgressorLabel("Saving...")
        time.sleep(readTime)
        arcpy.AddMessage("Saving...")

        project.saveACopy(parameters[2].valueAsText + "\\" + parameters[3].valueAsText + ".aprx")
        #Param 2 is the folder location and param 3 is the name of the new project
        return
    
    def postExecute(self, parameters):
        return

print("Map Created Successfully!    ...congrats i guess")