%define name	soma
%define version 2.4
%define release %mkrel 7
%define major	2
%define libname	%mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Basical soma suite
Group:		System/Servers
License:	GPL
URL:		http://www.somasuite.org/
Source0:	http://www.somasuite.org/src/%{name}-%{version}.tar.gz
Patch0:     soma-2.4-fix-format-errors.patch
Patch1:     soma-2.4-fix-open-calls.patch
Patch2: soma-2.4-ffmpeg.patch
Patch3: soma-2.4-link.patch
BuildRequires:	readline-devel
BuildRequires:  openssl-devel
BuildRequires:  libxml2-devel
BuildRequires:  ffmpeg-devel
BuildRequires:	confuse-devel
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
Basical soma suite. It contains somad, the broadcast sheduling demon,
somaclient, via tcp/ip administration utilities, and somacheck to check
configuration files.

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}soma0 < 2.4-7

%description -n	%{libname}
This package contains the libraries needed to run programs dynamically
linked with %{name} libraries.

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d %{name} 0}

%description -n	%{develname}
This package contains the static development libraries and headers needed
to compile applications linked with %{name} libraries.

%prep
%setup -q
%patch0 -p 1
%patch1 -p 1
%patch2 -p0
%patch3 -p0

%build
libtoolize
aclocal
autoconf
automake
%configure2_5x --enable-ffmpeg
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL README README.module
%{_bindir}/*
%{_mandir}/*/*
%dir %{_sysconfdir}/somad
%config(noreplace) %{_sysconfdir}/somad/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/%{name}

