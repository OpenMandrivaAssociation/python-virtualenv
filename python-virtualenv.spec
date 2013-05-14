%define	module	virtualenv

%define __noautoprov '.*setuptools.*'

Name:		python-%{module}
Version:	1.8.2
Release:	6
Summary:	Virtual Python Environment builder
Group:		Development/Python
License:	MIT
URL:		http://pypi.python.org/pypi/virtualenv
Source0:	http://pypi.python.org/packages/source/v/virtualenv/%{module}-%{version}.tar.gz
Source1:	virtualenv
Patch0:		multiarch-1.8.2.patch
BuildArch:	noarch
BuildRequires:	python-setuptools
Requires:	pkgconfig(python2)
Requires:	rpm-build

%description
virtualenv is a tool to create isolated Python environments.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1 -b .multiarch~

%build
python setup.py build

%install
python setup.py install --root="%{buildroot}"
mv %{buildroot}%{_bindir}/virtualenv{,.sh}
install -m755 %{SOURCE1} -D %{buildroot}%{_bindir}/virtualenv

%files
%doc docs/*.txt
%{_bindir}/virtualenv*
%{py_sitedir}/virtualenv*
