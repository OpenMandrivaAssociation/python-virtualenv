%define module virtualenv
%define name python-%{module}
%define version 1.8.2

Name:		%{name}
Version:	%{version}
Release:	5
Summary:	Virtual Python Environment builder
Group:		Development/Python
License:	MIT
URL:		http://pypi.python.org/pypi/virtualenv
Source0:	http://pypi.python.org/packages/source/v/virtualenv/%{module}-%{version}.tar.gz
Source1:	virtualenv
Patch0:		multiarch-1.8.2.patch
BuildArch:	noarch
#BuildRequires:	python-setuptools
Requires:	python-devel
Requires:	rpm-build

%description
virtualenv is a tool to create isolated Python environments.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1 -b .multiarch

%build
PYTHONDONTWRITEBYTECODE= %{__python} setup.py build

%install
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot}
mv %{buildroot}%{_bindir}/virtualenv %{buildroot}%{_bindir}/virtualenv.sh 
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}

%files
%doc docs/*.txt
%{_bindir}/virtualenv*
%{py_sitedir}/virtualenv*
