Summary: MRatwork release file and package configuration
Name: mratwork-release
Version: 0.0.1
Release: 1
License: AGPLV3
Group: System Environment/Base
URL: http://mratwork.com/

BuildArch: noarch
Packager: Mustafa Ramadhan <mustafa@bigraf.com>
Vendor: MRatWork Repository, http://rpms.mratwork.com/
#BuildRequires: redhat-rpm-config

%description
MRatwork rpm release. This package contains yum configuration for the MRatWork RPM Repository.

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/%{_sysconfdir}/yum.repos.d/

if $(yum list *yum*|grep @) ;  then
	releasever='6'
else
	releasever='5'
fi

if [ "$(uname -m)" == "x86_64" ] ;  then
	basearch='x86_64'
	basearchalt='amd64'
else
	basearch='i386'
	basearchalt='x86'
fi

cat > %{buildroot}/%{_sysconfdir}/yum.repos.d/mratwork.repo << _EOF_
[mratwork-release-neutral-noarch]
name=MRatWork - release-neutral-noarch
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/release/neutral/noarch/
mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-release-neutral-noarch-mirrors.txt
enabled=1
gpgcheck=0

[mratwork-release-neutral-arch]
name=MRatWork - release-neutral-$basearch
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/release/neutral/$basearch/
mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-release-neutral-$basearch-mirrors.txt
enabled=1
gpgcheck=0

[mratwork-release-version-noarch]
name=MRatWork - release-version-noarch
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/release/centos$releasever/noarch/
mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-release-centos$releasever-noarch-mirrors.txt
enabled=1
gpgcheck=0

[mratwork-release-version-arch]
name=MRatWork - release-version-$basearch
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/release/centos$releasever/$basearch/
mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-release-centos$releasever-$basearch-mirrors.txt
enabled=1
gpgcheck=0

[mratwork-testing-neutral-noarch]
name=MRatWork - testing-neutral-noarch
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/testing/neutral/noarch/
mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-testing-neutral-noarch-mirrors.txt
enabled=0
gpgcheck=0

[mratwork-testing-neutral-arch]
name=MRatWork - testing-neutral-$basearch
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/testing/neutral/$basearch/
mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-testing-neutral-$basearch-mirrors.txt
enabled=0
gpgcheck=0

[mratwork-testing-version-noarch]
name=MRatWork - testing-version-noarch
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/testing/centos$releasever/noarch/
mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-testing-centos$releasever-noarch-mirrors.txt
enabled=0
gpgcheck=0

[mratwork-testing-version-arch]
name=MRatWork - testing-version-$basearch
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/testing/centos$releasever/$basearch/
mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-testing-centos$releasever-$basearch-mirrors.txt
enabled=0
gpgcheck=0

[mratwork-srpms]
name=MRatWork - srpms
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/SRPMS/
mirrorlist=http://rpms.mratwork.com/repo/mirrors/mratwork-SRPMS-mirrors.txt
enabled=0
gpgcheck=0

# ==================================

[mratwork-centalt]
name=MRatWork - centalt - $basearch
baseurl=http://centos.alt.ru/repository/centos/$releasever/$basearch/
mirrorlist=http://rpms.mratwork.com/repo/mirrors/centalt-centos-$releasever-$basearch-mirrors.txt
enabled=1
gpgcheck=0
exclude=openssh* perl* mariadb*

# ==================================

[mratwork-ius]
name=MRatWork - IUS Community Packages for EL $releasever - $basearch
baseurl=http://dl.iuscommunity.org/pub/ius/stable/Redhat/$releasever/$basearch
mirrorlist=http://dmirr.iuscommunity.org/mirrorlist/?repo=ius-el$releasever&arch=$basearch
enabled=1
gpgcheck=0
exclude=php52* mysql51*

[mratwork-ius-c5]
name=MRatWork - IUS Community Packages for EL 5 (special) - $basearch
baseurl=http://dl.iuscommunity.org/pub/ius/archive/CentOS/5/$basearch
mirrorlist=http://rpms.mratwork.com/repo/mirrors/ius-centos-5-$basearch-mirrors.txt
enabled=1
gpgcheck=0
includepkgs=php52*

# ==================================

[mratwork-epel]
name=MRatWork - Extra Packages for EL $releasever - $basearch
baseurl=http://download.fedoraproject.org/pub/epel/$releasever/$basearch
mirrorlist=http://mirrors.fedoraproject.org/mirrorlist?repo=epel-$releasever&arch=$basearch
enabled=1
gpgcheck=0

# ==================================

# for varnish
[mratwork-varnish-3.0]
name=MRatWork - Varnish 3.0 for EL $releasever - $basearch
baseurl=http://repo.varnish-cache.org/redhat/varnish-3.0/el$releasever/$basearch
enabled=1
gpgcheck=0

# ==================================

# for hiawatha
[mratwork-centosec]
name=MRatWork - CentOS $releasever Packages from CentOS.EC
baseurl=http://centos$releasever.ecualinux.com/$basearch
enabled=0
gpgcheck=0
exclude=cairo*

# ==================================

# for nginx-stable
[mratwork-nginx]
name=Kloxo-MR - nginx repo
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=0
enabled=0

# ==================================

# for mariadb
[mratwork-mariadb]
name=Kloxo-MR - mariadb repo
baseurl=http://yum.mariadb.org/5.5/centos$releasever-$basearchalt
enabled=0
gpgcheck=0

# ==================================

# for atrpms
[mratwork-atrpms]
name=Kloxo-MR - Fedora Core $releasever - $basearch - ATrpms
baseurl=http://dl.atrpms.net/el$releasever-$basearch/atrpms/stable
gpgcheck=0
enabled=0

_EOF_

%{__rm} -rf %{_sysconfdir}/yum.repos.d/kloxo-mr.repo
%{__cp} -f %{buildroot}/%{_sysconfdir}/yum.repos.d/mratwork.repo %{_sysconfdir}/yum.repos.d/mratwork.repo

%clean

%post

%files
%defattr(-, root, root, 0755)
%dir %{_sysconfdir}/yum.repos.d/
%config %{_sysconfdir}/yum.repos.d/mratwork.repo

%changelog
* Mon Dec 06 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 0.0.1-1
- first release
