%global srcname docker

# In EPEL, many of the test suite requirements are either missing or too old.
%bcond_with tests

Name:           python-%{srcname}
Version:        2.5.0
Release:        1%{?dist}
Summary:        A Python library for the Docker Engine API
License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
Patch0:         remove-pip-dependency.patch
Patch1:         remove-environment-markers.patch
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
%if %{with tests}
BuildRequires:  python-mock >= 1.0.1
BuildRequires:  pytest >= 2.9.1
BuildRequires:  python-coverage >= 3.7.1
BuildRequires:  python-pytest-cov >= 2.1.0
BuildRequires:  python-flake8 >= 2.4.1
BuildRequires:  python-requests >= 2.5.2
BuildRequires:  python-six >= 1.4.0
BuildRequires:  python-websocket-client >= 0.32.0
BuildRequires:  python-docker-pycreds >= 0.2.1
BuildRequires:  python-backports-ssl_match_hostname
BuildRequires:  python-ipaddress
%endif

Requires:       python-requests >= 2.5.2
Requires:       python-six >= 1.4.0
Requires:       python-websocket-client >= 0.32.0
Requires:       python-docker-pycreds >= 0.2.1
Requires:       python-backports-ssl_match_hostname
Requires:       python-ipaddress

Provides:       python2-%{srcname} = %{version}-%{release}

Obsoletes:      python-docker-py < 2.0


%description
It lets you do anything the docker command does, but from within Python apps –
run containers, manage containers, manage Swarms, etc.


%prep
%autosetup -n %{srcname}-%{version} -p 1


%build
%py2_build


%install
%py2_install


%if %{with tests}
%check
%{__python2} -m pytest -v tests/unit/
%endif


%files
%license LICENSE
%doc README.md
%{python2_sitelib}/*


%changelog
* Tue Aug 22 2017 Carl George <carl@george.computer> - 2.5.0-1
- Latest upstream

* Tue Jul 25 2017 Carl George <carl@george.computer> - 2.4.2-1
- Initial package
