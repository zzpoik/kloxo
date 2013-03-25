zip -r9yD ./rpms-release-repodataonly.zip "./release" -x "*/*.rpm"
zip -r9yD ./rpms-testing-repodataonly.zip "./testing" -x "*/*.rpm"
zip -r9yD ./rpms-srpms-repodataonly.zip "./SRPMS" -x "*/*.rpm"