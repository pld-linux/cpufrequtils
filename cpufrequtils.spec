#
# Conditional build:
%bcond_with	sysfs	# sysfs (detection broken)
%bcond_without	procfs	# procfs
#
Summary:	Scales your CPU frequency
Summary(pl):	Skalowanie czêstotliwo¶ci procesora
Name:		cpufrequtils
Version:	0.3
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.kernel.org/pub/linux/utils/kernel/cpufreq/%{name}-%{version}.tar.bz2
# Source0-md5:	ccd1423d76d19889652f06b7c018106b
URL:		http://www.kernel.org/pub/linux/utils/kernel/cpufreq/cpufrequtils.html
%{?with_sysfs:BuildRequires:	libsysfs-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scales your CPU frequency.

%description -l pl
Skalowanie czêstotliwo¶ci procesora.

%package devel
Summary:	Header file for libcpufreq library
Summary(pl):	Plik nag³ówkowy biblioteki libcpufreq
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for libcpufreq library.

%description devel -l pl
Plik nag³ówkowy biblioteki libcpufreq.

%prep
%setup -q

%build
%configure \
	%{?with_sysfs:--enable-sysfs=/sys} \
	%{?with_procfs:--enable-proc} \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(754,root,root) %{_bindir}/cpufreq-*
%attr(755,root,root) %{_libdir}/libcpufreq.so.*.*.*
%{_mandir}/man1/cpufreq-*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcpufreq.so
%{_libdir}/libcpufreq.la
%{_includedir}/cpufreq.h
