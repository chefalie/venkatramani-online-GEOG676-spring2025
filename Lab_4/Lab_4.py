##########importing arcpy 
import arcpy

##########setting workpath 
arcpy.env.workspace = r'C:\Mac\Home\Documents\GEOG676\repo\venkatramani-online-GEOG676-spring2025\Lab_4\codes_env'
folder_path = r'C:\Mac\Home\Documents\GEOG676\repo\venkatramani-online-GEOG676-spring2025\Lab_4'

##########setting up geodatabase of campus
gdb_name = 'Test.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

##########setting up csv file of garages on campus 
csv_path = r'C:\Mac\Home\Documents\GEOG676\repo\venkatramani-online-GEOG676-spring2025\Lab_4\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

##########copying the buildings to our gdb
campus = r'C:\Mac\Home\Documents\GEOG676\repo\venkatramani-online-GEOG676-spring2025\Lab_4\Campus.gdb'
buildings_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

##########Reprojection
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)

###########Buffering the garages
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_Points_buffered', 150)

###########Inrersect our buffer with the buildings 
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Building_Intersection', 'ALL')
arcpy.TableToTable_conversion(gdb_path + '\Garage_Building_Intersection.dbf', r'C:\Mac\Home\Documents\GEOG676\repo\venkatramani-online-GEOG676-spring2025\Lab_4', 'nearbyBuildings.csv')
