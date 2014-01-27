#!/bin/bash

rpm --quiet -q createrepo

if [ $? != 0 ] ; then
	yum install createrepo -q -y
fi

CURRPATH=$(cd $(dirname $0); pwd)

cd $CURRPATH

### MR -- rpms ###
REPOPATH="$CURRPATH/repo/mratwork"

### MR -- release/testing portion ###
for a in release testing
do
	for b in neutral centos5 centos6
	do
		for c in noarch i386 x86_64
		do
			if [ -d $REPOPATH/$a/$b/$c ] ; then
				mv -f $REPOPATH/$a/$b/$c $REPOPATH/$a/$b/$a-$b-$c
			fi

			reposync --delete --config=$CURRPATH/mratwork-mirror.repo \
				--repoid=$a-$b-$c --download_path=$REPOPATH/$a/$b

			if [ -d $REPOPATH/$a/$b/$a-$b-$c ] ; then
				mv -f $REPOPATH/$a/$b/$a-$b-$c $REPOPATH/$a/$b/$c
			fi

			createrepo --checkts --update $REPOPATH/$a/$b/$c
		done
	done
done

### MR -- SRPMS portion ###
if [ "$(yum list installed kernel* | grep @)" == "" ] ; then
	reposync --delete --config=$CURRPATH/mratwork-mirror.repo \
		--repoid=SRPMS --download_path=$REPOPATH
else
	reposync --delete --norepopath --config=$CURRPATH/mratwork-mirror.repo \
		--repoid=SRPMS --download_path=$REPOPATH/SRPMS
fi

createrepo --checkts --update $REPOPATH/SRPMS

