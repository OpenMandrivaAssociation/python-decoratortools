%define oname DecoratorTools

Summary:	Use class and function decorators -- even in Python 2.3
Name:		python-decoratortools
Version:	1.8
Release:	8
Group:		Development/Python
License:	Python or ZPLv2.1
Url:		http://cheeseshop.python.org/pypi/DecoratorTools
Source0:	http://cheeseshop.python.org/packages/source/D/DecoratorTools/%{oname}-%{version}.zip
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python2)

%description
Want to use decorators, but still need to support Python 2.3? Wish you could
have class decorators, decorate arbitrary assignments, or match decorated
function signatures to their original functions?
Then you need "DecoratorTools".

%prep
%setup -qn %{oname}-%{version}

%build
%{python2} setup.py build

%install
%{python2} setup.py install --skip-build --root %{buildroot}
 
%files
%doc README.txt
%{py_puresitedir}/*

