%define oname DecoratorTools

Summary:	Use class and function decorators -- even in Python 2.3
Name:		python2-decoratortools
Version:	1.8
Release:	12
Group:		Development/Python
License:	Python or ZPLv2.1
Url:		https://cheeseshop.python.org/pypi/DecoratorTools
Source0:	http://cheeseshop.python.org/packages/source/D/DecoratorTools/%{oname}-%{version}.zip
BuildArch:	noarch
BuildRequires:	python2-setuptools
BuildRequires:	pkgconfig(python2)
%rename		python-decoratortools

%description
Want to use decorators, but still need to support Python 2.3? Wish you could
have class decorators, decorate arbitrary assignments, or match decorated
function signatures to their original functions?
Then you need "DecoratorTools".

%prep
%setup -qn %{oname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
 
%files
%doc README.txt
%{py2_puresitedir}/*
