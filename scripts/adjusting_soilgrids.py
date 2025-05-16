
import pcraster as pcr

glcc_map   = "/projects/0/dfguu/users/edwin/data/glcc_olson_land_cover_map_and_table/Global_OlsonEcosystem_GLCC_30arc.map"
glcc_table = 
# table is taken from http://dx.doi.org/10.17617/2.2344576

# soil water capacity based on Hagemann
soil_water_capacity_hagemann = pcr.lookupscalar(glcc_table, glcc_map)

inputDir     = /projects/0/dfguu/users/edwin/data/pcrglobwb_input_arise/develop/

soilPropertiesNC = None
# - if soilPropertiesNC = None, the following soil parameters will be used
firstStorDepth       = europe_30sec/landSurface/soil/soilgrids/version_2021-02-XX/layerDepth_average_1_europe_30sec.nc
secondStorDepth      = europe_30sec/landSurface/soil/soilgrids/version_2021-02-XX/layerDepth_average_2_europe_30sec.nc
soilWaterStorageCap1 = europe_30sec/landSurface/soil/soilgrids/version_2021-02-XX/WHC_average_1_europe_30sec.nc
soilWaterStorageCap2 = europe_30sec/landSurface/soil/soilgrids/version_2021-02-XX/WHC_average_2_europe_30sec.nc
airEntryValue1       = europe_30sec/landSurface/soil/soilgrids/version_2021-02-XX/psiAir_average_1_europe_30sec.nc
airEntryValue2       = europe_30sec/landSurface/soil/soilgrids/version_2021-02-XX/psiAir_average_2_europe_30sec.nc
poreSizeBeta1        = europe_30sec/landSurface/soil/soilgrids/version_2021-02-XX/BCH_average_1_europe_30sec.nc
poreSizeBeta2        = europe_30sec/landSurface/soil/soilgrids/version_2021-02-XX/BCH_average_2_europe_30sec.nc
resVolWC1            = europe_30sec/landSurface/soil/soilgrids/version_2021-02-XX/vmcRes_average_1_europe_30sec.nc
resVolWC2            = europe_30sec/landSurface/soil/soilgrids/version_2021-02-XX/vmcRes_average_2_europe_30sec.nc
satVolWC1            = europe_30sec/landSurface/soil/soilgrids/version_2021-02-XX/vmcSat_average_1_europe_30sec.nc
satVolWC2            = europe_30sec/landSurface/soil/soilgrids/version_2021-02-XX/vmcSat_average_2_europe_30sec.nc
KSat1                = europe_30sec/landSurface/soil/soilgrids/version_2021-02-XX/kSat_average_1_europe_30sec.nc
KSat2                = europe_30sec/landSurface/soil/soilgrids/version_2021-02-XX/kSat_average_2_europe_30sec.nc


# soil water capacity based on soil grids
soilWaterStorageCap1 = pcr.readmap()
soilWaterStorageCap2 = pcr.readmap()

soil_water_capacity_soil_grids =  + soilWaterStorageCap1 + soilWaterStorageCap2 

depth_correction_factor = pcr.min(1.0, soil_water_capacity_hagemann / soil_water_capacity_soil_grids)

firstStorDepth  = 0.3
secondStorDepth = 1.2
corrected_totalDepth = depth_correction_factor * (firstStorDepth + secondStorDepth)

# adjust soil thickness
corrected_firstStorDepth  = pcr.max(0.05, pcr.min(corrected_totalDepth, firstStorDepth))
corrected_secondStorDepth = pcr.max(0.05, pcr.min(corrected_totalDepth - corrected_firstStorDepth, secondStorDepth))

# adjust porosity
corrected_satVolWC1       = satVolWC1 
corrected_satVolWC2       = pcr.ifthenelse(corrected_firstStorDepth < firstStorDepth, satVolWC1, satVolWC2)
# - TODO: CORRECT this as there is a chance that the new second soil layer crosses the 0.3 original soil thickness

# adjust airEntryValue, KSat and poreSizeBeta - as above

# recalculate soilWaterStorageCap
corrected_soilWaterStorageCap1 = corrected_firstStorDepth  / corrected_satVolWC1
corrected_soilWaterStorageCap2 = corrected_secondStorDepth / corrected_satVolWC2

# 

corrected_airEntryValue1       = 
corrected_airEntryValue2       = 
corrected_poreSizeBeta1        = 
corrected_poreSizeBeta2        = 
corrected_resVolWC1            = 
corrected_resVolWC2            = 
corrected_KSat1                = 
corrected_KSat2                = 

