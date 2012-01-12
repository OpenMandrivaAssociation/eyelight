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

%define svnrev	62296

%define major   0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Eyelight is a simple EFL based presentation tool
Name:		eyelight
Version:	0.5.0
Release:	0.%{svnrev}.1
License:	GPLv2.1
URL:		http://enlightenment.org/
Source: 	%{name}-%{version}.%{svnrev}.tar.xz
Group:		Graphical desktop/Enlightenment

BuildRequires:	edje
BuildRequires:	embryo
BuildRequires:	evas
BuildRequires:	pkgconfig(png)
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(edje)

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

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
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

