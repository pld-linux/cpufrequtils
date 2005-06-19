#
# Conditional build:
%bcond_with	sysfs	# sysfs
%bcond_without	procfs	# procfs
#
Summary:	Scales your cpu frequency
Summary(pl):	Skalowanie czêstotliwo¶ci procesora
Name:		cpufrequtils
Version:	0.3
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.kernel.org/pub/linux/utils/kernel/cpufreq/%{name}-%{version}.tar.bz2
# Source0-md5:	ccd1423d76d19889652f06b7c018106b
URL:		http://www.kernel.org/pub/linux/utils/kernel/cpufreq/cpufrequtils.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
%{?with_sysfs:BuildRequires:	libsysfs-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TODO

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

cd utils
%{__libtoolize}
%{__aclocal}
%{__autoconf}
#%{__automake}
cd ..

cd libcpufreq
%{__libtoolize}
%{__aclocal}
%{__autoconf}
#%{__automake}
cd ..

%configure \
	%{?with_sysfs:--enable-sysfs=/sys} \
	%{?with_procfs:--enable-proc} \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(754,root,root) %{_sbindir}/*
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.conf
#%{_mandir}/man?/*
#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%dir %{_libdir}/%{name}
#%attr(755,root,root) %{_libdir}/%{name}/*
