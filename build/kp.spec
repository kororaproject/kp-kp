%define git ac4b41d

Name:           kp
Version:        0.1
Release:        1%{?dist}
Summary:        Korora Packaging Tool
License:        GPLv3
URL:            https://kororaproject.org/
Source0:        https://github.com/kororaproject/kp
BuildArch:      noarch
Requires:       createrepo mock livecd-tools pykickstart

%description
Korora Package tool (called kp) is a bunch of shell scripts that wrap standard system commands 
(like git, mock and livecd-creator) to build Korora packages and images. 
Users should be running Korora or Fedora already, however which specific version generally doesn't matter.

%prep
%setup -q -n numixproject-numix-icon-theme-circle-%{git}


%build

%install
mkdir -p %{buildroot}%{_datadir}/icons/korora
cp -apR Numix-Circle/* %{buildroot}%{_datadir}/icons/korora
install %{SOURCE1} %{buildroot}%{_datadir}/icons/korora/scalable/apps/
chmod 644 %{buildroot}%{_datadir}/icons/korora/index.theme

%post
touch --no-create %{_datadir}/icons/korora &>/dev/null ||:

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/korora &>/dev/null
  gtk-update-icon-cache -q %{_datadir}/icons/korora &>/dev/null ||:
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/korora &>/dev/null ||:

%files
%doc license
%{_datadir}/icons/korora/*

%changelog
