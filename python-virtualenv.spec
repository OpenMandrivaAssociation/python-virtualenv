%define	module	virtualenv
%define __noautoprov '.*setuptools.*'

Summary:	Virtual Python Environment builder
Name:		python-%{module}
Version:	20.4.0
Release:	1
Group:		Development/Python
License:	MIT
Url:		http://pypi.python.org/pypi/virtualenv
Source0:	https://files.pythonhosted.org/packages/46/3d/81513f1aeab4c11c50d8c01ee041223350ddfad3d75eb05d0fce4a1d82dc/virtualenv-20.4.0.tar.gz
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
