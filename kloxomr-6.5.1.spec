%define kloxo /usr/local/lxlabs/kloxo
%define productname kloxomr
%define timestamp 2013093003

Name: %{productname}
Summary: Kloxo-MR web panel
Version: 6.5.1.a
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
## disable because move to pscript
#%{__cp} -rp $RPM_BUILD_ROOT%{kloxo}/httpdocs/htmllib/script/* $RPM_BUILD_ROOT/script/

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
		echo " _/  Run 'sh /script/upcp' to install completely                             _/"
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
* Mon Sep 30 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013093003.mr
- fix varnish init and copy config
- mod mysql-convert.php 

* Mon Sep 30 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013093001.mr
- ready for testing varnish cache server
- add new 'class' as 'webcache'
- make simple 'removeOtherDrivers' function
- delete old config when switch web/dns to
- remove unused files
- restart qmail using 'restart' instead 'stop' and 'start'

* Sat Sep 28 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013092802.mr
- hiawatha already work for redirect 
- set enable gzip and fix urltoolkit setting for hiawatha
- using 'qmailcrl restart' instead 'qmailctl stop qmailctl start'
- make simple logic for webmail in web config
- fix webmail config (thanks for hiawatha with their strict path)
- change 'insert into' to 'insert ignore into' for sql to guarantee latest data 
- remove 'old style' sql data and function 

* Thu Sep 26 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013092606.mr
- change 'please contact'
- mod to web config only need init.conf (ssl, default and cp) and each domain config
- fix 'text record' for pdns (thanks SpaceDust)
- change apache ip to 127.0.0.1 in proxy 'mode'
- cleanup also remove /home/<webdrive>/conf/webmails
- fix dns uninstall
- use qmailctl instead service for stop/start qmail
- fix 'defaults' dir content remove
- remove unused function in web__lib.php and fix related to it
- fix lighttpd for running with 'new' config model

* Tue Sep 24 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013092403.mr
- better changedriver message
- disable qmail restart inside tmpupdatecleanup.php
- disable robots to cp, disable, default and webmail dirs
- ready testing for hiawatha and hiawatha-proxy (still unfinish work)
- reformat dns config tpl
- fix webmail and cp for hiawatha (move from 'generic' to each 'domain'config)
- emulate index files and permalink in urltoolkit for hiawatha

* Mon Sep 23 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013092302.mr
- add for 'lost' replace_between function
- change to better dnsnotify.pl and mod dnsnotify
- mod dnsnotify.pl for detail info
- add replace for maradns; add backend-bind for pdns
- add error log for php.ini.tpl
- use faatcgi+php-fpm instead ruid2 as default httpd in install process

* Sun Sep 22 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013092202.mr
- optimize config and process ('reload/restart' process) for dns
- fix restart-all (have a problem when php-fpm restart before web server restart)
- mod pdns.sql
- fix wrong djbdns tpl
- fix maradns tpl (but change to ip4_bind_address script still not ready)
- maradns.init include change default 'ip4_bind_address' to hostname ip
- add 'notify=yes' in bind
- mod to small dns config because using 'origin' based
- fix action login in update dns config process
- remove 'srv record' in djbdns; mod mararc for accept modified for xfr and zone list
- fix issue in dns switch (need stop server before unistall; found issue in maradns)
- back to use read db instead call var for__var_mmaillist in web__lib.php
- fix missing parameter in createListNlist
- add list.transfered.conf.tpl for maradns
- fix list.master.conf.tpl in maradns
- fix uninstall dns (wrong var)
- add 'dnsnotify' in maradns and djbdns with external script
- add supermasters process in pdns
- mod README.md

* Thu Sep 19 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013091903.mr
- fix nsd (add dns_nsdlib.php and disable include for slave conf)

