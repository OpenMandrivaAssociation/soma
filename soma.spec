%define name	soma
%define version 2.1
%define release %mkrel 1
%define major	0
%define libname	%mklibname %{name} %{major}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Basical soma suite
Group:		System/Servers
License:	GPL
URL:		http://www.somasuite.org/
Source0:	http://www.somasuite.org/src/%{name}-%{version}.tar.bz2
Source1:	%{name}-%{version}.faq.texi.bz2
Source2:	%{name}-%{version}.hooks.texi.bz2
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

%package -n	%{libname}-devel
Summary:	Static libraries and header files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}

%description -n	%{libname}-devel
This package contains the static development libraries and headers needed
to compile applications linked with %{name} libraries.

%prep
%setup -q
bzcat %{SOURCE1} > ffmpeg/ffmpeg/doc/faq.texi
bzcat %{SOURCE2} > ffmpeg/ffmpeg/doc/hooks.texi

%build
%configure
make

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
%{_datadir}/%{name}
%dir %{_sysconfdir}/somad
%config(noreplace) %{_sysconfdir}/somad/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/%{name}

