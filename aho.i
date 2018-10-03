%module aho
%{
	#include "aho.h"
%}
%include "stl.i"
%include "std_string.i"
%include "std_vector.i"
namespace std {
	%template(vs) vector<string>;
	%template(vi) vector<int>;
}
%include "std_map.i"
namespace std {
	%template(msvi) map < string, vector<int> >;
}
%clear std::map< std::string, std::vector<int> >;
%typemap(out) std::map< std::string, std::vector<int> > {
  $result = PyDict_New();

  int size = $1.size();

  std::map< std::string, std::vector<int> >::iterator iter;
  std::vector<int> idx;
  const char * hash;

  for (iter = $1.begin(); iter != $1.end(); ++iter) {
    hash = (iter->first).c_str();
    idx = iter->second;
    PyObject *value = PyList_New(idx.size());
	for (int i = 0; i < idx.size(); i++) {
		PyObject *o = PyInt_FromLong(idx[i]);
		PyList_SetItem(value, i, o);
	}

    PyDict_SetItem($result, PyString_FromString(hash), value);
  }
}

%include "aho.h"