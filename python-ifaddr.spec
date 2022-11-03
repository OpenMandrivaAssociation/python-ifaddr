Summary:	Python library that allows you to find all the IP addresses of the computer
Name:		python-ifaddr
Version:	0.2.0
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		https://pypi.org/project/ifaddr/
Source0:	https://files.pythonhosted.org/packages/source/i/ifaddr/ifaddr-%{version}.tar.gz
BuildRequires:	python3dist(setuptools)
BuildArch:	noarch

%description
ifaddr is a small Python library that allows you to find all the IP addresses of the computer.


%files
%{py_puresitedir}/ifaddr
%{py_puresitedir}/ifaddr*.egg-info

#------------------------------------------------------------
%prep
%autosetup -p1 -n ifaddr-%{version}

%build
%set_build_flags

export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%install
%{__python} setup.py \
	install \
	--root="%{buildroot}" --skip-build --optimize=1

%check
%{__python} setup.py \
	check
