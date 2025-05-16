# soil_adjustment


scratch note for the general concept:

soil_water_capacity_hagemann

soil_water_capacity_soil_grids

https://www.researchgate.net/profile/Stefan-Hagemann-2/publication/27269130_An_Improved_Land_Surface_Parameter_Dataset_for_Global_and_Regional_Climate_Models/links/09e41505c535bce979000000/An-Improved-Land-Surface-Parameter-Dataset-for-Global-and-Regional-Climate-Models.pdf?_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6InB1YmxpY2F0aW9uIiwicGFnZSI6InB1YmxpY2F0aW9uIn19

# - using soilGrids
soilPropertiesNC    	= None
# - if soilPropertiesNC = None, the following soil parameters will be used
firstStorDepth      	= general/layerDepth_average_1_global_05arcmin.nc
secondStorDepth     	= general/layerDepth_average_2_global_05arcmin.nc
soilWaterStorageCap1	= general/WHC_average_1_global_05arcmin.nc
soilWaterStorageCap2	= general/WHC_average_2_global_05arcmin.nc
airEntryValue1      	= general/psiAir_average_1_global_05arcmin.nc
airEntryValue2      	= general/psiAir_average_2_global_05arcmin.nc
poreSizeBeta1       	= general/BCH_average_1_global_05arcmin.nc
poreSizeBeta2       	= general/BCH_average_2_global_05arcmin.nc
resVolWC1           	= general/vmcRes_average_1_global_05arcmin.nc
resVolWC2           	= general/vmcRes_average_2_global_05arcmin.nc
satVolWC1           	= general/vmcSat_average_1_global_05arcmin.nc
satVolWC2           	= general/vmcSat_average_2_global_05arcmin.nc
KSat1               	= general/kSat_average_1_global_05arcmin.nc
KSat2               	= general/kSat_average_2_global_05arcmin.nc

soil_water_capacity_soil_grids = soilWaterStorageCap1 + soilWaterStorageCap2
soil_water_capacity_hagemann from http://dx.doi.org/10.17617/2.2344576
depth_correction_factor = min(1.0, soil_water_capacity_hagemann / soil_water_capacity_soil_grids)
corrected_totalDepth 		= depth_correction_factor x ( firstStorDepth + secondStorDepth)
corrected_firstStorDepth 	= max(0.05, min(corrected_totalDepth, firstStorDepth))
corrected_secondStorDepth 	= max(0.05, min(corrected_totalDepth - corrected_firstStorDepth, secondStorDepth))
