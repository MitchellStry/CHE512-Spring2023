all: md.exe

md.exe: md.o
	g++ -o md.exe md.o

md.o: md.cpp
	g++ -c md.cpp
     
clean:
	rm md.o md.exe
