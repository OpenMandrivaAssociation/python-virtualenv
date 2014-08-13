%define	module	virtualenv
%define __noautoprov '.*setuptools.*'

Summary:	Virtual Python Environment builder
Name:		python-%{module}
Version:	1.11.6
Release:	1
Group:		Development/Python
License:	MIT
Url:		http://pypi.python.org/pypi/virtualenv
Source0:	https://pypi.python.org/packages/source/v/virtualenv/%{module}-%{version}.tar.gz
Source1:	virtualenv
Source2:	virtualenv2
Patch0:		multiarch-1.8.2.patch
BuildArch:	noarch
BuildRequires:	python-setuptools
Requires:	pkgconfig(python)
Requires:	rpm-build

%description
virtualenv is a tool to create isolated Python environments.

%package -n python2-%{module}
Summary:        Python 2 Virtual Python Env builder
BuildRequires:  pkgconfig(python)
Requires:       pkgconfig(python2)

%description -n python2-%{module}
virtualenv is a tool to create isolated Python environments.
This is the package for python 2.x.

%prep
%setup -qn %{module}-%{version}
%apply_patches

mkdir python2
mv `ls |grep -v python2` python2
cp -a python2 python3

%build
cd python2
python2 setup.py build

cd ../python3
python3 setup.py build

%install
cd python2
python2 setup.py install --root=%{buildroot} 
mv %{buildroot}%{_bindir}/virtualenv{,2.sh}
install -m755 %{SOURCE2} -D %{buildroot}%{_bindir}/virtualenv2

cd ../python3
python3 setup.py install --root=%{buildroot}
mv %{buildroot}%{_bindir}/virtualenv{,.sh}
install -m755 %{SOURCE1} -D %{buildroot}%{_bindir}/virtualenv

%files
%doc python3/docs/*.rst
%{_bindir}/virtualenv
%{_bindir}/virtualenv.sh
%{_bindir}/virtualenv-3*
%{py3_puresitedir}/virtualenv*

%files -n python2-%{module}
%{_bindir}/virtualenv2*
%{_bindir}/virtualenv-2*
%{py2_puresitedir}/virtualenv*

