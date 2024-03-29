Summary:	Tlen.pl protocol plugin for Pidgin
Summary(pl.UTF-8):	Tlen.pl plugin dla pidgina
Name:		libpurple-protocol-tlen
Version:	20101112
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://nic.com.pl/~alek/pidgin-tlen/pidgin-tlen-%{version}.tar.gz
# Source0-md5:	c7279014f492830ba93be138d9f2e9c0
URL:		http://nic.com.pl/~alek/pidgin-tlen/
BuildRequires:	libpurple-devel
BuildRequires:	pidgin-devel
BuildRequires:	pkgconfig
Obsoletes:	pidgin-plugin-tlen
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tlen.pl protocol plugin for Pidgin.

%description -l pl.UTF-8
Tlen.pl plugin dla Pidgina.

%prep
%setup -q -n pidgin-tlen-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="$(pkg-config pidgin --cflags) -fPIC -Wall %{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/purple-2
for i in 16 22 48; do \
	install -d $RPM_BUILD_ROOT%{_pixmapsdir}/pidgin/protocols/$i
	cp -a tlen_$i.png $RPM_BUILD_ROOT%{_pixmapsdir}/pidgin/protocols/$i/tlen.png
done
install -p libtlen.so $RPM_BUILD_ROOT%{_libdir}/purple-2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/purple-2/*.so
%{_pixmapsdir}/pidgin/protocols/*/tlen.png
