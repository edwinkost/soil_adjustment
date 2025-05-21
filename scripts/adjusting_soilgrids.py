
import pcraster as pcr
import os

output_folder = "/scratch-shared/edwin/test_adjust_soil_grids/"
cmd = "mkdir -p " + output_folder
os.system(cmd)

# rooting depth (m)
rooting_depth_file = "/projects/0/dfguu/users/edwin/data/pcrglobwb_input_arise/develop/europe_30sec/landSurface/landCover/naturalVegetationAndRainFedCrops/version_2020-12-XX/meanrootdepth_all.map"
rooting_depth = pcr.readmap(rooting_depth_file)

# set the minimum rooting depth to 10 cm
rooting_depth = pcr.roundup(rooting_depth * 10.) / 10.
rooting_depth = pcr.max(0.1, rooting_depth)

# set the maximum rooting depth to 150 cm
rooting_depth = pcr.min(1.5, rooting_depth)

# original soil grids
firstStorDepth       = 0.3 
secondStorDepth      = 1.2 
resVolWC1            = 0.0 
resVolWC2            = 0.0 
satVolWC1            = pcr.readmap("/projects/0/dfguu/users/edwin/data/pcrglobwb_input_arise/develop/europe_30sec//landSurface/soil/soilgrids/version_2021-02-XX//maps/vmcSat_average_1_europe_30sec.map"    )
satVolWC2            = pcr.readmap("/projects/0/dfguu/users/edwin/data/pcrglobwb_input_arise/develop/europe_30sec//landSurface/soil/soilgrids/version_2021-02-XX//maps/vmcSat_average_2_europe_30sec.map"    )
KSat1                = pcr.readmap("/projects/0/dfguu/users/edwin/data/pcrglobwb_input_arise/develop/europe_30sec//landSurface/soil/soilgrids/version_2021-02-XX//maps/kSat_average_1_europe_30sec.map"      )
KSat2                = pcr.readmap("/projects/0/dfguu/users/edwin/data/pcrglobwb_input_arise/develop/europe_30sec//landSurface/soil/soilgrids/version_2021-02-XX//maps/kSat_average_2_europe_30sec.map"      )
airEntryValue1       = pcr.readmap("/projects/0/dfguu/users/edwin/data/pcrglobwb_input_arise/develop/europe_30sec//landSurface/soil/soilgrids/version_2021-02-XX//maps/psiAir_average_1_europe_30sec.map"    )
airEntryValue2       = pcr.readmap("/projects/0/dfguu/users/edwin/data/pcrglobwb_input_arise/develop/europe_30sec//landSurface/soil/soilgrids/version_2021-02-XX//maps/psiAir_average_2_europe_30sec.map"    )
poreSizeBeta1        = pcr.readmap("/projects/0/dfguu/users/edwin/data/pcrglobwb_input_arise/develop/europe_30sec//landSurface/soil/soilgrids/version_2021-02-XX//maps/BCH_average_1_europe_30sec.map"       )
poreSizeBeta2        = pcr.readmap("/projects/0/dfguu/users/edwin/data/pcrglobwb_input_arise/develop/europe_30sec//landSurface/soil/soilgrids/version_2021-02-XX//maps/BCH_average_2_europe_30sec.map"       )
soilWaterStorageCap1 = pcr.readmap("/projects/0/dfguu/users/edwin/data/pcrglobwb_input_arise/develop/europe_30sec//landSurface/soil/soilgrids/version_2021-02-XX//maps/WHC_average_1_europe_30sec.map"       )
soilWaterStorageCap2 = pcr.readmap("/projects/0/dfguu/users/edwin/data/pcrglobwb_input_arise/develop/europe_30sec//landSurface/soil/soilgrids/version_2021-02-XX//maps/WHC_average_2_europe_30sec.map"       )


# get the corrected thickness for the first soil layer
corrected_firstStorDepth = pcr.min(rooting_depth, firstStorDepth)
# - set the minimum thickness to 5 cm
corrected_firstStorDepth = pcr.max(0.05, corrected_firstStorDepth)
pcr.report(corrected_firstStorDepth , output_folder + "corrected_firstStorDepth.map")

# get the corrected thickness for the second soil layer
corrected_secondStorDepth = pcr.min(rooting_depth - corrected_firstStorDepth, secondStorDepth)
# - set the minimum thickness to 5 cm
corrected_secondStorDepth = pcr.max(0.05, corrected_secondStorDepth)
pcr.report(corrected_secondStorDepth , output_folder + "corrected_secondStorDepth.map")

# recalculate the total thickness, set the maximum to 150 cm
corrected_totalDepth = pcr.min(1.5, corrected_firstStorDepth + corrected_secondStorDepth)
check = corrected_totalDepth - (corrected_firstStorDepth + corrected_secondStorDepth)
pcr.aguila(check) 

# corrected properties for the first soil layer
corrected_satVolWC1            = satVolWC1
corrected_KSat1                = KSat1
corrected_airEntryValue1       = airEntryValue1
corrected_poreSizeBeta1        = poreSizeBeta1
corrected_soilWaterStorageCap1 = corrected_satVolWC1 * corrected_firstStorDepth

# corrected properties for the second soil layer
corrected_satVolWC2            = pcr.ifthenelse(corrected_firstStorDepth <= 0.3, satVolWC1     , satVolWC2)
corrected_KSat2                = pcr.ifthenelse(corrected_firstStorDepth <= 0.3, KSat1         , KSat12)
corrected_airEntryValue2       = pcr.ifthenelse(corrected_firstStorDepth <= 0.3, airEntryValue1, airEntryValue2)
corrected_poreSizeBeta2        = pcr.ifthenelse(corrected_firstStorDepth <= 0.3, poreSizeBeta1 , poreSizeBeta2)
corrected_soilWaterStorageCap2 = corrected_satVolWC2 * corrected_secondStorDepth
