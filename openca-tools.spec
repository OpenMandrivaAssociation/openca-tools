Summary:	OpenCA Base Tools
Name:		openca-tools
Version:	1.3.0
Release:	3
License:	BSD-style
Group:		System/Servers
URL:		https://www.openca.org/
Source0:	http://prdownloads.sourceforge.net/openca/%name-%version.tar.gz
Patch0:		openca-tools-no_rpath.diff
Patch2:		openca-tools-1.1.0-format_not_a_string_literal_and_no_format_arguments.diff
Requires:	openssl >= 0.9.7
BuildRequires:	openssl >= 0.9.7
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
OpenCA Tools provide command line facilities for (1) digital signatures
generation and verifications and for (2) SCEP message handling.

%package -n	openca-scep
Summary:	OpenCA SCEP Tool
Group:		System/Servers
License:	BSD-style

%description -n	openca-scep
OpenCA SCEP Tool

%package -n	openca-sv
Summary:	OpenCA PKCS#7 tool
Group:		System/Servers
License:	BSD-style

%description -n	openca-sv
OpenCA SV Tool is aimed to help you in generating PKCS#7 signatures and verify
them. This tool can also verify signatures generated with Netscape crypto()
javascript function.

%package -n	openca-crmf
Summary:	OpenCA CRMF Tool
Group:		System/Servers
License:	GPLv2

%description -n	openca-crmf
OpenCA CRMF Tool

%prep

%setup -q
%patch0 -p0
%patch2 -p1

# fix borkiness
perl -pi -e "s|/etc/issue|/etc/mandriva-release|g" configure*

%build
%serverbuild
rm -f configure
autoreconf -fi

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

%files -n openca-crmf
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/openca-crmf


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2011.0
+ Revision: 613530
- rebuild

* Mon Apr 19 2010 Funda Wang <fwang@mandriva.org> 1.3.0-1mdv2010.1
+ Revision: 536580
- New version 1.3.0

* Mon Oct 05 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-3mdv2010.0
+ Revision: 454029
- P1: fix format string errors
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Oct 15 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-1mdv2009.1
+ Revision: 293923
- 1.1.0
- rediffed P1

* Mon Jul 14 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdv2009.0
+ Revision: 234495
- rebuild
- fix build

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Aug 18 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2008.0
+ Revision: 65479
- fix build
- Import openca-tools



* Sat Aug 18 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2008.0
- initial Mandriva package
