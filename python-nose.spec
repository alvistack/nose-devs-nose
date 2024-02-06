# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-nose
Epoch: 100
Version: 1.3.7
Release: 1%{?dist}
BuildArch: noarch
Summary: Nose extends unittest to make testing easier
License: LGPL-2.1-or-later
URL: https://github.com/nose-devs/nose/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
nose extends the test loading and running features of unittest, making.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{_prefix}/man
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-nose
Summary: Nose extends unittest to make testing easier
Requires: python3
Provides: python3-nose = %{epoch}:%{version}-%{release}
Provides: python3dist(nose) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-nose = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(nose) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-nose = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(nose) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-nose
nose extends the test loading and running features of unittest, making.

%files -n python%{python3_version_nodots}-nose
%license lgpl.txt
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-nose
Summary: Nose extends unittest to make testing easier
Requires: python3
Provides: python3-nose = %{epoch}:%{version}-%{release}
Provides: python3dist(nose) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-nose = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(nose) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-nose = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(nose) = %{epoch}:%{version}-%{release}

%description -n python3-nose
nose extends the test loading and running features of unittest, making.

%files -n python3-nose
%license lgpl.txt
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
