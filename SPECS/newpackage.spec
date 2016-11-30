%define _tmppath /home/rpmbuild/rpm/tmp
Name:  testjar         
Version:      1.0.1  
Release:        1%{?dist}
Summary:        test jar for testing

Group:          Applications/System
License:        Restricted
URL:            https://private.com
BuildArch: noarch       

%description
First version of jar

%prep



%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
cp -r %{_tmppath}/testjar/ $RPM_BUILD_ROOT/usr/local
mkdir -p $RPM_BUILD_ROOT/usr/local/testjar/logs
mkdir -p $RPM_BUILD_ROOT/etc/init.d
cp -r %{_tmppath}/testjar/testjarservice $RPM_BUILD_ROOT/etc/init.d
mkdir -p $RPM_BUILD_ROOT/var/run/testjar

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc
%defattr(644,root,root)
%dir %attr(755, root,root)/usr/local/testjar
/usr/local/testjar
%attr(755,root,root) /etc/init.d/testjarservice
%dir %attr(755, root,root)/usr/local/testjar/testjarservice
%dir %attr(755,root,root) /var/run/testjar


%changelog
