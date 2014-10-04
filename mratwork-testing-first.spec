Summary: MRatwork release file and package configuration
Name: mratwork-testing
Version: 0.0.1
Release: 1
License: AGPLV3
Group: System Environment/Base
URL: http://mratwork.com/

BuildArch: noarch
Packager: Mustafa Ramadhan <mustafa@bigraf.com>
Vendor: MRatWork Repository, http://rpms.mratwork.com/
#BuildRequires: redhat-rpm-config
#Obsoletes: mratwork-release
Conflicts: mratwork-release


%description
MRatwork rpm testing. This package contains yum configuration for the MRatWork RPM Repository.

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/%{_sysconfdir}/yum.repos.d/

cat > %{buildroot}/%{_sysconfdir}/yum.repos.d/mratwork.repo << _EOF_
[mratwork-release-neutral-noarch]
name=MRatWork - release-neutral-noarch
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/release/neutral/noarch/
#mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-release-neutral-noarch-mirrors.txt
enabled=1
gpgcheck=0

#[mratwork-release-neutral-arch]
#name=MRatWork - release-neutral-arch
#baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/release/neutral/\$basearch/
##mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-release-neutral-\$basearch-mirrors.txt
#enabled=0
#gpgcheck=0

#[mratwork-release-version-noarch]
#name=MRatWork - release-version-noarch
#baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/release/centos\$releasever/noarch/
##mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-release-centos\$releasever-noarch-mirrors.txt
#enabled=0
#gpgcheck=0

[mratwork-release-version-arch]
name=MRatWork - release-version-arch
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/release/centos\$releasever/\$basearch/
#mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-release-centos\$releasever-\$basearch-mirrors.txt
enabled=1
gpgcheck=0

[mratwork-testing-neutral-noarch]
name=MRatWork - testing-neutral-noarch
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/testing/neutral/noarch/
#mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-testing-neutral-noarch-mirrors.txt
enabled=1
gpgcheck=0

#[mratwork-testing-neutral-arch]
#name=MRatWork - testing-neutral-arch
#baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/testing/neutral/\$basearch/
##mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-testing-neutral-\$basearch-mirrors.txt
#enabled=0
#gpgcheck=0

#[mratwork-testing-version-noarch]
#name=MRatWork - testing-version-noarch
#baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/testing/centos\$releasever/noarch/
##mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-testing-centos\$releasever-noarch-mirrors.txt
#enabled=0
#gpgcheck=0

[mratwork-testing-version-arch]
name=MRatWork - testing-version-arch
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/testing/centos\$releasever/\$basearch/
#mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-testing-centos\$releasever-\$basearch-mirrors.txt
enabled=0
gpgcheck=0

[mratwork-srpms]
name=MRatWork - srpms
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/SRPMS/
#mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-SRPMS-mirrors.txt
enabled=0
gpgcheck=0

# ==================================

[mratwork-centalt]
name=MRatWork - centalt - arch
baseurl=http://centos.alt.ru/repository/centos/\$releasever/\$basearch/
#mirrorlist=http://rpms.mratwork.com/repo/mirrors/centalt-centos-\$releasever-\$basearch-mirrors.txt
enabled=0
gpgcheck=0
exclude=openssh* perl* mariadb* php* postfix* exim* ssmtp*

# ==================================

[mratwork-ius-stable]
name=MRatWork - IUS Community Packages for EL \$releasever (stable) - arch
baseurl=http://dl.iuscommunity.org/pub/ius/stable/Redhat/\$releasever/\$basearch
mirrorlist=http://dmirr.iuscommunity.org/mirrorlist/?repo=ius-el\$releasever&arch=\$basearch
enabled=1
gpgcheck=0
exclude=mysql51*

[mratwork-ius-archive]
name=MRatWork - IUS Community Packages for EL \$releasever (archive) - arch
baseurl=http://dl.iuscommunity.org/pub/ius/archive/Redhat/\$releasever/\$basearch
enabled=1
gpgcheck=0
exclude=mysql51*

# ==================================

[mratwork-remi]
name=MRatWork - Les RPM de remi pour Enterprise Linux \$releasever - arch
baseurl=http://rpms.famillecollet.com/enterprise/\$releasever/remi/\$basearch/
mirrorlist=http://rpms.famillecollet.com/enterprise/\$releasever/remi/mirror
enabled=0
gpgcheck=0

[mratwork-remi-php55]
name=MRatWork - Les RPM de remi de PHP 5.5 pour Enterprise Linux \$releasever - arch
baseurl=http://rpms.famillecollet.com/enterprise/\$releasever/php55/\$basearch/
mirrorlist=http://rpms.famillecollet.com/enterprise/\$releasever/php55/mirror
enabled=0
gpgcheck=0

[mratwork-remi-php56]
name=MRatWork - Les RPM de remi de PHP 5.6 pour Enterprise Linux 6 - arch
#baseurl=http://rpms.famillecollet.com/enterprise/\$releasever/php56/\$basearch/
mirrorlist=http://rpms.famillecollet.com/enterprise/\$releasever/php56/mirror
enabled=0
gpgcheck=0

# ==================================

[mratwork-epel]
name=MRatWork - Extra Packages for EL \$releasever - arch
baseurl=http://download.fedoraproject.org/pub/epel/\$releasever/\$basearch
mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-\$releasever&arch=\$basearch
enabled=1
gpgcheck=0
exclude=postfix* exim* ssmtp* pdns*


