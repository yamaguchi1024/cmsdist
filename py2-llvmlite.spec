### RPM external py2-llvmlite 0.26.0x
## IMPORT build-with-pip

Requires: py2-enum34 llvm py2-wheel
%define source0     git+https://github.com/numba/llvmlite?obj=master/499a6aba18ab6c4d11ae279604d4a62454cfa8d4&export=llvmlite-%{realversion}&output=/source.tar.gz
%define PipPreBuild export LLVM_CONFIG=${LLVM_ROOT}/bin/llvm-config 
