%define	module	virtualenv
%define __noautoprov '.*setuptools.*'

Summary:	Virtual Python Environment builder
Name:		python-%{module}
Version:	20.0.20
Release:	1
Group:		Development/Python
License:	MIT
Url:		http://pypi.python.org/pypi/virtualenv
Source0:	https://files.pythonhosted.org/packages/cc/d4/b0e9c0926b08ae4d3f2439bae3c370917ff8c32fc254acf7023fd131eeb0/virtualenv-20.0.20.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:  pkgconfig(python3)
BuildRequires:  python-pkg-resources
Requires:	pkgconfig(python3)
Requires:	rpm-build

%description
virtualenv is a tool to create isolated Python environments.

%prep
%setup -qn %{module}-%{version}

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/virtualenv
%{py3_puresitedir}/virtualenv*
