%define major 0
%define libname %mklibname ytnef %major
%define devname %mklibname -d ytnef

Summary:	TNEF Stream Parser Library
Name:		libytnef
Version:	1.9.3
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		https://github.com/Yeraze/ytnef/
#Source0:	https://github.com/Yeraze/ytnef/archive/v1.9.3/ytnef-%{version}.tar.gz

#Looks like tarball is broken, use master git.
Source0:  https://github.com/Yeraze/ytnef/archive/ytnef-master.tar.gz

%description
TNEF Stream Parser Library to decode TNEF (winmail.dat) streams
generated by Microsoft Outlook.

%package -n %{libname}
Summary:	TNEF Stream Parser shared library
Group:		System/Libraries

%description -n %{libname}
TNEF Stream Parser Library to decode TNEF (winmail.dat) streams
generated by Microsoft Outlook.

%package -n %{devname}
Summary:	TNEF Stream Parser library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libytnef-devel = %{version}-%{release}

%description -n %{devname}
TNEF Stream Parser Library to decode TNEF (winmail.dat) streams
generated by Microsoft Outlook.

%prep
%setup -q -n ytnef-master

%build
#NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make_build


%install
%make_install

%files -n %{libname}
%{_libdir}/libytnef.so.%{major}*

%files -n %{devname}
%doc ChangeLog
%{_libdir}/libytnef.so
%{_includedir}/*.h

