all: compile link run

compile:
	g++ -c glad.c main.cpp

link:
	g++ main.o glad.o -o main -lGL -lGLU -lglfw -lX11 -lXxf86vm -lXrandr -lpthread -lXi -ldl

run:
	./main
