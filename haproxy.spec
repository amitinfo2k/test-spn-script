Name: sxp-haproxy
Version:  %{version}
Release:  %{release}%{?dist}
Summary:  HA Proxy image

License:  GPL
URL:   None
Source:  sxp-haproxy

%description
HA Proxy image

#%prep
#%setup -n sxp-haproxy

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/haproxy
cp -R * $RPM_BUILD_ROOT/etc/haproxy

%files
/etc/haproxy

%clean
rm -rf $RPM_BUILD_ROOT
