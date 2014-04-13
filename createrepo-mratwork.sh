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

echo "*** Delete old repodata dirs..."
find $CURRPATH/repo/mratwork/ -type d -name "repodata" -exec rm -rf {} \; >/dev/null 2>&1

echo "*** Process for SRPMS..."
createrepo $CURRPATH/repo/mratwork/SRPMS

for type in release testing
do
	for ver in centos5 centos6 neutral
	do
		for item in i386 x86_64 noarch
		do
			echo "*** Process for '$type-$ver-$item'..."
			createrepo $CURRPATH/repo/mratwork/$type/$ver/$item
		done
	done
done

find $CURRPATH/repo/mratwork/ -type d -name ".repodata" -exec rm -rf {} \; >/dev/null 2>&1

### MR -- need change path because don't want path include '/home/repos/rpms.mratwork.com/repo/mratwork'
cd $CURRPATH/repo/mratwork/

echo "*** Zip repodata..."
echo "- For release"
zip -r9yD $CURRPATH/rpms-release-repodataonly.zip "./release" -x "*/*.rpm"
echo "- For testing"
zip -r9yD $CURRPATH/rpms-testing-repodataonly.zip "./testing" -x "*/*.rpm"
echo "- For SRPMS"
zip -r9yD $CURRPATH/rpms-srpms-repodataonly.zip "./SRPMS" -x "*/*.rpm"

cd $CURRPATH
