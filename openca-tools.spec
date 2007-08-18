Summary:	OpenCA Base Tools
Name:		openca-tools
Version:	1.0.0
Release:	%mkrel 1
License:	BSD-style
Group:		System/Servers
URL:		http://www.openca.org/
Source0:	openca-tools-%{version}.tar.gz
Patch0:		openca-tools-no_rpath.diff
Requires:	openssl >= 0.9.7
BuildRequires:	openssl >= 0.9.7
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	automake1.9
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
OpenCA Tools provide command line facilities for (1) digital signatures
generation and verifications and for (2) SCEP message handling.

%package -n	openca-scep
Summary:	OpenCA SCEP Tool
Group:		System/Servers

%description -n	openca-scep
OpenCA SCEP Tool

This product includes OpenCA software written by Massimiliano Pala
(madwolf@openca.org) and the OpenCA Group (www.openca.org)

%package -n	openca-sv
Summary:	OpenCA PKCS#7 tool
Group:		System/Servers

%description -n	openca-sv
OpenCA SV Tool is aimed to help you in generating PKCS#7 signatures and verify
them. This tool can also verify signatures generated with Netscape crypto()
javascript function.

This product includes OpenCA software written by Massimiliano Pala
(madwolf@openca.org) and the OpenCA Group (www.openca.org)

%prep

%setup -q
%patch0 -p0

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

%build
%serverbuild
rm -f configure
libtoolize --copy --force; aclocal-1.9 -I build; autoconf; automake-1.9 --add-missing --copy

%configure2_5x \
    --enable-engine \
    --with-openssl-prefix=%{_prefix} \
    --with-openca-prefix=%{_datadir}/openca \
    --with-openca-user=openca \
    --with-openca-group=openca

%install
rm -rf %{buildroot}

%makeinstall_std

# fix man pages
mv %{buildroot}%{_mandir}/man1/sign.1 %{buildroot}%{_mandir}/man1/openca-sign.1
mv %{buildroot}%{_mandir}/man1/verify.1 %{buildroot}%{_mandir}/man1/openca-verify.1

%clean
rm -rf %{buildroot}

%files -n openca-scep
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README examples/openca-scep
%attr(0755,root,root) %{_bindir}/openca-scep

%files -n openca-sv
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README examples/openca-sv
%attr(0755,root,root) %{_bindir}/openca-sv
%attr(0644,root,root) %{_mandir}/man1/openca-sign.1*
%attr(0644,root,root) %{_mandir}/man1/openca-verify.1*