* Thu Sep 19 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013091902.mr
- add double quote for 'txt record' of pdns
- fix issue fail install pdns-backend-mysql after install pdns
- mod pdns.sql for optimize to innodb
- maradns ready
- add and use setRpmRemovedViaYum for dns drivers
- disable process xfr on maradns
- fix maradns domain config
- try to use '0.0.0.0' for maradns ip bind
- prepare for NSD dns server
- convert all 'cname record' to 'a record' in dns server config
- mod watchdog list
- add 'nsd' in 'reserved', 'dns' and 'driver' list;
- set for 'nsd' dns server
- fix latest nginx (cache dir)
- still using '0.0.0.0' for 'nsd' notify/provide-xfr 

* Tue Sep 17 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013091704.mr
- add convert to utf8 charset for mysql-convert
- automatically add 'SPF record' beside 'A record' for 'SPF'
- fix pdns for addon-domain
- fix warning when spam switch

* Tue Sep 17 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013091702.mr
- fix detect primary ip for hostname
- disable dnssec for powerdns because still not work; add 'create database' in pdns.sql
- install pdns also install pdns-backend-mysql
- fix calling from powerdns to pdns

* Mon Sep 16 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013091603.mr
- move fix/mod '/etc/hosts' from setup.ah/installer.sh to lib.php
- remove fixmail-all in tmpupdatecleanup.php (because duplicate)
- create powerdns database ready if switch to powerdns or running cleanup
- fix hiawatha process in cleanup
- change name driver from 'powerdns' to 'pdns'
- fix ugly button and other not 'standard' html tag in 'default' theme
- fix isPhpModuleInstalled() var
- include new features (no exists in 6.5.0)

* Thu Sep 12 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013091202.mr
- add option server/client/domain in fixdomainkey
- fix installer process (conflict between mysql from centalt and ius)
- fix php-fpm tpl for deprecated commenting
- fix html code for display/theme

* Wed Sep 11 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013091101.mr
- change procedural to object style of MySQLi API
- fix link in langfunctionlib.php

* Mon Sep 9 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013090904.mr
- fix some display/theme; add testing for reset-mysql-root-password
- fix insert 'universal' hostname
- install mariadb if exist instead mysql55
- fix installer (because php52s must install after mysql55 and php53u)
- fix getRpmVersion()

* Mon Sep 9 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013090903.mr
- fix some bug on installer.php
- change install mysql55 instead mysql (from centos) because have trouble with MySQLi API in 5.0.x
- fix for php52s (add install net-snmp)
- adjutment installer.sh to match with setup.sh

* Mon Sep 9 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013090901.mr
- change 'Kloxo' title to 'Kloxo-MR'
- beside 'fs.file-max' also add others (like 'vm.swappiness') to optimize
- instead warning for 'hostname', add 'universal' hostname to '/etc/hosts' in install process

* Sun Sep 8 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013090801.mr
- mod service list
- mod reset-mysql-root-password
- remove 'javascript:' except for 'href'
- fix select all for client list
- add another var to sysctl.conf (for minimize buffers and cached memory)

* Sat Sep 7 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013090704.mr
- fix install process (especially in centos 5); fix qmail-toaster initial
- fix/better update process
- chkconfig off for php-fpm when install (because using ruid2 as 'default' php-type)

* Sat Sep 7 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013090702.mr
- fix identify hostname (use 'hostname' instead 'hostname -f')
- remove unused code
- fix updatelib.php for install process
- fix for ruid2 (need php.conf) for 'default' php-type

* Sat Sep 7 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013090701.mr
- move hostname checking from installer.php to setup.sh/installer.sh

* Fri Sep 6 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013090607.mr
- add function for checking hostname and stop install process if not qualified
- remove libmhash to checking
- no need check old.program.pem
- fix/better lxphp.exe checking when running upcp
- add '-y' to force to 'reinstall'; fix setup.sh/installer.sh/upcp script for install process

* Fri Sep 6 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013090603.mr
- add parse_ini.inc (prepare for kloxo config in ini format)
- fix 'default' default.conf
- mod fixdomainkey execute dns subaction for domain instead full_update
- change listen ip-port to socket in php-fpm.conf (for php 5.2)
- fix upcp script for fresh install 
- fix installer.php for 'default' web using ruid2 (need enable php.conf) 

