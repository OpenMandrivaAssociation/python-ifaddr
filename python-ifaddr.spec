%define module ifaddr

Name:		python-ifaddr
Summary:	Python library that allows you to find all the IP addresses of the computer
Version:	0.2.0
Release:	3
Group:		Development/Python
License:	MIT
Url:		https://pypi.org/project/ifaddr/
Source0:	https://files.pythonhosted.org/packages/source/i/%{module}/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)

%description
ifaddr is a small Python library that allows you to find all the IP addresses of the computer.

%prep
%autosetup -p1 -n %{module}-%{version}
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%install
%py_install

%check
%{__python} setup.py \
	check

%files
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
