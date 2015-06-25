SHEDSKIN_LIBDIR=/usr/share/shedskin/lib
CC=g++
CCFLAGS=-O2 -march=native -Wno-deprecated $(CPPFLAGS) -I. -I${SHEDSKIN_LIBDIR}
LFLAGS=-lgc -lpcre $(LDFLAGS)

CPPFILES=solution.cpp \
	${SHEDSKIN_LIBDIR}/re.cpp \
	${SHEDSKIN_LIBDIR}/builtin.cpp

HPPFILES=solution.hpp \
	${SHEDSKIN_LIBDIR}/re.hpp \
	${SHEDSKIN_LIBDIR}/builtin.hpp

all:	solution

solution:	$(CPPFILES) $(HPPFILES)
	$(CC)  $(CCFLAGS) $(CPPFILES) $(LFLAGS) -o solution

solution_prof:	$(CPPFILES) $(HPPFILES)
	$(CC) -pg -ggdb $(CCFLAGS) $(CPPFILES) $(LFLAGS) -o solution_prof

solution_debug:	$(CPPFILES) $(HPPFILES)
	$(CC) -g -ggdb $(CCFLAGS) $(CPPFILES) $(LFLAGS) -o solution_debug

clean:
	rm -f solution solution_prof solution_debug

.PHONY: all clean

