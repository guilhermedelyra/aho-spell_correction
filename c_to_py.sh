swig -c++ -python aho.i && g++ -c -fPIC aho_wrap.cxx  -I/usr/include/python2.7 -I/usr/lib/python2.7 &> out && g++ -shared -Wl,-soname,_aho.so -o _aho.so aho-corasick.o aho_wrap.o