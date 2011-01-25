%define module	virtualenv
%define name	python-%{module}
%define version	1.5.1

Name:		%{name}
Version:	%{version}
Release:	%mkrel 4
Summary:	Virtual Python Environment builder
Group:		Development/Python
License:	MIT
URL:		http://pypi.python.org/pypi/virtualenv
Source0:	http://pypi.python.org/packages/source/v/virtualenv/%{module}-%{version}.tar.gz
Source1:	virtualenv
Patch0:		multiarch.patch
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
virtualenv is a tool to create isolated Python environments.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0 -b .multiarch

%build
PYTHONDONTWRITEBYTECODE= %{__python} setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot} --record=FILE_LIST
%__install -m 755 %SOURCE1 %{buildroot}%{_bindir}

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root,-)
%doc docs/*.txt
