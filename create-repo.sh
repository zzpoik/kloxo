#!/bin/sh

# release on Kloxo 6.2.0
# by mustafa.ramadhan@lxcenter.org

if [ "$1" == "--help" ] ; then
	echo
	echo " ---------------------------------------------------------------------------"
	echo "  format: sh $0 --with-repofile"
	echo " ---------------------------------------------------------------------------"
	echo "   --createrepo - also creating '/etc/yum.repos.d/kloxo-mr-local.repo' file"
	echo
	echo " * Local repo inside /home/rpms and running this script will be"
	echo "      setup repodata inside /home/rpms"
	exit;
fi

echo
echo "- For help, type '$0 --help'"

if [ "$#" == 0 ] ; then
	echo
	echo "- No argument supplied. Defaulting to creating local-repo without .repo file"
	echo
fi

rpm --quiet -q createrepo -q

if [ $? != 0 ] ; then
	yum install createrepo -q -y
fi

mkdir -p ./release/centos5/{i386,x86_64,noarch}
mkdir -p ./release/centos6/{i386,x86_64,noarch}
mkdir -p ./release/neutral/{i386,x86_64,noarch}

mkdir -p ./testing/centos5/{i386,x86_64,noarch}
mkdir -p ./testing/centos6/{i386,x86_64,noarch}
mkdir -p ./testing/neutral/{i386,x86_64,noarch}

mkdir -p ./SRPMS

chmod -R o-w+r ../../

createrepo -d ./SRPMS

list=(i386 x86_64 noarch)

for item in ${list[*]}
do
	createrepo -d ./release/centos5/$item
	createrepo -d ./release/centos6/$item
	createrepo -d ./release/neutral/$item

	createrepo -d ./testing/centos5/$item
	createrepo -d ./testing/centos6/$item
	createrepo -d ./testing/neutral/$item
done

if [ "$1" == "--with-repofile" ] ; then

# RELEASEVER=$(rpm -q --qf "%{VERSION}" $(rpm -q --whatprovides redhat-release))

echo "- Creating local-repo inside '/home/rpms' "
echo "     with kloxo-local.repo inside '/etc/yum.repos.d'"

echo "[kloxo-mr-release-neutral-noarch-local]
name=Kloxo-MR - release-neutral-noarch
baseurl=file://home/repos/rpms.mtatwork.com/repo/release/neutral/noarch/
enabled=1
gpgcheck=0

[kloxo-mr-release-neutral-arch-local]
name=Kloxo-MR - release-neutral-\$basearch
baseurl=file://home/repos/rpms.mtatwork.com/repo/release/neutral/\$basearch/
enabled=1
gpgcheck=0

[kloxo-mr-release-version-noarch-local]
name=Kloxo-MR - release-version-noarch
baseurl=file://home/repos/rpms.mtatwork.com/repo/release/centos\$releasever/noarch/
enabled=1
gpgcheck=0

[kloxo-mr-release-arch-local]
name=Kloxo-MR - release-version-\$basearch
baseurl=file://home/repos/rpms.mtatwork.com/repo/release/centos\$releasever/\$basearch/
enabled=1
gpgcheck=0

[kloxo-mr-testing-neutral-noarch-local]
name=Kloxo-MR - testing-neutral-noarch
baseurl=file://home/repos/rpms.mtatwork.com/repo/testing/neutral/noarch/
enabled=0
gpgcheck=0

[kloxo-mr-testing-neutral-arch-local]
name=Kloxo-MR - testing-neutral-\$basearch
baseurl=file://home/repos/rpms.mtatwork.com/repo/testing/neutral/\$basearch/
enabled=0
gpgcheck=0

[kloxo-mr-testing-version-noarch-local]
name=Kloxo-MR - testing-version-noarch
baseurl=file://home/repos/rpms.mtatwork.com/repo/testing/centos\$releasever/noarch/
enabled=0
gpgcheck=0

[kloxo-mr-testing-version-arch-local]
name=Kloxo-MR - testing-version-\$basearch
baseurl=file://home/repos/rpms.mtatwork.com/repo/testing/centos\$releasever/\$basearch/
enabled=0
gpgcheck=0

[kloxo-mr-srpms-local]
name=Kloxo-MR - srpms
baseurl=file://home/repos/rpms.mtatwork.com/repo/SRPMS/
enabled=0
gpgcheck=0" > /etc/yum.repos.d/kloxo-mr-local.repo


fi

echo
