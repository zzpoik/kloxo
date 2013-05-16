%define kloxo /usr/local/lxlabs/kloxo
%define productname kloxomr
%define timestamp 2013031813

Name: %{productname}
Summary: Kloxo-MR web panel
Version: 6.5.0.f
Release: %{timestamp}%{?dist}
License: GPL
Group: Applications/Internet

Source0: %{name}-%{version}-%{timestamp}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
This is special edition (fork) of Kloxo with many features not existing on 
Kloxo official release (6.1.12+).

This fork named as Kloxo-MR (meaning 'Kloxo fork by Mustafa Ramadhan').

%prep
%setup -q -n %{name}-%{version}-%{timestamp}

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p -m0755 $RPM_BUILD_ROOT%{kloxo}/
%{__cp} -rp * $RPM_BUILD_ROOT%{kloxo}/
%{__mkdir} -p $RPM_BUILD_ROOT/script/
%{__cp} -rp $RPM_BUILD_ROOT%{kloxo}/pscript/* $RPM_BUILD_ROOT/script/
%{__cp} -rp $RPM_BUILD_ROOT%{kloxo}/httpdocs/htmllib/script/* $RPM_BUILD_ROOT/script/

%clean
#%{__rm} -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/useradd -s /sbin/nologin -M -r -d /home/lxlabs/ \
    -c "Kloxo-MR Website Control Panel" lxlabs &>/dev/null || :

%files
%defattr(644,lxlabs,lxlabs,755)
%{kloxo}
%defattr(644,root,root,755)
/script

%post

# this is for fresh install
if [ "$1" = "1" ]; then
	if [ -f /var/lib/mysql/kloxo ] ; then
		# but previous version already exists
		echo
		echo "_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/"
		echo "_/                                                                        _/"
		echo "_/  ..:: Kloxo-MR Web Panel ::..                                          _/"
		echo "_/                                                                        _/"
		echo "_/  Attention:                                                            _/"
		echo "_/                                                                        _/"
		echo "_/  Run 'sh /script/cleanup' for to make sure running well                _/"
		echo "_/  or 'sh /script/cleanup-simple' (cleanup without fix services configs  _/"
		echo "_/                                                                        _/"
		echo "_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/"
		echo
	else
		# real fresh install
		echo
		echo "_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/"
		echo "_/                                                                        _/"
		echo "_/  ..:: Kloxo-MR Web Panel ::..                                          _/"
		echo "_/                                                                        _/"
		echo "_/  Attention:                                                            _/"
		echo "_/                                                                        _/"
		echo "_/  Run 'sh /usr/local/lxlabs/kloxo/install/setup.sh' completely install  _/"
		echo "_/                                                                        _/"
		echo "_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/"
		echo
	fi
elif [ "$1" = "2" ]; then
	# yum update
	echo
	echo "_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/"
	echo "_/                                                                        _/"
	echo "_/  ..:: Kloxo-MR Web Panel ::..                                          _/"
	echo "_/                                                                        _/"
	echo "_/  Attention:                                                            _/"
	echo "_/                                                                        _/"
	echo "_/  Run 'sh /script/cleanup' for to make sure running well                _/"
	echo "_/  or 'sh /script/cleanup-simple' (cleanup without fix services configs  _/"
	echo "_/                                                                        _/"
	echo "_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/"
	echo
fi

%changelog
* Thu May 16 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031813.mr
- fix sh permission to 755; fix www redirect; make simple awstats link
- add mariadb in mysql branch; disable mariadb from centalt repo (conflict when install)
- based on 6.5.1.a-2013050502 and 6.5.1.a-2013051601

* Sun May 5 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031812.mr
- update suphp config (fix for possible security issue) and remove delete spamassassin dirs
- based on 6.5.1.a-2013050501 and 6.5.1.a-2013050502

* Fri Apr 26 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031811.mr
- fix packer.sh (remove lang except en-us); use ionice for du
- based on 6.5.1.a-2013042601 and 6.5.1.a-2013042602

* Sun Apr 21 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031810.mr
- fix some script based-on 6.5.1.a-2013042001 and 6.5.1.a-2013042101

* Mon Apr 8 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031809.mr
- fix some script based-on 6.5.1.a-2013040801

* Sat Mar 30 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031808.mr
- fix install issue on openvz

* Wed Mar 27 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031807.mr
- fix traffic issue and installer.sh/installer.php; add some scripts

* Mon Mar 25 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031806.mr
- no need cleanup on installer/setup also change mysqli to mysql on reset password

* Mon Mar 25 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031805.mr
- no need running full installer.sh twice just function step2 if running setup.sh

* Mon Mar 25 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031804.mr
- fix bugs relate to install/setup

* Sat Mar 23 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031803.mr
- remove php modules (except php-pear) because conflict between centos and other repos

* Sat Mar 23 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031802.mr
- fix critical bug (don't install php-mysqli on install/setup process)

* Mon Mar 18 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031801.mr
- first release of Kloxo-MR
