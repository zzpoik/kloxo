#!/bin/sh

# release on Kloxo 6.2.0
# by mustafa.ramadhan@lxcenter.org

# RELEASEVER=$(rpm -q --qf "%{VERSION}" $(rpm -q --whatprovides redhat-release))

echo "- Creating custom-repo inside '/home/rpms' "
echo "     with kloxo-custom.repo inside '/etc/yum.repos.d'"

echo "[kloxo-release-public-core]
name=kloxo-release-public-core
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/release/kloxo/noarch/
enabled=1
gpgcheck=0

[kloxo-release-public-noarch]
name=kloxo-release-public-noarch
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/release/centos\$releasever/noarch/
enabled=1
gpgcheck=0

[kloxo-release-public-arch]
name=kloxo-release-public-\$basearch
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/release/centos\$releasever/\$basearch/
enabled=1
gpgcheck=0

[kloxo-testing-public-core]
name=kloxo-testing-public-core
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/testing/kloxo/noarch/
enabled=0
gpgcheck=0

[kloxo-testing-public-noarch]
name=kloxo-testing-public-noarch
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/testing/centos\$releasever/noarch/
enabled=0
gpgcheck=0

[kloxo-testing-public-arch]
name=kloxo-testing-public-\$basearch
baseurl=https://github.com/mustafaramadhan/kloxo/raw/rpms/testing/centos\$releasever/\$basearch/
enabled=0
gpgcheck=0

# ==================================

[kloxo-centalt]
name=kloxo-centalt - \$basearch
baseurl=http://centos.alt.ru/repository/centos/\$releasever/\$basearch/
enabled=1
gpgcheck=0
exclude=openssh*

# ==================================

[kloxo-ius]
name=kloxo - IUS Community Packages for Enterprise Linux \$releasever - \$basearch
baseurl=http://dl.iuscommunity.org/pub/ius/stable/Redhat/\$releasever/\$basearch
mirrorlist=http://dmirr.iuscommunity.org/mirrorlist/?repo=ius-el\$releasever&arch=\$basearch
enabled=1
gpgcheck=0

# ==================================

[kloxo-epel]
name=kloxo - Extra Packages for Enterprise Linux \$releasever - \$basearch
baseurl=http://download.fedoraproject.org/pub/epel/\$releasever/\$basearch
mirrorlist=http://mirrors.fedoraproject.org/mirrorlist?repo=epel-\$releasever&arch=\$basearch
enabled=1
gpgcheck=0" > /etc/yum.repos.d/kloxo-mr.repo
