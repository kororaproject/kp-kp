%define git 38b8564

Name:           kp
Version:        0.1
Release:        1%{?dist}
Summary:        Korora Packaging Tool
License:        GPLv3
URL:            https://kororaproject.org/
Source0:        https://github.com/kororaproject/kp/tarball/%{git}
BuildArch:      noarch
Requires:       createrepo mock livecd-tools pykickstart rpm-sign

%description
Korora Package tool (called kp) is a bunch of shell scripts that wrap standard system commands 
(like git, mock and livecd-creator) to build Korora packages and images. 
Users should be running Korora or Fedora already, however which specific version generally doesn't matter.

%prep
%setup -q -n kororaproject-kp-%{git}

%build

%install
mkdir -p %{buildroot}%{_datadir}/share/%{name}
mkdir -p %{buildroot}%{_bindir}

ls

install -m 755 kp %{buildroot}%{_bindir}/kp
cp -r lib/* %{buildroot}%{_datadir}/share/%{name}/

%post

%postun

%files
%doc COPYING
%{_bindir}/kp
%{_datadir}/kp

%changelog
* Mon Jan 11 2016 Jim Dean <ozjd@kororaproject.org> 0.1-1
- Initial spec. 
