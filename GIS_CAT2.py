##This script runs the buffer tool.
#The user supplies the input and output path, and the buffer distance.
import arcpy
arcpy.env.overwriteOutput = True
try:
    #Get the input parameters for the Buffer tool
    inPath = arcpy.GetParameterAsText(0)
    outPath = arcpy.GetParameterAsText(1)
    bufferDistance = arcpy.GetParameterAsText(2)
    
    #Run the buffer tool
    arcpy.Buffer_analysis(inPath, outPath, bufferDistance)
    
    #Report a success message
    arcpy.AddMessage("All done")
except:
    #Report error messages
    arcpy.AddError("Could not complete the buffer")
    
    #Reort anyerror messages that the Buffer tool might have generated
    arcpy.AddMessage(arcpy.GetMessages())
    
