#!/bin/bash

rpm --quiet -q createrepo

if [ $? != 0 ] ; then
	yum install createrepo -q -y
fi

CURRPATH=$(cd $(dirname $0); pwd)

cd $CURRPATH

### MR -- CentAlt rpms ###
REPOPATH="$CURRPATH/repo/centalt"

for a in 5 6
do
	for b in i386 x86_64 SRPMS
	do
		if [ -d $REPOPATH/centos/$a/$b ] ; then
			mv -f $REPOPATH/centos/$a/$b $REPOPATH/centos/$a/centalt-centos-$a-$b
		fi

		reposync --delete --newest-only \
			--config=$CURRPATH/kloxomr-mirror.repo \
			--repoid=centalt-centos-$a-$b --download_path=$REPOPATH/centos/$a

		mv -f $REPOPATH/centos/$a/centalt-centos-$a-$b $REPOPATH/centos/$a/$b

		createrepo --checkts --update $REPOPATH/centos/$a/$b
	done
done

