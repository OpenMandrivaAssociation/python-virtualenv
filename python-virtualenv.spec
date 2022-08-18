%define module virtualenv
%define __noautoprov '.*setuptools.*'

Summary:	Virtual Python Environment builder
Name:		python-%{module}
Version:	20.16.3
Release:	1
Group:		Development/Python
License:	MIT
Url:		http://pypi.python.org/pypi/virtualenv
Source0:	https://files.pythonhosted.org/packages/source/v/virtualenv/virtualenv-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
BuildRequires:	pkgconfig(python)
BuildRequires:	python-pkg-resources
BuildRequires:	python-pip
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(tomli)
Requires:	pkgconfig(python3)
Requires:	rpm-build

%description
virtualenv is a tool to create isolated Python environments.

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/virtualenv
%{py_puresitedir}/virtualenv*
