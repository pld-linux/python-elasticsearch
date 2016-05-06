#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define 	module	elasticsearch
Summary:	Client for Elasticsearch
Name:		python-%{module}
Version:	1.0.0
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/e/elasticsearch/elasticsearch-%{version}.tar.gz
# Source0-md5:	ac087d3f7a704b2c45079e7e25b56b9f
URL:		https://github.com/elasticsearch/elasticsearch-py
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with tests}
BuildRequires:	python-thrift >= 0.9.1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Low level client for Elasticsearch. It's goal is to provide common
ground for all Elasticsearch-related code in Python. The client's
features include:

- Translating basic Python data types to and from json
- Configurable automatic discovery of cluster nodes
- Persistent connections
- Load balancing (with pluggable selection strategy) across all
  available nodes
- Failed connection penalization (time based - failed connections
  won't be retried until a timeout is reached)
- Thread safety
- Pluggable architecture

%prep
%setup -qn %{module}-%{version}

rm -r %{module}.egg-info

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
