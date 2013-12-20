%_javapackages_macros
%global short_name plexus-tools

Name:           %{short_name}-pom
Version:        1.0.11
Release:        8.0%{?dist}
Summary:        Plexus Tools POM
BuildArch:      noarch

License:        ASL 2.0
URL:            http://plexus.codehaus.org/%{short_name}
Source0:        http://repo.maven.apache.org/maven2/org/codehaus/plexus/%{short_name}/%{version}/%{short_name}-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  plexus-pom

%description
This package provides Plexus Tools parent POM used by different
Plexus packages.

%prep
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%pom_disable_module plexus-cdc
%pom_disable_module plexus-cdc-anno
%pom_disable_module plexus-cli
%pom_disable_module plexus-javadoc

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE
