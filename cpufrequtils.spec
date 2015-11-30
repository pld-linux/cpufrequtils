#
# Conditional build:
%bcond_without	sysfs	# sysfs support
%bcond_without	procfs	# procfs support
#
Summary:	Scaling your CPU frequency
Summary(pl.UTF-8):	Skalowanie częstotliwości procesora
Name:		cpufrequtils
Version:	008
Release:	4
Epoch:		1
License:	GPL v2
Group:		Applications/System
#Source0:	https://www.kernel.org/pub/linux/utils/kernel/cpufreq/%{name}-%{version}.tar.bz2
Source0:	http://ftp.sunet.se/pub/Linux/kernel.org/linux/utils/kernel/cpufreq/%{name}-%{version}.tar.bz2
# Source0-md5:	c59b71c044d463896f3247e8dd83dd7e
# 404 as of Dec 2013, use mirror
#URL:		https://www.kernel.org/pub/linux/utils/kernel/cpufreq/cpufrequtils.html
URL:		http://ftp.sunet.se/pub/Linux/kernel.org/linux/utils/kernel/cpufreq/cpufrequtils.html
BuildRequires:	gettext-tools
%{?with_sysfs:BuildRequires:	sysfsutils-devel >= 1.3.0-3}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scaling your CPU frequency.

%description -l pl.UTF-8
Skalowanie częstotliwości procesora.

%package libs
Summary:	cpufrequtils library
Summary(pl.UTF-8):	Biblioteka skalująca częstotliwość procesora
Group:		Libraries

%description libs
cpufrequtils library.

%description libs -l pl.UTF-8
Biblioteka skalująca częstotliwość procesora.

%package devel
Summary:	Header file for libcpufreq library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libcpufreq
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
%{?with_sysfs:Requires:	sysfsutils-devel >= 1.3.0-3}
Obsoletes:	cpufrequtils-static
Conflicts:	kernel-tools-cpupower-libs-devel

%description devel
Header file for libcpufreq library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki libcpufreq.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	OPTIMIZATION="%{rpmcflags}" \
	V=true \
	%{!?with_sysfs:SYSFS=false} \
	%{!?with_procfs:PROC=false}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir} \
	mandir=%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/cpufreq-*
%{_mandir}/man1/cpufreq-*.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcpufreq.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcpufreq.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcpufreq.so
%{_includedir}/cpufreq.h
