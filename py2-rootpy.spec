### RPM external py2-rootpy 1.0.1
## IMPORT build-with-pip

%define doPython3 no
%define PipPostBuild \
   perl -p -i -e "s|^#!.*python|#!/usr/bin/env python|" %{i}/bin/rootpy %{i}/bin/roosh %{i}/bin/root2hdf5
Requires: python root py2-matplotlib root
