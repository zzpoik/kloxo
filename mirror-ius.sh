#!/bin/bash

rpm --quiet -q createrepo

if [ $? != 0 ] ; then
	yum install createrepo -q -y
fi

CURRPATH=$(cd $(dirname $0); pwd)

cd $CURRPATH

### MR -- IUS rpms ###
REPOPATH="$CURRPATH/repo/ius"

for a in 5
do
	for b in i386 x86_64 SRPMS
	do
		if [ -d $REPOPATH/centos/$a/$b ] ; then
			mv -f $REPOPATH/centos/$a/$b $REPOPATH/centos/$a/ius-centos-$a-$b
		fi

		reposync --delete --config=$CURRPATH/kloxomr-mirror.repo \
			--repoid=ius-centos-$a-$b --download_path=$REPOPATH/centos/$a

		mv -f $REPOPATH/centos/$a/ius-centos-$a-$b $REPOPATH/centos/$a/$b

		createrepo --checkts --update $REPOPATH/centos/$a/$b
	done
done

