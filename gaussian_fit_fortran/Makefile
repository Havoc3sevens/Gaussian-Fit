
#OBJS1 = numtype.o setup.o temwave.o test.o
#
#PROG1 = run
#
#F95 = gfortran -fopenmp
#
#F95FLAGS = -O3 -funroll-loops  -fexternal-blas
#
#LIBS = -framework Accelerate
#
#LDFLAGS = $(LIBS)
#
#all: $(PROG1) 
#
#$(PROG1): $(OBJS1)
#	$(F95) $(LDFLAGS) -o $@ $(OBJS1) 
#
#clean:
#	rm -f $(PROG1) *.{o,mod}
#
#.SUFFIXES: $(SUFFIXES) .f95
#
#.f95.o:
#	$(F95) $(F95FLAGS) -c $<


OBJS1 =	numtype.o setup.o downhill-pe.o main.o

PROG1 = run

F95 = gfortran -fopenmp

F95FLAGS = -O3 -funroll-loops  -fexternal-blas

LIBS = -lblas -llapack # Linux

LDFLAGS = $(LIBS)

all: $(PROG1) 

$(PROG1): $(OBJS1)
	$(F95) -o $@ $(OBJS1) $(LDFLAGS) # Linux

clean:
	rm -f $(PROG1) fort.* *.o *.mod *.d # Linux

.SUFFIXES: $(SUFFIXES) .f95

.f95.o:
	$(F95) $(F95FLAGS) -c $<