* Tue Sep 2 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013090302.mr
- make install setup (run 'sh /script/upcp' instead '/usr/local/lxlabs/kloxo/install'
- fix mysqli_query for webmail database
- better reset-mysql-root password and mysql-convert code

* Mon Sep 2 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013090302.mr
- testing for 6.5.1.a
- convert mysql to mysqli API in Kloxo-MR code
- fix display/theme
- add/mod hash/bucket because nginx not started in certain conditions
- change lxphp to php52s in desclib.php

* Mon Sep 2 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013090201.mr
- fix display/theme (restore no domain list; wrong button title)
- add/mod hash/bucket for nginx.conf (nginx not start in certain conditions)
- add changelog content of first release 6.5.0.f

* Tue Aug 27 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013082704.mr
- taken code from 6.5.1.a (but maradns and hiawatha still disable)
- convert cname to a record for djbdns (because cname work work)
- fix error/warning for debug panel
- fix htmllib
- fix hiawatha service not execute after cleanup; fix old link to /script
- fix web drivers list
- add hiawatha, maradns and powerdns in update services in cleanup

* Mon Aug 26 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013082602.mr
- fix html tags especially for deprecated tag like <font>

* Mon Aug 26 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013082601.mr
- make fixdns faster (synchronize and allowed_transfer change to per-client)
- add 'accept-charset="utf-8"' for <form>

* Sat Aug 24 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013082401.mr
- fix panel port (back to 7778/7777 from 37778/37777)

* Fri Aug 23 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013082302.mr
- fix clientmail.php (missing ';')

* Thu Aug 22 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013082301.mr
- set root:root to installatron symlink
- add graph for load average
- move files inside script to pscript
- fix readsmtpLog for read smtp.log to maillog
- fix mail forward with disable detect mail account
- get client list from db directly instead from client object

* Thu Aug 22 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013082201.mr
- fix dns config issue (update config not work)
- mod/change fix-all (include fixftpuser instead fixftp)
- add process for delete /etc/pure-ftpd/pureftpd.passwd.tmp (unfinish loop for cleanup)

* Wed Aug 21 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013082102.mr
- fix dns config (make faster and no memory leak if running fixdns/cleanup)
- fix installatron-install script

* Tue Aug 20 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013082002.mr
- fix mysql-to-mariadb bug
- better getRpmVersion
- use lib.php from dev but disable mariadb/powerdns/hiawatha initial
- mod suphp configs
- better apache tpl
- better getRpmVersionViaYum function

* Sun Aug 18 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013081801.mr
- php*-gd, -bcmath and -pgsql also detect when running cleanup
- all languages including in core (still compile separately)

* Sat Aug 17 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013081701.mr
- fix/add packages listing on 'services' and 'component list'
- make cp address as additional panel

* Fri Aug 16 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013081601.mr
- fix detect ftp for lxguard (because think as using syslog but possible using rsyslog)
- fix restart scripts (because old script not work for other then english
- add php*-gd and php*-pdo (because repo not make as 'default') as default ext
- add config for microcache for nginx

* Wed Aug 14 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013081402.mr
- update customize fastcgi_param for ngix
- add init file checking for dns initial
- no convert cname to a record for local domain
- fix remove lxphp.exe for lxphp (because change to php52s)

* Tue Aug 13 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013081304.mr
- fix error 500 on kloxo-hiawatha (back to use TimeForCGI)

* Tue Aug 13 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013081303.mr
- fix upload issue (increasing MaxRequestSize TimeForRequest and MaxKeepAlive)
- fix/mod restart scripts

* Mon Aug 12 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013081208.mr
- add allowed-transfer script for dns server (make possible dns server as 'master')
- fix some minor bugs for dns template
- fix some minor bugs for install process
- mod/add restart/clearcache script

* Tue Aug 7 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013080701.mr
- fix bind dns config (bind work now like djbsns)

* Tue Aug 6 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013080605.mr
- simple execute for djbdns list.master.conf.tpl
- fix 'make' execute for axfrdns of djbdns
- fix no conf directory issues when using djbdns (cleanup will be create this dirs)
- fix bind domains.conf.tpl (problem with ns declare)
- add 'make' install when install kloxo (djbdns need it)
- add 'sock' dir for php-fpm socket when running cleanup

* Tue Aug 6 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013080602.mr
- fix dns config especially 'server alias' issue
- switch to djbns also execute djbdns 'setup'

* Tue Aug 6 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013080601.mr
- bugfix for dns config (wrong ns and cname)
- bugfix for access panel via https/7777
- mod sysctl.conf when running cleanup

* Mon Aug 5 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013080502.mr
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
- FIX - Security bug (possible sql-injection on login and switch 'safe' and 'unsafe' mode)
- FIX - Backup and restore (no worry about 'could_not_zip' and 'could_not_unzip')
- FIX - No password prompt when install spamdyke
- FIX - Add missing fetchmail when install
- FEATURE - Add Nginx, Nginx-proxy and Lighttpd-proxy
- FEATURE - Possible using different 'Php Branch' (for Php version 5.2, 5.3 and 5.4)
- FEATURE - Possible enable/disable 'Secondary Php' (using lxphp and suphp)
- FEATURE - More 'Php-type' (mod_php, suphp, fcgid and php-fpm) with different apache mpm
- FEATURE - Template-based web, php and php-fpm configs (use 'inline-php') and possible to customize
- FEATURE - Reverse DNS always appear
- FEATURE - Add select 'Ssl Key Bits' (2048, 1024 and 512) for 'Add Ssl Certificate'
- FEATURE - More logs on 'Log Manager'
- FEATURE - Enable logrotate
- FEATURE - Support for Centos 5 and 6 on 32bit or 64bit
- FEATURE - Possible install on Yum-based Linux OS (Fedora, ScientificLinux, CloudLinux and etc)
- FEATURE - Based-on multiple repo (Kloxo-MR owned, CentAlt, IUS, Epel and etc)
- FEATURE - Support different 'Mysql Branch' and MariaDB
- FEATURE - Add 'sysinfo' script to support purpose
- FEATURE - Add 'lxphp-module-install' script for installing module for lxphp
- FEATURE - Add and modified some scripts (convert-to-qmailtoaster, fix-qmail-assign, fixvpop and fixmail) for mail services
- FEATURE - Faster and better change mysql root password
- FEATURE - Add new webmail (afterlogic Webmail lite, T-Dah and Squirrelmail)
- FEATURE - Automatic add webmail when directory create inside /home/kloxo/httpd/webmail
- FEATURE - Change components to rpm format (addon, webmail, phpmyadmin and etc)
- FEATURE - Possible access FTP via ssl port
- FEATURE - Automatic install RKHunter and add log to 'Log Manager'
- CHANGE - Use qmail-toaster instead qmail-lxcenter (with script for convert)
- CHANGE - New interface for login and 'defaults' pages
- CHANGE - Use Kloxo-MR logo instead Kloxo logo
- CHANGE - Remove xcache, zend, ioncube and output compressed from 'Php Configs'
- CHANGE - Use php-fpm instead fastcgi or spawn-cgi for Lighttpd
- CHANGE - Use 'en-us' instead 'en' type for language
- CHANGE - Remove unwanted files and or code for windows os target
- CHANGE - Use '*' (wildcard) instead 'real' ip for web config and then no issue related to 'ip not found'
- CHANGE - Use 'apache:apache' instead 'lxlabs:lxlabs' ownership for '/home/kloxo/httpd' ('defaults' page')
- CHANGE - Use local data for 'Release Note' instead download
- CHANGE - Use tar.gz instead zip for compressing Kloxo-MR
- PATCH - bug fix for installer.sh (installer.sh for 'dev' step and yum install/update + setup.sh for final step)
- PATCH - remove php modules (except php-pear) because conflict between centos with other repos
