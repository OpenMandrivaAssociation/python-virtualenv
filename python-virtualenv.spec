%define	module	virtualenv
%define __noautoprov '.*setuptools.*'

Summary:	Virtual Python Environment builder
Name:		python-%{module}
Version:	20.2.1
Release:	1
Group:		Development/Python
License:	MIT
Url:		http://pypi.python.org/pypi/virtualenv
Source0:	https://files.pythonhosted.org/packages/49/63/8e16d7f59ec7be34fbf57f9935e3ce1ab8b96cb6f1609ff30f16bbe7cf0d/virtualenv-20.2.1.tar.gz
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
