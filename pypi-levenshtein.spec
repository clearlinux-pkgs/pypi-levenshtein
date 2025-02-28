#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v20
# autospec commit: e180208
#
Name     : pypi-levenshtein
Version  : 0.26.1
Release  : 7
URL      : https://files.pythonhosted.org/packages/97/e6/79807d3b59a67dd78bb77072ca6a28d8db0935161fecf935e6c38c5f6825/levenshtein-0.26.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/97/e6/79807d3b59a67dd78bb77072ca6a28d8db0935161fecf935e6c38c5f6825/levenshtein-0.26.1.tar.gz
Summary  : Python extension for computing string edit distances and similarities.
Group    : Development/Tools
License  : MIT
Requires: pypi-levenshtein-license = %{version}-%{release}
Requires: pypi-levenshtein-python = %{version}-%{release}
Requires: pypi-levenshtein-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : ninja
BuildRequires : pypi(scikit_build_core)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Levenshtein
<p>
<a href="https://github.com/rapidfuzz/Levenshtein/actions">
<img src="https://github.com/rapidfuzz/Levenshtein/workflows/Build/badge.svg"
alt="Continuous Integration">
</a>
<a href="https://pypi.org/project/levenshtein/">
<img src="https://img.shields.io/pypi/v/levenshtein"
alt="PyPI package version">
</a>
<a href="https://www.python.org">
<img src="https://img.shields.io/pypi/pyversions/levenshtein"
alt="Python versions">
</a>
<a href="https://rapidfuzz.github.io/Levenshtein">
<img src="https://img.shields.io/badge/-documentation-blue"
alt="Documentation">
</a>
<a href="https://github.com/rapidfuzz/Levenshtein/blob/main/COPYING">
<img src="https://img.shields.io/github/license/rapidfuzz/Levenshtein"
alt="GitHub license">
</a>
</p>

%package license
Summary: license components for the pypi-levenshtein package.
Group: Default

%description license
license components for the pypi-levenshtein package.


%package python
Summary: python components for the pypi-levenshtein package.
Group: Default
Requires: pypi-levenshtein-python3 = %{version}-%{release}

%description python
python components for the pypi-levenshtein package.


%package python3
Summary: python3 components for the pypi-levenshtein package.
Group: Default
Requires: python3-core
Provides: pypi(levenshtein)
Requires: pypi(rapidfuzz)

%description python3
python3 components for the pypi-levenshtein package.


%prep
%setup -q -n levenshtein-0.26.1
cd %{_builddir}/levenshtein-0.26.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1730166809
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-levenshtein
cp %{_builddir}/levenshtein-%{version}/extern/rapidfuzz-cpp/LICENSE %{buildroot}/usr/share/package-licenses/pypi-levenshtein/0375d56b18430f366cea90f3712664ccd180558c || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-levenshtein/0375d56b18430f366cea90f3712664ccd180558c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
