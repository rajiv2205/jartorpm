%define _tmppath /home/rpmbuild/rpm/tmp
Name:  Spring3HibernateApp         
Version:      2.0.1  
Release:        1%{?dist}
Summary:        crud application rpm deployment in tomcat

Group:          Applications/System
License:        Restricted
URL:            https://rajivsharma.com
BuildArch: noarch       

%description
First version of Spring3HibernateApp 


%prep
pwd
cd %{_sourcedir}
git clone https://github.com/OpsTree/ContinuousIntegration.git
echo "cloned successfully"

%build
cd %{_sourcedir}
cd ./ContinuousIntegration/Spring3HibernateApp
mvn clean install

%pre 
if [ "$1" = "1" ]; then
 echo "first time"  ;
# Perform tasks to prepare for the initial installation
elif [ "$1" = "2" ]; then
  echo "this is the upgrade"; 
  rm -rf /opt/tomcat7/webapps/Spring3HibernateApp* 
# Perform whatever maintenance must occur before the upgrade begins
fi

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/tomcat7/webapps/
cp -r %{_sourcedir}/ContinuousIntegration/Spring3HibernateApp/target/Spring3HibernateApp.war  $RPM_BUILD_ROOT/opt/tomcat7/webapps/

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf  %{_sourcedir}

%preun

%files
%defattr(-,root,root)
%doc
%defattr(644,root,root)
%dir %attr(755, root,root) /opt/tomcat7/webapps/
%attr(644,root,root) /opt/tomcat7/webapps/Spring3HibernateApp.war


%changelog
