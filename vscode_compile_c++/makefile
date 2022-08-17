CC   		=	g++
DEBUG   	=	-DUSE_DEBUG
CFLAGS  	=	-Wall -std=c++14

SOURCES   	:=	$(wildcard ./*.cpp)
SOURCES   	+=	$(wildcard ./unique_ptr/*.cpp)

INCLUDES  	:=	-I./unique_ptr/
INCLUDES	+=	-I./

OBJ   =$(patsubst %.cpp, %.o, $(SOURCES))
TARGET  =test

#links
$(TARGET):$(OBJ)
	$(CC) $(OBJ) -o $(TARGET) $(INCLUDES) $(DEBUG) $(CFLAGS)
	@echo -e "\033[32m -> build finish..\033[0m"
 
#compile
%.o: %.cpp
	$(CC) $(INCLUDES) $(DEBUG) -c $(CFLAGS) $< -o $@
	@echo -e "\033[33m -> ok: "$@"\033[0m"


.PHONY:clean exe px3

clean:
	@echo "Remove linked and compiled files......"
	rm -rf $(OBJ) $(TARGET)

exe:
	./${TARGET}

px3:
	