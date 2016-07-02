Name:          ambience-jollait
Version:       0.1.2
Release:       2
Summary:       Jolla Community Italia ambience
Group:         System/Tools
Vendor:        fravaccaro
Distribution:   SailfishOS
Packager:      fravaccaro <fravaccaro@jollacommunity.it>
URL:            www.jollacommunity.it

License:       GPL

%description
Official ambience from Jolla Community Italia, the Italian Jolla and Sailfish OS community.

%files

%defattr(-,root,root,-)
/usr/share/ambience/*

%post
chmod 755 /usr/share/ambience/{name}
chmod 755 /usr/share/ambience/{name}/images
chmod 644 /usr/share/ambience/{name}/*.*
chmod 644 /usr/share/ambience/{name}/images/*.*
systemctl-user restart ambienced.service

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm -rf /usr/share/ambience/{name}
systemctl-user restart ambienced.service
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "It's just upgrade"
systemctl-user restart ambienced.service
fi
fi

%changelog
* Mon May 29 2016 0.1
- First build.
