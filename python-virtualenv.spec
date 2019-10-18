%define	module	virtualenv
%define __noautoprov '.*setuptools.*'

Summary:	Virtual Python Environment builder
Name:		python-%{module}
Version:	16.7.6
Release:	1
Group:		Development/Python
License:	MIT
Url:		http://pypi.python.org/pypi/virtualenv
Source0:	https://files.pythonhosted.org/packages/7f/8a/f0aaaff0d65330bac376f6c60e40387e6575eae1ee72b6c0dce87c6cc8ad/virtualenv-16.7.6.tar.gz
Source1:	virtualenv
Source2:	virtualenv2
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:  pkgconfig(python3)
BuildRequires:  python-pkg-resources
Requires:	pkgconfig(python3)
Requires:	rpm-build

%description
virtualenv is a tool to create isolated Python environments.

%package -n python2-%{module}
Summary:        Python 2 Virtual Python Env builder
BuildRequires:  pkgconfig(python2)
BuildRequires:  python2-pkg-resources
BuildRequires:  python2-setuptools
Requires:       pkgconfig(python2)

%description -n python2-%{module}
virtualenv is a tool to create isolated Python environments.
This is the package for python 2.x.

%prep
%setup -qn %{module}-%{version}

mkdir python2
mv `ls |grep -v python2` python2
cp -a python2 python3

%build
cd python2
%__python2 setup.py build

cd ../python3
%__python setup.py build

%install
cd python2
%__python2 setup.py install --root=%{buildroot} 
mv %{buildroot}%{_bindir}/virtualenv{,2.sh}
install -m755 %{SOURCE2} -D %{buildroot}%{_bindir}/virtualenv2

cd ../python3
PYTHONDONTWRITEBYTECODE=1 %__python setup.py install --root=%{buildroot}
mv %{buildroot}%{_bindir}/virtualenv{,.sh}
install -m755 %{SOURCE1} -D %{buildroot}%{_bindir}/virtualenv

%files
%doc python3/docs/*.rst
%{_bindir}/virtualenv
%{_bindir}/virtualenv.sh
%{py3_puresitedir}/virtualenv*
%{py3_puresitedir}/__pycache__/*.pyc

%files -n python2-%{module}
%{_bindir}/virtualenv2*
%{py2_puresitedir}/virtualenv*
