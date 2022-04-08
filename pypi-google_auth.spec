#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-google_auth
Version  : 2.6.3
Release  : 37
URL      : https://files.pythonhosted.org/packages/ad/48/37cd164bfdd85a3b18bb18d221642407d2b75bc317ea3d0b62a5a355c18a/google-auth-2.6.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/ad/48/37cd164bfdd85a3b18bb18d221642407d2b75bc317ea3d0b62a5a355c18a/google-auth-2.6.3.tar.gz
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
%setup -q -n google-auth-2.6.3
cd %{_builddir}/google-auth-2.6.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649376476
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . cachetools
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-google_auth
cp %{_builddir}/google-auth-2.6.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-google_auth/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} cachetools
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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
