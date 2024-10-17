#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/PROTO/eyelight eyelight; \
#cd eyelight; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf eyelight-$PKG_VERSION.tar.xz eyelight/ --exclude .svn --exclude .*ignore

%define svnrev	68638

%define major   0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Eyelight is a simple EFL based presentation tool
Name:		eyelight
Version:	0.5.0
Release:	0.%{svnrev}.3
License:	GPLv2.1
URL:		https://enlightenment.org/
Source0: 	%{name}-%{version}.%{svnrev}.tar.xz
Source100:	eyelight.rpmlintrc
Patch0:		add-libeet.patch
Patch1:		fix-include-paths.patch
Group:		Graphical desktop/Enlightenment

BuildRequires:	doxygen
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(embryo)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(eet)

%description
Eyelight is a simple EFL based presentation tool

%package -n %{libname}
Summary:    Eyelight library
Group:      System/Libraries

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{develname}
Summary:    Eyelight headers, libraries, documentation and test programs
Group:      Development/Other
Requires:   %{libname} = %{version}
Provides:   %{name}-devel = %{version}-%{release}

%description -n %{develname}
Headers and libraries from %{name}

%prep
%setup -qn %{name}
%autopatch -p1

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std
find %{buildroot} -name *.la | xargs rm

%files
%{_bindir}/*
%{_datadir}/%{name}/themes/default/fonts/*
%{_datadir}/%{name}/themes/default/theme.edj
%{_datadir}/%{name}/themes/default/transition/*.edc
%{_datadir}/%{name}/viewer/*.ttf

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*



%changelog
* Wed Jul 04 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.5.0-0.68638.1
+ Revision: 808110
- version update 0.5.0.68638

* Thu Jan 12 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.5.0-0.62296.1
+ Revision: 760245
- fixed build
- fixed BR
- imported package eyelight

