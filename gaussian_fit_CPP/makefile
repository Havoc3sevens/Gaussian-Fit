OBJS1 = main.cpp

PROG1 = run

C = g++
#C = gcc

all: $(PROG1)

$(PROG1): $(OBJS1)
	$(C) -o $@ $(OBJS1) 

clean:
	rm -f $(PROG1) *.o *.dat *.mod

.SUFFIXES: $(SUFFIXES) .cpp
