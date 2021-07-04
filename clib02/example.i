/* 
swig -c++ -python example.i (create 2 files: example_wrap.cxx, example.py)
python3 setup.py build_ext --inplace
*/

%module example
%{
#include "square.h"
%}
%include "square.h"