### RPM external py2-pytest 3.8.0
## IMPORT build-with-pip

Requires: py2-more-itertools py2-atomicwrites py2-attrs py2-funcsigs py2-pathlib2 py2-pluggy py2-py py2-scandir
%define PipPostBuild perl -p -i -e "s|^#!.*python|#!/usr/bin/env python|" %{i}/bin/*
