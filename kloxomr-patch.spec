%define kloxo /usr/local/lxlabs/kloxo
%define productname kloxomr-patch
%define timestamp 2013032301

Name: %{productname}
Summary: Kloxo-MR web panel Patch
Version: 6.5.0.f
Release: %{timestamp}%{?dist}
License: GPL
Group: Applications/Internet

Source0: %{productname}-%{version}-%{timestamp}.tar.gz

BuildRoot: %{_tmppath}/%{productname}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
This is special edition (fork) of Kloxo with many features not existing on 
Kloxo official release (6.1.12+).

This fork named as Kloxo-MR (meaning 'Kloxo fork by Mustafa Ramadhan').

This is for 'patch' portion for final release.

%prep
%setup -q -n %{productname}-%{version}-%{timestamp}

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p -m0755 $RPM_BUILD_ROOT%{kloxo}/
%{__cp} -rp * $RPM_BUILD_ROOT%{kloxo}/

%clean
#%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,lxlabs,lxlabs,755)
%{kloxo}

%changelog
* Sat Mar 23 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031802.mr
- bug fix for installer.sh
