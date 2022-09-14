##ii)
#This script uses map algebra to find values in an
#elevation raster grater than 3500 (meters)
import arcpy
from arcpy.sa import *
#Specify the unput raster
inRaster = "C:/Users/HP 1030/Desktop/GIS_PRcticle/" #elevation data
cutoffElevation = 3500
#Check out the Spatial Analyst extension
arcpy.CheckOutExtension("Spatial")

#Make a map algebra expression and save the resulting raster
outRaster = Raster(inRaster) > cutoffElevation
outRaster.save ("C:/Users/HP 1030/Desktop/GIS_PRcticle/nameOfOutput")

#check in the spatial Analyst extension now that yoyu are done
arcpy.CheckInExtension("Spatial")
