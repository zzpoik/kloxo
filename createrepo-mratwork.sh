#!/bin/sh

rpm --quiet -q createrepo

if [ $? != 0 ] ; then
	yum install createrepo -q -y
fi

CURRPATH=$(cd $(dirname $0); pwd)

cd $CURRPATH

for type in release testing
do
	for ver in centos5 centos6 neutral
	do
		for item in i386 x86_64 noarch
		do
			mkdir -p $CURRPATH/repo/mratwork/$type/$ver/$item
		done
	done
done

mkdir -p $CURRPATH/repo/mratwork/SRPMS

chmod -R o-w+r $CURRPATH

createrepo --database --update $CURRPATH/repo/mratwork/SRPMS

for type in release testing
do
	for ver in centos5 centos6 neutral
	do
		for item in i386 x86_64 noarch
		do
			createrepo --checkts --update $CURRPATH/repo/mratwork/$type/$ver/$item
		done
	done
done

### MR -- need change path because don't want path include '/home/repos/rpms.mratwork.com/repo/mratwork'
cd $CURRPATH/repo/mratwork/

zip -r9yD $CURRPATH/rpms-release-repodataonly.zip "./release" -x "*/*.rpm"
zip -r9yD $CURRPATH/rpms-testing-repodataonly.zip "./testing" -x "*/*.rpm"
zip -r9yD $CURRPATH/rpms-srpms-repodataonly.zip "./SRPMS" -x "*/*.rpm"

cd $CURRPATH
