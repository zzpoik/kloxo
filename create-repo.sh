#!/bin/sh

# release on Kloxo 6.2.0
# by mustafa.ramadhan@lxcenter.org

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

chmod -R o-w+r /home/admin/rpms.potissima.com

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