# ==================================

# for varnish
[mratwork-varnish-3.0]
name=MRatWork - Varnish 3.0 for EL \$releasever - arch
baseurl=http://repo.varnish-cache.org/redhat/varnish-3.0/el\$releasever/\$basearch
enabled=1
gpgcheck=0

# ==================================

# for hiawatha
[mratwork-centosec]
name=MRatWork - CentOS \$releasever Packages from CentOS.EC
baseurl=http://centos\$releasever.ecualinux.com/\$basearch
enabled=0
gpgcheck=0
exclude=cairo*

# ==================================

# for nginx
[mratwork-nginx]
name=Kloxo-MR - nginx repo
baseurl=http://nginx.org/packages/mainline/centos/\$releasever/\$basearch/
enabled=1
gpgcheck=0

# for nginx-stable
[mratwork-nginx-stable]
name=Kloxo-MR - nginx-stable repo
baseurl=http://nginx.org/packages/centos/\$releasever/\$basearch/
enabled=1
gpgcheck=0

# ==================================

# for mariadb
[mratwork-mariadb-32]
name=Kloxo-MR - mariadb 32bit repo
baseurl=http://yum.mariadb.org/10.0/centos\$releasever-x86
enabled=0
gpgcheck=0

[mratwork-mariadb-64]
name=Kloxo-MR - mariadb 64bit repo
baseurl=http://yum.mariadb.org/10.0/centos\$releasever-amd64
enabled=0
gpgcheck=0

# ==================================

# for atrpms
[mratwork-atrpms]
name=Kloxo-MR - Fedora Core \$releasever - $basearch - ATrpms
baseurl=http://dl.atrpms.net/el\$releasever-\$basearch/atrpms/stable
enabled=0
gpgcheck=0

# ==================================

# for litespeed
[mratwork-litespeed]
name=MRatWork - LiteSpeed Tech Repository for CentOS \$releasever - \$basearch
baseurl=http://rpms.litespeedtech.com/centos/\$releasever/\$basearch/
#failovermethod=priority
enabled=1
gpgcheck=0

[mratwork-litespeed-update]
name=MRatWork - LiteSpeed Tech Repository for CentOS \$releasever - \$basearch
baseurl=http://rpms.litespeedtech.com/centos/\$releasever/update/\$basearch/
#failovermethod=priority
enabled=1
gpgcheck=0

# ==================================

# for mod-pagespeed
[mratwork-google-mod-pagespeed]
name=MRatWork - google-mod-pagespeed
baseurl=http://dl.google.com/linux/mod-pagespeed/rpm/stable/\$basearch
enabled=1
gpgcheck=0

# ==================================

# for mod_mono
[mratwork-mod-mono]
name=MRatWork - mod_mono
baseurl=http://download.mono-project.com/repo/centos/
enabled=1
gpgcheck=0

# ==================================

# for CentOS kernel
[mratwork-centos-kernel]
name=MRatWork - CentOS kernel
baseurl=http://elrepo.org/linux/kernel/el\$releasever/\$basearch
enabled=0
gpgcheck=0

_EOF_

%{__rm} -rf %{_sysconfdir}/yum.repos.d/kloxo.repo
%{__rm} -rf %{_sysconfdir}/yum.repos.d/kloxo-mr.repo
%{__rm} -rf %{_sysconfdir}/yum.repos.d/kloxo-custom.repo
%{__rm} -rf %{_sysconfdir}/yum.repos.d/lxcenter.repo
%{__rm} -rf %{_sysconfdir}/yum.repos.d/lxlabs.repo
%{__cp} -f %{buildroot}/%{_sysconfdir}/yum.repos.d/mratwork.repo %{_sysconfdir}/yum.repos.d/mratwork.repo

%clean

%post

%files
%defattr(-, root, root, 0755)
%dir %{_sysconfdir}/yum.repos.d/
%config %{_sysconfdir}/yum.repos.d/mratwork.repo

%changelog
* Tue Apr 9 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 0.0.2-4
- Change 'Obsoletes' to 'Conflicts' for 'mratwork-testing' because trouble when install the other

* Tue Apr 8 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 0.0.2-3
- add 'Obsoletes' for 'mratwork-release'

* Fri Apr 4 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 0.0.2-2
- disable release-neutral-arch and release-version-noarch because trouble with centos 6 latest version

* Sun Mar 23 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 0.0.2-1
- remove php52 from ius (because only for centos 5 and 'archives' status)
- exclude postfix, ssmtp and exim from ius and centalt

* Tue Mar 4 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 0.0.1-9
- disable php5* from centalt because conflict with other php branches

* Sat Feb 22 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 0.0.1-8
- add google-mod-pagespeed repo

* Thu Jan 16 2014 Mustafa Ramadhan <mustafa@bigraf.com> - 0.0.1-6
- add litespeed repo

* Sat Dec 28 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 0.0.1-5
- back to disable mirror because mirror have a trouble if using centos 6

* Tue Dec 17 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 0.0.1-3
- fix version detect
- no change for basearch except basearchalt

* Mon Dec 16 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 0.0.1-2
- fix version detect

* Mon Dec 16 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 0.0.1-1
- first release
