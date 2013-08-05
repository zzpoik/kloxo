%define kloxo /usr/local/lxlabs/kloxo
%define productname kloxomr
%define timestamp 2013080502

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
		echo " _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/"
		echo " _/                                                                          _/"
		echo " _/  ..:: Kloxo-MR Web Panel ::..                                            _/"
		echo " _/                                                                          _/"
		echo " _/  Attention:                                                              _/"
		echo " _/                                                                          _/"
		echo " _/  Run 'sh /script/cleanup' for to make sure running well                  _/"
		echo " _/  or 'sh /script/cleanup-simple' (cleanup without fix services configs    _/"
		echo " _/                                                                          _/"
		echo " _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/"
		echo
	else
		# real fresh install
		echo
		echo " _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/"
		echo " _/                                                                          _/"
		echo " _/  ..:: Kloxo-MR Web Panel ::..                                            _/"
		echo " _/                                                                          _/"
		echo " _/  Attention:                                                              _/"
		echo " _/                                                                          _/"
		echo " _/  Run 'sh /usr/local/lxlabs/kloxo/install/setup.sh' completely install    _/"
		echo " _/                                                                          _/"
		echo " _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/"
		echo
	fi
elif [ "$1" = "2" ]; then
	# yum update
	echo
	echo " _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/"
	echo " _/                                                                          _/"
	echo " _/  ..:: Kloxo-MR Web Panel ::..                                            _/"
	echo " _/                                                                          _/"
	echo " _/  Attention:                                                              _/"
	echo " _/                                                                          _/"
	echo " _/  Run 'sh /script/cleanup' for to make sure running well                  _/"
	echo " _/  or 'sh /script/cleanup-simple' (cleanup without fix services configs)   _/"
	echo " _/                                                                          _/"
	echo " _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/"
	echo
fi

%changelog
* Thu Jul 11 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013080502.mr
- based on until 6.5.1.a-2013080502
- change timestamp from 20130318xx to real timestamp release
- change lxphp + lxlighttpd to php52s + hiawatha (the first cp using it!)
- template-based for dns server (bind and djbdns)
- bugfix for add ip
- remove unwanted files (related to os detect/specific)
- because using hiawatha, socket error already fixed (related to php-cli wrapper)
- using closeinput instead closeallinput (no different effect found)
- remove unwanted skin images
- change /restart or /backendrestart to /load-wrapper (related to socket error issue)
- change helpurl from forum.lxcenter.org to forum.mratwork.com
- exclude bind from centalt because something trouble when using it
- add error page for panel
- remove lxphp-module-install and change to php5Xs-extension-install
- add/change set-secondary-php script

* Thu Jul 11 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031828.mr
- based on until 6.5.1.a-2013071102
- disable mysql51 and mysql55 from ius (make conflict)
- improve mysql-convert and mysql-optimize
- modified kloxo-mr.repo
- make setup process until 3x if kloxo database not created (normally enough 1-2x)

* Wed Jul 10 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031827.mr
- based on until 6.5.1.a-2013071001
- disable mysql from ius repo (make conflict) when install process
- change kloxo-mr.repo related to disable mysql from ius
- mysql-convert script will convert all database for storage-engine target
- move certain parameter of nginx from 'location /' to 'server'
- disable 'php_admin_value[memory_limit]' on php-fpm template
- restart will be execute start if not running for qmail service
- rename custom qmail run/log run of qmail-toaster
- increase value of TopCountries and others for webalizer
- fix web config, expecially for add/delete domain.

* Thu Jun 27 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031826.mr
- based on until 6.5.1.a-2013062801
- fix install process (need running setup.sh 2x in certain condition)
- fix wrong message for afterlogic when running cleanup/fixwebmail/fixmail-all
- back to use 'wget' instead 'wget -r' in how-to-install
- disable mirror for repo and just using for emergency

* Thu Jun 27 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031825.mr
- based on until 6.5.1.a-2013062701
- remove double install process for mysql and httpd
- fix conflict of mysql install
- set php53u and mysql51/mysql55 as default install
- fix telaen config copy
- fix webmail detect

* Wed Jun 26 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031824.mr
- based on until 6.5.1.a-2013062602
- fix restore message
- prepare for qmail-toaster custom-based run/log run

* Thu Jun 20 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031823.mr
- based on until 6.5.1.a-2013062301
- restart kloxo if found 'server 7779' not connected
- move maillog from /var/log/kloxo to /var/log; remove smtp.log and courier.log
- dual log (multilog and splogger) for qmail-toaster
- remove unwanted files (espacially related to qmail-toaster)
- bug fix for reset-mysql-root-password script
- change to apache:apache for dirprotect dir
- fix segfault when install
- change kloxo sql without engine=myisam

* Sun Jun 16 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031822.mr
- fix clearcache script
- remove certain qmail config fix (becuase logic and code move to rpm)

* Sat Jun 15 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031821.mr
- based on until 6.5.1.a-2013061501
- back to disable mariadb from centalt (still have a problem install Kloxo-MR on centos 6 32bit)
- fix diprotect path for apache
- not need softlimit change (already set inside qmail-toaster)
- fix clearcache script for openvz host
- fix function.sh and lxphpcli.sh (add exec)
- back to use restart function instead stop and start for restart

* Tue Jun 11 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031820.mr
- based on until 6.5.1.a-2013061101
- install without asking 'master/slave' (always as 'master'; run make-slave for change to slave)
- more info backup/restore
- mod smtp-ssl_run for rblsmtpd/blacklist; remove double process for softlimit change
- fix issue when install on openvz host
- enable gateway when add ip
- modified nginx config for dualstack ip (ipv4+ipv6)

* Tue Jun 4 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031819.mr
- based on until 6.5.1.a-2013060402
- fix fixmail-all ('cp' weird behaviour for copy dir)
- add info in sysinfo

* Mon Jun 3 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031818.mr
- based on until 6.5.1.a-2013060301
- fix web config for www-redirect and wildcards
- create mail account automatically create subscribe folders
- fix smtp issue
- possible customize qmail run script

* Fri May 31 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031817.mr
- fix restart-services
- fix userlist with exist checking
- fix mail config (smtp and submission already work!)
- remove for exlude mariadb from centalt repo
- based on until 6.5.1.a-2013053102

* Sun May 26 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031816.mr
- fix qmail init
- based on until 6.5.1.a-2013052101

* Sun May 19 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031815.mr
- fix kloxo database path
- based on until 6.5.1.a-2013051901

* Sat May 18 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031814.mr
- fix install process and reset password from ssh
- fix wildcards for website
- based on until 6.5.1.a-2013051804

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
