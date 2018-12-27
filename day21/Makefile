CXX = /usr/bin/c++
INCLDIRS =
LIBDIRS =
LIBS =
CFLAGS = -Wall -O3 $(INCLDIRS)
OBJECTS = chronal_conversion.o util.o

chronal_conversion: $(OBJECTS)

chronal_conversion.o: util.h
util.o: util.h

%.o: %.cpp
	$(CXX) $(CFLAGS) -c $<

chronal_conversion: $(OBJECTS)
	$(CXX) -o $@ $(OBJECTS) $(LIBDIRS) $(LIBS)

clean:
	rm -f *~
	rm -f *.o
	rm -f chronal_conversion
