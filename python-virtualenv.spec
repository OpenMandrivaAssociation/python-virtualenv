%define	module	virtualenv
%define __noautoprov '.*setuptools.*'

Summary:	Virtual Python Environment builder
Name:		python-%{module}
Version:	1.8.2
Release:	10
Group:		Development/Python
License:	MIT
Url:		http://pypi.python.org/pypi/virtualenv
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
%setup -qn %{module}-%{version}
%apply_patches

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

