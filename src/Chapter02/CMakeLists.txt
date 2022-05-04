project(Chapter02)
MESSAGE("------------------------Chapter02")

FILE(GLOB PROJECT_SOURCE_FILES ${PROJECT_SOURCE_FILES}
    *.cpp
	*.h
	*.txt
    )
	
ADD_EXECUTABLE(Chapter02 ${PROJECT_SOURCE_FILES})
SET(EXECUTABLE_OUTPUT_PATH ${BIN_DIR})

TARGET_LINK_LIBRARIES(${PROJECT_NAME} 
debug SDL2 
debug SDL2_image 
debug SDL2_mixer 
debug SDL2_ttf 
debug SDL2main 
debug SDL2test 
optimized SDL2 
optimized SDL2_image 
optimized SDL2_mixer 
optimized SDL2_ttf 
optimized SDL2main 
optimized SDL2test)

set_property(TARGET ${PROJECT_NAME} PROPERTY FOLDER "Chapter02")









