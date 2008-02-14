%define name	soma
%define version 2.4
%define release %mkrel 1
%define major	0
%define libname	%mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Basical soma suite
Group:		System/Servers
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
URL:		http://www.somasuite.org/
Source0:	http://www.somasuite.org/src/%{name}-%{version}.tar.gz
BuildRequires:	termcap-devel
BuildRequires:	readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  freetype-devel
BuildRequires:  openssl-devel
BuildRequires:  SDL-devel
BuildRequires:  perl
BuildRequires:  tetex-texi2html
BuildRequires:  libxml2-devel

%description
Basical soma suite. It contains somad, the broadcast sheduling demon,
somaclient, via tcp/ip administration utilities, and somacheck to check
configuration files.

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries

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

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL README README.module
%{_bindir}/*
%{_mandir}/*/*
%dir %{_sysconfdir}/somad
%config(noreplace) %{_sysconfdir}/somad/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/%{name}

