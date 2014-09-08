%define debug_package %{nil}
%define kloxo /usr/local/lxlabs/kloxo
%define productname kloxomr
%define timestamp 2014072901
Name: %{productname}
Summary: Kloxo-MR web panel
Version: 6.5.1.b
Release: %{timestamp}%{?dist}
License: GPL
Group: Applications/Internet

Source0: %{name}-%{version}-%{timestamp}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

Obsoletes: kloxomr-addon-extjs, kloxomr-addon-yui-dragdrop
#Provides: kloxomr-editor-fckeditor, kloxomr-editor-ckeditor

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
# disable because move to pscript
#%{__cp} -rp $RPM_BUILD_ROOT%{kloxo}/httpdocs/htmllib/script/* $RPM_BUILD_ROOT/script/

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/useradd -s /sbin/nologin -M -r -d /home/lxlabs/ \
    -c "Kloxo-MR Website Control Panel" lxlabs &>/dev/null || :

%files
%defattr(644,lxlabs,lxlabs,755)
%{kloxo}
%defattr(644,root,root,755)
/script
%defattr(755,root,root,755)
%{kloxo}/init/php*/*.sh

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
		echo " _/  - Run 'sh /script/upcp' to install completely                           _/"
		echo " _/                                                                          _/"
		echo " _/  - Some file downloads may not show a progress bar so please,            _/"
		echo " _/    do not interrupt the process.                                         _/"
		echo " _/                                                                          _/"
		echo " _/  - Then, go to 'Switch Program' to enable web and other programs         _/"
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
	echo " _/  Run 'sh /script/upcp' if update from Kloxo-MR 6.5.0                     _/"
	echo " _/                                                                          _/"
	echo " _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/"
	echo
fi

%changelog
* Tue Jul 29 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014072901.mr
- fix installing process related to phpm-installer

* Mon Jul 28 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014072801.mr
- change system() to exec() in fixvpop.php
- fix hiawatha service when running cleanup if hiawatha as active webserver

* Sun Jul 27 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014072701.mr
- just using phpm-installer for install all phpXYm/s
- mod/fix all php bin for general path
- change session path based on user
- validate username and password for add ftp user

* Wed Jul 09 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014070901.mr
- auto chown 755 for pl/cgi/py/rb if upload or fix-chownchmod 

* Tue Jul 08 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014070801.mr
- fix update ssh script
- disable .htaccess fix in fixweb 

* Mon Jul 07 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014070704.mr
- check mod_perl in cleanup process
- back to use previous reverseproxy for nginx and hiawatha
- add keep-alive and reduce timeout to 90 in hiawatha-proxy
- change reverseproxy passing from all to except pl/cgi/py/rb/shmtl (because handle by cgi-wrapper)
- reduce timeout value in nginx

* Sun Jul 06 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014070601.mr
- use hiawatha's cgi-wrapper instead apache's cgi in hiawatha-proxy
- mod/add index order (accept index.cgi also)
- using mod_perl instead mod_cgi for apache
- enable taint in perl for security reason

* Fri Jul 04 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014070402.mr
- fix enable-cgi (also warning 'not implementing yet' in nginx)

* Fri Jul 04 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014070401.mr
- fix/mod certain throw messages
- mod htmltextarea space
- enable/disable cgi for webserver
- use cgi-wrapper for hiawatha
- change openbasedir for 'apache' user
- use directly cgi-assign to perl instead perlsuexec for lighttpd
- fix lighttpd conf.tpl

* Mon Jun 30 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014063001.mr
- remove 'output_buffering = 4096' and stay with '= off' in php.ini 
- change throw value from array to string

* Fri Jun 27 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014062702.mr
- fix throw for mailing list
- convert to string if message as array (related to getThrow)
- mod certain throw messages

* Fri Jun 27 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014062701.mr
- use phpXYm for suphp in secondary php
- fix ssl reloop for nginx-proxy
- fix ckeditor for only save body content
- enable phar, intl, geoip, fileinfo and tidy module in php fix logrotate

* Tue Jun 24 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014062401.mr
- add getThrow() for translate throw message
- update all throw message with getThrow; fix logrotate config

* Sat Jun 21 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014062102.mr
- change addon-ckeditor/fckeditor to editor-ckeditor/fckeditor
- change addon-fckeditor to editor-*

* Sat Jun 21 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014062101.mr
- remove obsolete for fckeditor and ckeditor
- remove fckeditor/ckeditor from core code
- install ckeditor if not exists when running cleanup
- add provide for fckeditor and ckeditor

* Fri Jun 20 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014062001.mr
- add $this->write in postUpdate to make sure db write before next process
- prepare 'multiple php' (but still in progrss)

* Thu Jun 19 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014061903.mr
- add try-catch in default_index.php
- fix fixlxphpexe 
- also run rkhunter update in install process
- use ckeditor instead fckeditor if installed
- include ckeditor

* Tue Jun 17 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014061701.mr
- fix 'phptype_not_set' alert
- increasing connection in nginx and hiawatha until 10x (for high-traffic)
- use 'new' permalink for lighttpd
- prepare 'new' ip validate

* Sun Jun 15 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014061502.mr
- use callInBackground for lx_mail
- possible disable send notify for quota with flag
- add 'disable notify' for 'disable policy'
- add 'enable cron for all' in 'general settings'
- fix change 'webmail system default' (no need 2x click update again)
- increase types_hash_bucket_size in nginx for long domain name issue

* Sat Jun 14 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014061403.mr
- add default.conf for nginx for prevent when using webcache in front of nginx
- prevent delete main ftpuser
- fix 'server alias' for wildcard
- fix web_lib.php related to nginx

* Wed Jun 11 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014061101.mr
- mod scavenge send mail with Y/m/d format; mod djbdns tpl
- add some env to php53-fpm-pool.conf.tpl
- prepare phpm-fpm template
- mod kloxo.init to accept custom sh/conf/ini
- upload 'new' phpm-fpm template
- mod php-fpm-part.conf.tpl
- use symlink instead copy from pscript to /script
- mod php-fpm tpl to change php_value to php_flag for on/off
- change php_active to kloxo_php_active and adjustment for kloxo.init and fixlxphpexe

* Sun Jun 08 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014060802.mr
- add enable gzip in hiawatha
- change X-Forwarded-For in nginx
- mod php-fpm.conf.tpl (fpm for php52)
- enable send mail for scavenge
- fix loqout in feather skin
- add expire in hiawatha for panel
- add php-fpm conf/init/sh in php52m/php52s
- fix scavenge.php

* Wed Jun 04 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014060401.mr
- change CGIHandler from php to pl in hiawatha
- enable alias to cgi-bin in hiawatha; fix cron for client
- change root@ to admin@
- fix 'go' button in list
- set cursor to certain css tag
- mod htmllib related to cursor 
- change 'idle-timeout' for 'FastCGIExternalServer' of mod_fastcgi from 180 to 90

* Fri May 30 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014053003.mr
- fix header in lx_mail()
- mod to possible stmprelay/smarthost to outside smtp server
- mod to enable cron for users if exists '/usr/local/lxlabs/kloxo/etc/flag/enablecronforall.flg' file
- mod apache disable dirlist
- mod message for cron list
- fix nginx config (inactivate for 'disable_symlinks') because troube with static file path
- change sender from kloxo@ to root@

* Sat May 24 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014052401.mr
- mod/fix lx_mail() to accept utf8 and html and remove pre from message

* Mon May 21 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014052103.mr
- set /tmp dir as upload and save dir for phpmyadmin
- add 'max_input_vars' in php.ini and php-fpm config (set '3000' as default)
- add 'max input vars' in 'advanced php configure'
- send message as html and with utf8 charset

* Mon May 19 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014051901.mr
- add www.conf (blank) for php-fpm because latest php always create this file
- fix crf_token
- delete unused certain php files

* Tue May 13 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2014051301.mr
- add '-pass-header Authorization' in domains.conf.tpl of apache
- fix syncserver in web__lib.php
- prettier php code in certain files

* Mon May 12 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2014051201.mr
- separate warning for php.ini to client and pserver
- feather skin also appear background image (but still not use)
- no convert for '\n' to '<br />\n' (fix ticket list appear)

* Sat May 10 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2014051004.mr
- change listen.mode from 0660 to 0666 in php-fpm pool
- mod fixmail-all 

* Sat May 10 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014051002.mr
- mod/fix phpm-installer
- mod installatron-install
- fixmail-all also fix chown and chmod of /home/lxadmin/mail
- fixmail-all also checking postfix user and change to vpopmail if exists
- fix/mod installer related to postfix user
- fix php-fpm related to php53/php54 release -28 (add listen.owner, .group and .mode);
- fix/mod installer (related to fix process) and fix-all

* Mon May 5 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014050502.mr
- fix 'php used' in 'webserver configure' in master-slave environment

* Mon May 5 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014050501.mr
- fix default_index.php for using login page
- add syncserver for input array (importance for pdns in master-slave environment)
- fix dns class lib (add __construct like web class lib do)
- fix php.ini warning if not set (server and admin level)
- fix 'switch program' fpr master-slave environment
- fix 'webcache' input array in web lib
- fix click in php.ini warning
- change restart httpd in latest step in restart-all/restart-web

* Wed Apr 30 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014043002.mr
- set/enable phprc in php-cli (fix issue for missing .so in lxphp.exe)

* Wed Apr 30 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014043001.mr
- set mywebsql as 'sql manager' if exists in 'httpdocs/thirdparty'
- fix installatron-install if webmin exists
- fix php53m-extension-installer (also remove full path of extension)
- fix phpm-config-setup with remove full path of extension

* Tue Apr 29 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014042902.mr
- increasing MaxUploadSize to 2000 in hiawatha and MaxClients to 1000 in httpd
- fix custombutton not show icon in client
- make possible php54s beside php53s (resolve mariadb 10.0 issue; compile with mysqlnd for '--with-mysqli')

* Mon Apr 28 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014042803.mr
- overwrite /etc/php.ini in upcp (prevent missing .so in lxphp.exe)
- remove postfix user before re-/install qmail-toaster in upcp
- add install yum-plugin-replace in upcp
- mod phpm-config-setup
- fixmail-all also remove postfix user and install qmail-toaster if not exists
- move 'default' php.ini (because wrong place)

* Sun Apr 27 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014042702.mr
- move process update mratwork.repo to fixrepo and then execute in upcp (including change $releasever to OS version)

* Sun Apr 27 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014042701.mr
- fix web config template (forgot open bracket for .ca logic)
- fix upcp for 'mratwork-' execute

* Sat Apr 26 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014042601.mr
- still trouble with php for openssl (not perfect for SAN) and then mod to minimize problem
- little fix lighttpd config (still problem with ssl)

* Thu Apr 24 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014042401.mr
- external apps access via post (like phpmyadmin)
- fix to mariadb may not work if /var/lib/mysqltmp not exists
- implementing SAN for domain-based ssl cert
- cleanup will be copy openssl.cnf.tpl to /home/openssl
- fix button appear for client login

* Tue Apr 22 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014042202.mr
- fix reset-mysql-kloxo-password.php
- fix lighttpd conf.tpl related to .ca ssl
- change all lpform method to 'get'

* Mon Apr 21 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014042101.mr
- disable implementing update/add/delete in get for 'csrf token' because too much exception

* Sun Apr 20 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014042008.mr
- set 'cgi.rfc2616_headers = 0' in phpm series (because problem with mod_fastcgi)
- mod mysql-to-mariadb.php and mariadb-to-mysql.php
- change extension from mysql to mysqli in phpmyadmin_config.inc.php
- fix issue related to csrf for service action
- fix restore process for 'csrf token' (change 'get' to 'post')

* Sun Apr 20 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014042004.mr
- add/delete domain-based cert also fixweb and restart-web
- disable php module flag and update in phpinilib.php
- disable setInstallPhpFpm when switch web (aka install web driver) 

* Sun Apr 20 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014042001.mr
- add no permit for add/delete/update with get instead post 
- prepare domain-based ssl without assign to IP address
- fix delete in list related to 'csrf token'
- fix/change kloxo-php-fpm as root
- fix topbar_right (remove undefined param)
- fix certain form to post (related to 'csrf_token')
- implementing domain-based ssl certificate (delete still not remove files)
- mod web config related to domain-based ssl cert
- change using .crt to .pem in all web config
- fix delete cert also delete cert files
- change is__table to getClass (because the same purpose)
- fix sshconfig ini in show
- mod messagelib.php related to domain-based cert

* Fri Apr 18 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041802.mr
- set to make sure all add/delte/update in form must be under post and add csrf_token

* Fri Apr 18 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041801.mr
- mod property for 'limit' and 'custombutton'
- fix phpm-config-setup (related to php55m for symlink)

* Thu Apr 17 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041704.mr
- disable fix_self_ssl in update process
- enable for disable_functions in phpXYm php.ini
- add mysql56u in set.mysql.lst
- fix ftpuser if docroot not exists
- add/mod message in messagelib
- mod/fix phpini initialValue
- fix frame_left for client level (disable quickaction logic)
- mod/fix for handle update situation for mysql and php53s
- 'yum remove' for php53s also 'rpm -e --noscripts' for php53s-fpm

* Wed Apr 16 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041602.mr
- separate delete warning for customer and admin/reseller
- fix/mod for detect use yum and rpm in sh script

* Wed Apr 16 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041601.mr
- fix/mod 'nice' params
- mod csrf_token logic
- update and phpm install not work in panel (found yum problem in centos 6 64bit)

* Tue Apr 15 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041504.mr
- fix display issue related to token validate where only add/update/delete with 'post' method
- fix phpini because getlist for pserver only work under admin and then change to parent
- add warning in deletion list
- move deletion warning to top because possible not appear in long list

* Tue Apr 15 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041501.mr
- validate token able to disable
- fix add cron job (update still not work) 

* Mon Apr 14 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041402.mr
- recompile with fix wrong domainlib.php file

* Mon Apr 14 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041401.mr
- remove mysql from mysql.lst and for only mysql55 beside mariadb
- mariadb-to-mysql will be convert to mysql55
- disable installapp reference in ddatabaselib
- set initPhpIni() only use values from setUpINitialValues()
- add missing 'selected' keyword
- update 'limit' will be update will execute fixphp
- fix domainlib issue (isOn change to '=== 'on') in client domain
- to make sure quota value in 'float' format
- fix preAdd() with add params
- fix 'checked' in display

* Sun Apr 13 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041303.mr
- fix php53s.ini for using special setting for panel

* Sun Apr 13 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041301.mr
- add isTokenMatch() for 'csrf token'
- change protect from 'remote post' to 'csrf token'
- fix htaccess.tpl and php.ini.tpl (add 'default value')
- fix issue if select 'multiple php' and user click 'php configure' in domain
- mod phpm-instaler/-config-setup
- to make sure '/tmp/multiple_php_install.tmp' owned by root 

* Sat Apr 12 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041203.mr
- mod/fix langkeyword/message data
- mod multiselect list able to use keyword for title
- change redirect for 'change owner' from 'a=resource' to 'new client'

* Sat Apr 12 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041201.mr
- add ftpChangeOwner() because call by web__lib
- add db_set_value()
- fix do_remote_exec() with create remote object if not set (effect for 'change owner')
- fix ftpuser owner for 'change owner'

* Fri Apr 11 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041104.mr
- mod/update phpm-installer/-config-setup (all config parts move to -config-setup)
- mod 'searchall' button
- set 'php configure' not appear if not enable 'multiple php'
- fix preUpdate in objectactionlib.php
- add fix-yum-cache
- change from 300 to 30 for timeout in /etc/yum.conf

* Fri Apr 11 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041101.mr
- add more disable modules for phpm-installer (minimize trouble when using php52 as php-branch)

* Thu Apr 10 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041003.mr
- forgot submit mod lxclass.php (related to preAdd()/preUpdate())
- mod preUpdate in serverweblib.php (consistence with declare preUpdate in lxclass)

* Thu Apr 10 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014041001.mr
- add new preAdd()/preUpdate() function to process before add()/update()
- install 'multiple php' runnind well now from panel and in background process (need a trick)
- mod lxa.js related to multiselct

* Wed Apr 9 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014040901.mr
- move mratwork-* detect from cleanup to upcp

* Tue Apr 8 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014040801.mr
- fix directory protect for hiawatha (forgot add 'basic' in 'passwordfile' param)
- add log for phpm install process
- mod php5.fcgi 
- prepare install 'multiple php' via panel
- fix switch-php-fpm
- add option in 'webserver configure' for switch-php-fpm ('multiple php install' still not work)
- add 'Fix - PHP' in 'command center'
- change form color

* Sun Apr 6 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014040601.mr
- also disable magic_quotes, register_long_arraya and register_globalsin htaccess
- disable allow_call_time_pass_reference in php
- prepare add token in add/delete/update form
- add validate for 'server alias'
- better 'die' display
- mod xprint for display data of object, array or string
- implementing protect from 'remote post' instead using 'csrf token' (need more investigate)
- back to declare all php module in apache because selected module need fixweb every php-type changed
- fix mod_rewrite issue in apache
- fix chmod for php5.fcgi
- fix isRemotePost (change 'SERVER_NAME' to 'HTTP_HOST')
- fix directory declare in hiawatha related to directory protect
- fix phpm-installer (wrong declare for redis)

* Fri Apr 4 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014040405.mr
- fix php53s-installer

* Fri Apr 4 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014040404.mr
- enable unzip in docroot (no warning)
- back to set 'cgi.rfc2616_headers = 0' because trouble in wordpress in apache/-proxy
- back to not use ' -pass-header Authorization' in mod_fastcgi because must be 'cgi.rfc2616_headers = 0'

* Fri Apr 4 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014040403.mr
- now install with php53s by default

* Fri Apr 4 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014040402.mr
- remove pear channel update

* Fri Apr 4 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014040401.mr
- back to use 'cgi.fix_pathinfo = 1' because many apps not work if 0
- magic_quotes, register_globals and safe_mode always disable (make simple for multiple php)
- remove double post_max_size
- php*-enchant also not enable (bug issue)
- set no options for magic_quotes, register_globals and safe_mode in panel
- mod kloxo.init
- mod sh script for php
- php52s and php53s only for panel and use m version for general purpose (use switch-php-fpm)
- symlink /usr/lib64/php to /usr/lib/php (make simple for 64bit)
- mod fixlxphpexe, cleanup, cleanup-simple and cleanup-nokloxorestart
- mod packer.sh

* Wed Apr 2 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014040201.mr
- fix php.ini.tpl
- fixlxphpexe (better rm for symlink to make sure)
- when install in 64bit, phpm-installer only install 64bit dependencies

* Tue Apr 1 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014040109.mr
- fix php.ini.tpl
- php52s/php53s install using 'standard' php52/php53u

* Tue Apr 1 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014040108.mr
- fix run cleanup after update Kloxo-MR
- fix packer.sh

* Tue Apr 1 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014040106.mr
- running fixphp include fix extension_dir path (crucial for multiple php system)

* Tue Apr 1 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014040105.mr
- run fixlxphpexe include copy kloxo.init (guarantee always new)
- add missing kloxo-php-fpm.conf (special)

* Tue Apr 1 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014040104.mr
- fix typo in php53-fpm-pool.conf.tpl
- disable 'customemode' option in 'appearance'
- fix php.conf to inactive if switch to php-fpm in httpd
- disable 'export PHPRC=' in all php script (not needed)
- change php-error.log name depend on multiple php-type
- always use 'extension_dir' in all php.ini to mininize wrong php modules loaded
- add switch-php-fpm to make possible one of 'multiple php' for single purpose
- add reset-mysql-kloxo-password (alternative for fix-program-mysql)
- correct double param in php53-fpm-pool.conf.tpl
- correct/mod extension_dir in php.ini.tpl/php.ini.tpl
- fix php52s-installer
- also fix php-fpm-pool.conf.tpl in future phpcfg for typo and double param

* Sun Mar 30 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014033004.mr
- fix fix-qmail-assign
- running 'fix-qmail-assign' also create '.qmail-default' if not exists

* Sun Mar 30 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014033003.mr
- disable 'PATH_TRANSLATED' in nginx config because set 'cgi.fix_pathinfo = 0' in php.ini
- fix url for 'driver' list
- mod related to 'createListAddForm' and 'addListForm' function
- fix related to 'click here to add' in 'printListAddForm'
- change color for active tab and breadcumb
- fix/mod fix-qmail-assign to more info
- add 'help' in 'feather' (simple skin already exists)
- fix-chownchmod also fix mail dirs/files

* Sat Mar 29 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014032907.mr
- back to previous idea for phpXYm script
- fix extension_dir for phpXYm
- separated config-setup to file from phpm-installer
- add run phpm-config-setup to cleanup

* Sat Mar 29 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014032905.mr
- fix/mod sshauthorizedkey
- fix appear for 'selectshow'
- set to 'no disabled' for 'admin'
- mod/fix script for phpXYm and phpXYm
- already appear 'multiple php' options but unfinished yet
- fix/mod 'StW' type display (using textarea instead table)
- make simple sshauthorizedkey code
- change 'multiple php enable' to 'multiple php ready'
- prepare for 'multiple php' template script
- back to php.ini under web but only for 'php selected' and enable 'multiple php'
- add/change 'alert' if php.ini not set under 'pserver'

* Tue Mar 25 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014032502.mr
- fix detect php 5.4/5.5 which 'php -v' not work if using php 5.2/5.3 ini
- add 'try again' in 'alert' for fail to add domain
- remove 'disable installapp' in 'general'
- fix to setup roundcube 1.0.rc
- fix copy php-fpm.conf

* Tue Mar 25 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014032501.mr
- fix image/font appear depend on button type
- change to lxguardhit appear different column for fail and success
- fix permissions (from 0600 to 644) for user-logo
- fix version check
- fix restart if hiawatha status as not running
- gen-hashed.sh (for qmail user assign (based on 'real' bash)

* Sun Mar 23 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014032301.mr
- mod how-to-install.txt
- mod/change phpXY-installer
- create log file for escape segfault in install
- php.ini now based on user-level
- able setting php max children in resource plan
- mod fixweb/fixphp to adopt user-level php.ini
- install process with more info/message
- move php.ini/php5.fcgi from /home/httpd/<domain> to /home/kloxo/client/<client>
- fix fcgid to config adopt user-level php.ini
- max children appear 'unlimited' but intepret as '6'
- fix dns serial
- fix wrong text for load-wrapper calling
- php-fpm config include php configure from panel as 'php_admin_value'
- no admin/domain mode for admin (just appear admin mode)
- fix detect phpversion
- delete client also delete php-fpm config
- fix issue if dnssyncserver not array
- add is_cli() for debug purpose (different appear in cli and cgi mode)
- fix issue in sqlite.php if object not exist
- modified simplicity skin where breadcumb move from top to bottom of tab
- fix mailinglist where wrong url because as object
- fixweb and fixphp is separate process now
- fix fixlxphpexe script
- 2 type of multi-php (phpXYm and phpXYs)
- mod upcp and install scripts
- add options for install (-y/-force, --with-php53s/-53s and --remove-kloxo-database/-r)

* Mon Mar 17 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014031701.mr
- fix cleanup (no need restart phpXs)
- change to use php52 instead php53 for install step
- fix kloxo.inits
- fix phpXs-installer
- installer have options with '--force'/'-y', '--remove-kloxo-database' and '--use-php53s'
- delete disable-mysql-aio and add set-mysql-default (with more options)

* Sun Mar 16 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014031602.mr
- add missing default driver content
- phpXs-installer will be detect target php

* Sun Mar 16 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014031601.mr
- fix dependencies for phpXs-installer
- cleanup also convert special php53s to php53s based on php53u
- fix and also convert php52s in cleanup

* Sat Mar 15 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014031501.mr
- fix detect phpversion
- mod status appear in simplicity skin
- panel using php53u (via php53s-installer) instead special php53s
- add php*s-installer (prepare for multi-php)
- disable register_long_arrays in php 5.3+ (problem for 5.4+)
- possible execure php-cli with softlimit
- increase listen.backlog in nginx
- install able with '--force' and '--use-php52s' (default using php53s)

* Wed Mar 12 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014031203.mr
- rename softlimit to softlimit.sample because something wrong under centos 6 64bit (bug?)

* Wed Mar 12 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014031202.mr
- add 'proxy_set_header X-Forwarded-Protocol $scheme;' to nginx proxy.conf
- change menu file/dir for simplicity skin
- add soflimit in php*-cli.sh (automatically for lxphp.exe)
- change 'vm.vfs_cache_pressure' value 100 (tend to slow cached memory created)
- pending select php.ini from menu for client in simplicity skin 

* Mon Mar 10 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014031002.mr
- disable dtree for delete client
- fix for delete database username 

* Mon Mar 10 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014031001.mr
- make enable clientname as database username
- fix/mod image to font icon if select 'button_type' as font
- fix initial roundcube
- fix spamdyke config
- add -pass-header Authorization in mod_fastcgi of httpd
- fix for double userdir rule in nginx
- back to user 'default' restart for services
- delete domain also delete docroot if no other domain use the same docroot

* Sat Mar 1 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014030101.mr
- disable UserDirectory in hiawatha (to purpose userdir but not work)
- disable 'enable_php_fastcgi' in resourceplan
- move php logic for topbar to their php
- add 'wait' in 'status' top bar when click add/update

* Fri Feb 28 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014022801.mr
- fix tab bar for 'Client Processed Logs' page
- fix tab bar for 'lxguard' page
- fix font-icons in lxguard pages
- move left/right top bar of 'simplicity' to include_one with 'custom rule'
- fix icons in list if using 'image' as 'button type'

* Thu Feb 27 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014022701.mr
- mod packer.sh with also remove .pid files
- make already appear tab bar
- mod dprint/dprint_r with 'pre'
- add xprint (like dprint without debug mode)
- add database without prefix name and also database username for admin
- fix userdir in httpd with make declare userdir outside 'default' virtualhost

* Sun Feb 24 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014022404.mr
- add fixftp-all
- add 'standard command' like fixdns in 'command center'
- remove installapp
- fix quota/normal view with more detail
- add more detil in login history but bug still unreseolvced
- remove livesupport (unfinish work original Ligesh)
- fix list pagesize/pagenum
- use * instead *.lxlabs.com certificate
- upload new certificate

* Sat Feb 23 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014022305.mr
- fix userdir in httpd
- add fixftp-all
- add 'standard command' like fixdns in 'command center'

* Sat Feb 23 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014022303.mr
- resubmit certain restart scripts because wrong files 

* Sat Feb 23 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.b-2014022302.mr
- mod clock also hour with 2 digit format
- fix all restart and cleanup scripts
- move clock js code to clock.js file
- all include, js and css ready for 'custom rule'
- set Kloxo-MR 6.5.1 as b (beta)

* Sat Feb 22 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014022204.mr
- fix validate for new client
- set smaller menu, tab-bar and link-path in 'simplicity' skin
- more detail message and validate for add client and database 

* Sat Feb 22 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014022202.mr
- fix fix-userlogo (related to domainroot)
- fix all cleanups
- fix message and ticket (related to send mail) with add <pre>
- fix list if data is array (date in cron list still not fix)
- add clock in 'simplicity' top bar

* Fri Feb 21 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014022102.mr
- fix userlogo and default_index.php
- add left-side userlogo in panel
- add 'ticket' in 'simplicity' top bar
- fix non-admin send ticket
- reduce menu text width

* Fri Feb 21 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014022101.mr
- add alert when click status in 'simplicity' top bar
- change clientname length to 31 (according to centos and pure-ftpd)
- spawn-fcgi only auto-install under php52s in kloxo.init

* Thu Feb 20 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014022002.mr
- fix display_init
- better status title display in 'simplicity' skin
- restore css for default because wrong css

* Thu Feb 20 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014022002.mr
- remove double php53s-snmp in php53s-install
- add 'message' and 'status' in 'simplicity' top bar
- add db_get_count() in lib.php
- change "#" to "javascript://" for href in 'simplicity' index.php
- reduce menu container with (800 to 700px) to accept width 1024px display
- move 'status' bar from top-left to top-right

* Wed Feb 19 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014021901.mr
- fix sysinfo.php
- add squid in webcache list
- change client/database name to 64 chsrs and database username to 16 chars
- vslidate for client/database name and database username
- warning if 'switch program' and 'php-type' not set
- change default php-type to php-fpm_worker
- back to use default web, dns and spam server like 6.5.0 version
- mysql_conver also include change to utf-8 charset in panel (like in command-line)
- change '--- none ---' to '--- No Change ---'
- use db_get_value for php-type value
- fix issue if log not create
- fix getRpmBranchInstalled() if list file not exists
- mod randomString()
- add convert_message() fot handling like '[%_server_%]' and implementing also for error/alert message
- fix drop menu align in simplicity skin
- mod changeport.php for compatible with 6.5.0 and 6.5.1
- kloxo stop also checking php52s and php53s running or not
- installer still using php52s (because less memory usage)
- installer also php53s install and restart services before finish

* Sat Feb 15 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014021502.mr
- fix issue related to lxphp.exe
- fix restarts and kloxo.init
- set 755 for php*-cli.sh and php*-cgi.sh

* Sat Feb 15 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014021502.mr
- fix php53s-install (replace php53s to php53s-cli to escape conflict with regular php)
- prepare for random prefix for databasename

* Sat Feb 15 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014021501.mr
- fix nginx config related to disable_symlinks

* Fri Feb 14 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014021401.mr
- fix php53s-install and restart-all script

* Wed Feb 12 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014021201.mr
- add SymLinksIfOwnerMatch to apache config and equivalent param for other webservers
- change dynamic to ondemand for pm in php-fpm
- panel execute under php 5.2 or php 5.3 but install process still in php 5.2
- prepare jailed code (still disabled)
- run php53s-install if want running panel under php 5.3

* Mon Feb 3 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014020301.mr
- update cron_task (make client only able to list and delete their cron)

* Sun Feb 2 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014020201.mr
- fix install process (add looping to make sure kloxo database created)

* Fri Jan 31 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014013101.mr
- kloxo service using spawncgi (make kloxo-phpcgi under lxlabs user like kloxo-hiawatha)
- disable perl until fix hardlinks issue related to perl
- mod permissions update display

* Wed Jan 29 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014012902.mr
- fix some issues to make better update from Kloxo official 

* Wed Jan 29 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014012901.mr
- fix hiawatha config for dirprotect
- fix docroot where update not work 

* Tue Jan 28 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014012802.mr
- fix kloxo sql
- mod file list column 

* Tue Jan 28 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014012801.mr
- mod kloxo sql to using myisam as storage-engine
- fix ownership in filemanager

* Mon Jan 27 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014012702.mr
- back to use tcp/ip instead sock

* Mon Jan 27 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014012701.mr
- fix select-all in dns/mysql list
- fix docroot
- fix fastcgi (add ide-timeout)
- fix clearcache
- make update script as the same as cleanup
- fix nsd tpl
- use sock instead tcp/ip to access mysql in panel

* Fri Jan 10 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014011001.mr
- fix mysql-aio issue in openvz
- add disable-mysql-aio script
- mod how-to-install.txt for additional step when update from Kloxo 6.1.12
- no add certain param in sysctl.conf if openvz

* Tue Jan 07 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2014010701.mr
- fix install problem in openvz (wrong detect centos version)
- also remove exim in convert-to-qmailtoaster
- add try-catch in default_index.php

* Fri Jan 03 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014010301.mr
- mod again ionice (become not using '-n')
- fix hiawatha for proxy (404 and 504 error)

* Wed Jan 01 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2014010101.mr
- change ionice value
- detect hiawatha as web server when running restart-web/-all
- fix try-cache process in appear
- fix logic for nowrap in list table

* Thu Dec 26 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013122602.mr
- fix hiawatha service after hiawatha update

* Thu Dec 26 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013122601.mr
- fix mysql conflict because wrong detect centos 6
- fix web config for disable domain
- fix clearcache logic
- fix appear if restore from previous version

* Fri Dec 20 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013122002.mr
- fix wrong logic of lxphp detect

* Fri Dec 20 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013122001.mr
- add keyword text for updateall message and adjusment updateallWarningfunction js
- fix/mod certain infomsg
- change submit naming from frm_change to frm_button/frm_button_all and add frm_change hidden input
- add id for hidden input tags beside name
- fix all_client appear
- add warning to need add 'innodb_use_native_aio=0' in /etc/my.cnf to update to mysql to 5.5 if running cleanup
- cleanup process also fix if lxphp exist
- reupload abstract_012.jpg
- mod certain text in messagelib.php

* Tue Dec 17 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013121703.mr
- fix install and cleanup related to mratwork.repo

* Tue Dec 17 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013121702.mr
- fix logic for custom php-fpm in nginx 

* Tue Dec 16 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013121701.mr
- add/mod certain keyword/message
- fix 'webmail system default'
- mod message box (remove image)
- fix login page if 'session timeout' state

* Mon Dec 16 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013121603.mr
- fix security bug for php-fpm (add open_basedir)
- mod php-fpm open_basedir

* Mon Dec 16 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013121601.mr
- change kloxo-mr.repo to mratwork.repo via rpm and sdjustment in install and cleanup script
- change 'processed logs' to 'client processed logs' and 'stats configuration' to 'domain processed logs'
- fix error in debug file if 'property' not exist

* Sat Dec 14 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013121402.mr
- fix tree appear in feather skin 
- fix infomsg in 'Feather' skin
- fix certain infomsg
- remove useless code in display
- fix appear if no infomsg
- fix link in show
- split %client% to %client% and %loginas% in infomsg
- add certain infomsgs

* Wed Dec 11 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013121104.mr
- no permit if docroot with '..'
- change colors for version in login page
- beside when add domain, validate docroot also in 'docroot update' and 'redirect docroot'

* Wed Dec 11 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013121102.mr
- change to use jcterm instead sshterm-template for ssh access

* Mon Dec 9 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013120904.mr
- fix spamdyke disable/enable (need update qmail-toaster also)
- fix tls issue in smtp
- update panel port also create .ssl.port .nonssl.port files in /home/kloxo/httpd/cp
- port in cp also change if panel port change

* Mon Dec 9 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013120901.mr
- use 'post' instead 'get' if form have enctype
- change certain text (like 'show') to keywords
- fix htmledit appear and change height from 200 to 500
- switch to apache also install all necessary module (fix mod_fastcgi issue)
- prepare to change pure-ftp service from xinetd to init
- fix ie8 issue (possible)
- also change 'edit' beside 'html_edit' from 600 to 900px
- fix simplicity skin in IE8 
- mod/add certain infomsg
- prepare qmail stmp run (but still include in qmail rpm)
- fix pagenum/pagesize list

* Fri Dec 6 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013120601.mr
- update running cleanup-nokloxorestart instead cleanup
- add remark in messagelib.php for 'customize' var
- back to use action var instead get in form except for pagenum/pagesize in list

* Thu Dec 5 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013120503.mr
- change 'maxuploadsize' in kloxo-hiawatha from 100 to 2000 (MB)
- fix/mod 'simplicity' menu
- help/infomsg now able to use full html tags (like ul/ol/p)
- fix/mod space in certain list
- fix dbadmin and skeleton reference
- mod certain infomsg with rich html (unfinish jobs)
- mod width to wrap percentage (from 100 to 25)
- finishing reformat help messages (some messages still 'No information')
- fix messagelib.php
- combine add and list for ipaddress and adjustment menu

* Tue Dec 3 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013120301.mr
- note inside hiawatha.conf.base where able upload until 2GB if using hiawatha-9.3-2+

* Mon Dec 2 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013120201.mr
- move html.php from lib to theme
- add findindexfile in kloxo-hiawatha
- fix menu related to login-as-cancel
- fix sitepreview (also hn_urlrewrite) related to access php file directly
- fix hiawatha default.conf.tpl
- add getDescription function beside get getKeyword
- mod 'Comments' to without textarea
- combine resourplan 'information' and 'account on plan'
- fix/move infomsg for resourceplan
- add squid.conf (missing in previous)

* Fri Nov 29 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013112902.mr
- fix menu (wrong file 'version')

* Fri Nov 29 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013112901.mr
- fix hiawatha config if site access with '?s=a'
- translate certain text messages
- reversedns only able access by admin
- delete certain useless files
- fix/mod port checking
- disable licensecheck
- menu appear tree 'style' when admin/reseller access their customer

* Sat Nov 23 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013112305.mr
- fix update from panel (just enough running cleanup)
- mod 'ionice' from '-c3' (idle) to '-c2' (best-effort)

* Sat Nov 23 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013112304.mr
- mod hiawatha log format to extended (the same as apache log format)
- fix getContent in ffilelib.php
- better appear list in weblastvisit
- fix toggleVisibilityByClass in lxa.js
- fix branch list functions
- mod to not appear 'Consumed Login' when select 'Login As'
- fix/mod menu and buttons
- fix naming js function (to toggleVisibilityById)
- add 'click here' for 'help' and 'logout'
- add 'Login As (Cancel)' in menu
- remove 'Home' in 'Backup/Restore' and 'Update' title

* Fri Nov 22 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013112201.mr
- fix menu link in 'simplicity' skin (to using 'real link')
- fix ownwerahip in filemanager
- add php55u branch
- remove all '__m_message_pre' in add/update form and infomsg appear depend on variable in messagelib.php
- remove commonmessagelib.php because useless
- fix getRpmVersionViaYum
- mod toggleVisibility to make possible display all infomsg in 1 page

* Tue Nov 19 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013111901.mr
- fix related to forcedeletedserver
- run cleanup when click update (that mean update kloxomr)
- better info in 'update home' and fix installed/check-update rpm
- using text instead image for 'mail disk usage'
- add domain from commandline no need 'domain owned' approve

* Mon Nov 18 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013111801.mr
- fix too small font in certain pages
- make more space in drop menu
- set index.php in menu file only able access by display.php
- fix menu in 'simplicity' skin

* Sat Nov 16 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013111601.mr
- menu in 'simplicity' skin ready to multi-languages
- fix/mod many aspects related to better appearance

* Tue Nov 12 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013111202.mr
- set 'simplicity' tab slight bigger
- 'password' and 'server roles' tab always appear in 'server'
- change 'symbol' char to char number < 256 (make compatible for pc without unicode font)
- set 'block title' to centered (simple solution for weird certain pages like 'server roles' page)
- merge/reorganize buttons 'groups' (example: merge 'domain' and 'domain adm'/'administer' to 'domain')
- remove 'postmaster@...' from mailaccount in title because always postmaster from first domain
- change 'config' to 'configure' and 'config ...' to '... configure' in title

* Sun Nov 10 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013111002.mr
- fix appearance php warning
- set isDefaultSkin() to 'simplicity'
- fix 'select folder' in 'ftp user'
- fix 'custombutton'
- fix set_login_skin_to_feather()
- remove unwanted files
- after running upcp always restart-all
- fix/mod install process (no need 'yes' answer
- auto restart-all) 
- 

* Sat Nov 9 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013110902.mr
- add 'reverse-font' (metro-like) for 'button type' of 'appearence'
- fix apache issue when enable secondary php

* Fri Nov 8 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013110802.mr
- set 3 options for 'show directions'
- back to use addondomainlib.php (combine list + add parked + add redirect still not work)
- mod 'vertical 2' and set higher width and height for buttons show (need because set bigger font)
- install already set /tmp to permissions 1777
- also check already hosted when add domain
- fix/mod web server config (permalink)
- fix error 500 issue in apache (not able set 'cgi.rfc2616_headers = 1' in php.ini)
- fix/mod add domain (add 'domain owner' option)
- set to hidden of 'infomsg' in 'feather' skin (also appear if mouseover to 'help' button)
- add 'button type' in appearance (button using font or image)
- fix display where height problem in content when using div-div and change to div-table

* Tue Nov 5 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013110502.mr
- fix wrong style.css
- set font-size to bigger (9pt instead 8pt)
- change 'PHPMyAdmin' to 'SQL Manager' (prepare to using sqlite format for database)
- add dragdivscroll.js (horizontal mouse scrolling for buttons)
- remove graph column (trouble with bigger font; unnecessary)

* Mon Nov 4 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013110404.mr
- fix space between part of content
- forgot submit for 'show direction' 

* Mon Nov 4 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013110402.mr
- fix/mod display
- add 'show direction' for appear where skin able select for 'buttons' direction
 
* Sun Nov 3 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013110302.mr
- horizontal buttons flow instead vertical in 'simplicity' skin
- enable/disable compressing in php.ini
- to make sure, also install traceroute and util-linux (ionice)

* Sat Nov 2 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013110202.mr
- fix infomsg issue in 'webserver config'
- make more bigger font size 
- fix updateform in appearancelib.php
- add desc_addondomain_l declare (to prevent no object warning)
- fix many issue related to theme
- set drop menu to 'centered', fix width drop menu to 500px
- fix menu for resolution 1024
- add/mode background images
- fix background selected
- add brightness color function (use in the future)
- 'feather' skin still use icon images but 'simplicity' use symbol chars
- set smaller box in 'simplicity' skin
- embeded menu instead div caller
- delete gray version of background images
- no separate breadcomb with tab and content
- no need execute 'lxLoadBody()' js in 'simplicity' skin

* Wed Oct 30 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013103005.mr
- change path from $os.inc to rhel.inc
- fix path for webcache driver
- change 'Domain Adm' to 'Administer' text
- change certain image icon to char font
- fix resourceclass width table
- fix infomsg issue in 'webserver config'
- make more bigger font size

* Wed Oct 30 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013103003.mr
- remove 'add form' in each 'all' list
- fix background logic 
- better confirm page (with background color)

* Wed Oct 30 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013103001.mr
- fix path for drivers which move at previous
- res and naming adjustment for background

* Tue Oct 29 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013102903.mr
- disable installapp update in scavenge
- move files related to driver
- fix sitepreview

* Mon Oct 28 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013102802.mr
- fix dns config (wrong code submit)
- fix fixdns and fixweb 

* Mon Oct 28 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013102801.mr
- just fix html, css and js code for display
- add 'fs.aio-max-nr' and increase 'fs.file-max' value in install process
- make shadow effect for certain part

* Sat Oct 26 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013102601.mr
- try other dropdown menu (like it)
- remove unwanted files
- fix some 'bad' display

* Fri Oct 25 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013102502.mr
- move and rename header, bottom and lpanel.php to frame_ prefix and move to theme dir
- move functions related to lpanel from htmllib.php to frame_lpanel.php
- remove unwanted files/dirs
- add missing lst files
- fix packer process 

* Thu Oct 24 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013102402.mr
- restructure image/button/icon dirs
- remove unwanted files/functions
- fix nsd issue when select without domain exist
- mod os_create_default_slave_driver_db()
- fix mailaccount display
- remove content of login dir

* Tue Oct 22 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013102203.mr
- resubmit install script because wrong 'version'
- automatically change to 'simplicity' when still using 'default' skin
- 'simplicity' as default with background image
- fix password dialog for login with 'default' password (like 'admin')
- change (add/remove) background images

* Tue Oct 22 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013102201.mr
- remove 'default' skin but add color to feather
- move certain functions from lib.php to htmllib.php
- change default color from 'b1c0f0' to 'EFE8E0'
- restructure skin dirs
- reduce background image with to 1600 px

* Mon Oct 21 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013102103.mr
- disable web and dns installed by default
- mod setup.sh/installer.sh to handle 3x running installer.php when kloxo database fail to created

* Mon Oct 21 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013102102.mr
- fix skeleton.zip (previous with un-transparent logo)
- fix to make infomsg to center in feather/default skin
- move 'show/hide' button from tab to header
- fix js script for show/hide toggle

* Mon Oct 21 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013102101.mr
- 'simplicity' near final
- adjustment for 'default' and 'feather' skin
- convert some table-base to div-base html codes (not final work)
- add base extjs script (importance for frame-based skin)

* Sat Oct 19 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013101901.mr
- move all files in panel dir to theme dir amd adjustment link
- 'message inbox' as 'help' in simplicity psnel
- delete fckeditor _samples
- 'simplicity' skin able change background
- prepare for re-write display code

* Thu Oct 17 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013101703.mr
- fix for simplicity panel (no need frame and no thick/thin skin) 
- fix default slavedb driver

* Thu Oct 17 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013101701.mr
- restructure panel dirs
- introduce simplicity panel (based on thin feather but with css menu)
- remove unwanted files (related to panel display)
- use simplicity as 'default' panel

* Tue Oct 15 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013101501.mr
- select simple skin automatically redirect to display.php (no need frame-base again)
- fix issue in 'default' skin
- fix many bugs in interface

* Sat Oct 12 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013101203.mr
- rename all .phps to .php
- move htmllib to panel dir
- integrate extjs, yui-dropdown and fckeditor without source, example and docs files
- disable install kloxomr-addon 

* Sat Oct 12 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013101201.mr
- fix tmpfs detect logic
- fix program appear in 'switch programs'
- add cache grace in varnish
- mod comment in hiawatha config
- add squid driver
- add message for hiawatha microcache
- restructuring files for drivers and lib categories (prepare for easy add driver)
- most link in panel already 'right-click' to open (one step to new theme)
- remove unused files

* Tue Oct 8 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013100801.mr
- fix sysinfo to adopt hiawatha info
- fix hiawatha config for reverse-proxy
- disable 'microcache' in lighttpd because no different
- fix/optimize lighttpd.conf settting
- also enable 'microcache' nginx-proxy
- change remap.config setting for trafficserver
- set 'default value' for web/webcache/dns/spam driver because add 'none' driver
- fix web config for sure using 'php-fpm_event' as 'default' phptype
- warning in installer when '/tmp' set as 'tmpfs' (trouble with backup/restore)
- set max ip connection to 25 (like nginx config)
- use 'boosted' config for varnish
- prepare for squid web cache

* Fri Oct 4 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013100403.mr
- use trafficserver 4 config for version 3 and 4 because running well
- fix webmail logic
- introduce 'none' driver for web, dns and spam (as the same as webcache model)

* Thu Oct 2 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013100302.mr
- back to add .db_schema which importance for panel display
- all web server include 'generic' permalink
- change user as 'ats' instead 'root' for trafficserver
- enable 'debug' for trafficserver
- no include php imagick for install
- fix copy config for 'nsd' dns server
- restart qmail with 'stop
- sleep 2 start' instead 'restart'
- add missing file (db_schema)

* Wed Oct 2 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.1.a-2013100204.mr
- fix httpd template if web cache enable
- fix web cache for 'none'
- fix 'userdir' logic in template of httpd 
- fix dns and weh config
- change ats to root for minimize permissions issue for trafficserver
- remove 'debug' file
- fix 'default' web server in installing process
- fix 'default' configs copy for webcache server

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
- add replace for maradns
- add backend-bind for pdns
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
- remove 'srv record' in djbdns
- mod mararc for accept modified for xfr and zone list
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
- add 'nsd' in 'reserved', 'dns' and 'driver' list
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
- disable dnssec for powerdns because still not work
- add 'create database' in pdns.sql
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
- fix some display/theme
- add testing for reset-mysql-root-password
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
- fix install process (especially in centos 5)
- fix qmail-toaster initial
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
- add '-y' to force to 'reinstall'
- fix setup.sh/installer.sh/upcp script for install process

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
- fix hiawatha service not execute after cleanup
- fix old link to /script
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
- move maillog from /var/log/kloxo to /var/log
- remove smtp.log and courier.log
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
- mod smtp-ssl_run for rblsmtpd/blacklist
- remove double process for softlimit change
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
- fix sh permission to 755
- fix www redirect
- make simple awstats link
- add mariadb in mysql branch
- disable mariadb from centalt repo (conflict when install)
- based on 6.5.1.a-2013050502 and 6.5.1.a-2013051601

* Sun May 5 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031812.mr
- update suphp config (fix for possible security issue) and remove delete spamassassin dirs
- based on 6.5.1.a-2013050501 and 6.5.1.a-2013050502

* Fri Apr 26 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031811.mr
- fix packer.sh (remove lang except en-us)
- use ionice for du
- based on 6.5.1.a-2013042601 and 6.5.1.a-2013042602

* Sun Apr 21 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031810.mr
- fix some script based-on 6.5.1.a-2013042001 and 6.5.1.a-2013042101

* Mon Apr 8 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031809.mr
- fix some script based-on 6.5.1.a-2013040801

* Sat Mar 30 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031808.mr
- fix install issue on openvz

* Wed Mar 27 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031807.mr
- fix traffic issue and installer.sh/installer.php
- add some scripts

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
