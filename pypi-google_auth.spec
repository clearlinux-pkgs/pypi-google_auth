#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-google_auth
Version  : 2.17.1
Release  : 69
URL      : https://files.pythonhosted.org/packages/c8/ee/a028aa9ce069fe78d3cf8a86020d366fdb65b54fc33a9e317b4eafa1445e/google-auth-2.17.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/c8/ee/a028aa9ce069fe78d3cf8a86020d366fdb65b54fc33a9e317b4eafa1445e/google-auth-2.17.1.tar.gz
Summary  : Google Authentication Library
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-google_auth-license = %{version}-%{release}
Requires: pypi-google_auth-python = %{version}-%{release}
Requires: pypi-google_auth-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cachetools)
BuildRequires : pypi(pyasn1_modules)
BuildRequires : pypi(six)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Google Auth Python Library
==========================
|pypi|
This library simplifies using Google's various server-to-server authentication
mechanisms to access Google APIs.

%package license
Summary: license components for the pypi-google_auth package.
Group: Default

%description license
license components for the pypi-google_auth package.


%package python
Summary: python components for the pypi-google_auth package.
Group: Default
Requires: pypi-google_auth-python3 = %{version}-%{release}

%description python
python components for the pypi-google_auth package.


%package python3
Summary: python3 components for the pypi-google_auth package.
Group: Default
Requires: python3-core
Provides: pypi(google_auth)
Requires: pypi(cachetools)
Requires: pypi(pyasn1_modules)
Requires: pypi(rsa)
Requires: pypi(six)

%description python3
python3 components for the pypi-google_auth package.


%prep
%setup -q -n google-auth-2.17.1
cd %{_builddir}/google-auth-2.17.1
pushd ..
cp -a google-auth-2.17.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680224586
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . cachetools
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . cachetools
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-google_auth
cp %{_builddir}/google-auth-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-google_auth/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} cachetools
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-google_auth/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
