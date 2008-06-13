%define oname virtualenv

Name:           python-virtualenv
Version:        1.1
Release:        %mkrel 1
Summary:        Virtual Python Environment builder

Group:          Development/Python
License:        MIT
URL:            http://pypi.python.org/pypi/virtualenv
Source0:        http://pypi.python.org/packages/source/v/virtualenv/%{oname}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:	noarch
BuildRequires:  python-devel
Requires:	python-devel, python

%description
virtualenv is a tool to create isolated Python environments.


%prep
%setup -q -n virtualenv-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc docs/index.txt docs/license.txt
%{_bindir}/*
%{py_puresitedir}/*
