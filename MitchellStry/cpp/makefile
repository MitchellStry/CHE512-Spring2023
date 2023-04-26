all: hello.exe

hello.exe: main.o
	g++ -o hello.exe main.o

main.o: main.cpp
	g++ -c main.cpp

clean:
	rm main.o hello.exe

