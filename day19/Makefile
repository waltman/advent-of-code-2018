CXX = /usr/bin/c++
INCLDIRS =
LIBDIRS =
LIBS =
CFLAGS = -Wall -O3 $(INCLDIRS)
OBJECTS = go_flow.o util.o

go_flow3: $(OBJECTS)

go_flow.o: util.h
util.o: util.h

%.o: %.cpp
	$(CXX) $(CFLAGS) -c $<

go_flow3: $(OBJECTS)
	$(CXX) -o $@ $(OBJECTS) $(LIBDIRS) $(LIBS)

