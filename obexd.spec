Name:		obexd
Version:	0.46
Release:	%mkrel 1
Summary:	D-Bus service for Obex Client access

Group:		Communications
License:	GPLv2+
Source0:	http://www.kernel.org/pub/linux/bluetooth/obexd-%{version}.tar.gz
Url:		http://www.bluez.org/

BuildRequires:	glib2-devel
BuildRequires:	dbus-devel
BuildRequires:	bluez-devel >= 4.99
BuildRequires:	openobex-devel
BuildRequires:  libical-devel

%description
obexd contains obex-client, a D-Bus service to allow sending files
using the Obex Push protocol, common on mobile phones and
other Bluetooth-equipped devices.

%prep
%setup -q

%build
%configure2_5x --disable-server
%make

chmod -x test/send-files

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%doc README AUTHORS doc/client-api.txt test/send-files
%{_libexecdir}/obex-client
%{_datadir}/dbus-1/services/obex-client.service


%changelog
* Sun May 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.46-1mdv2012.0
+ Revision: 799741
- version update 0.46

* Fri Mar 09 2012 Götz Waschk <waschk@mandriva.org> 0.45-1
+ Revision: 783685
- bump bluez dep
- update to new version 0.45

* Sat Jan 14 2012 Götz Waschk <waschk@mandriva.org> 0.44-1
+ Revision: 760814
- update to new version 0.44

* Sun Jan 01 2012 Götz Waschk <waschk@mandriva.org> 0.43-1
+ Revision: 748638
- update to new version 0.43

* Tue Aug 02 2011 Götz Waschk <waschk@mandriva.org> 0.42-1
+ Revision: 692722
- update to new version 0.42

* Wed Jun 22 2011 Götz Waschk <waschk@mandriva.org> 0.41-1
+ Revision: 686589
- update to new version 0.41

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.40-3
+ Revision: 666935
- mass rebuild

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.40-2
+ Revision: 640304
- rebuild to obsolete old packages

* Sat Jan 22 2011 Götz Waschk <waschk@mandriva.org> 0.40-1
+ Revision: 632211
- update to new version 0.40

* Sat Jan 15 2011 Götz Waschk <waschk@mandriva.org> 0.39-1
+ Revision: 631101
- update to new version 0.39

* Wed Dec 29 2010 Götz Waschk <waschk@mandriva.org> 0.38-1mdv2011.0
+ Revision: 626011
- update to new version 0.38

* Thu Nov 25 2010 Götz Waschk <waschk@mandriva.org> 0.37-1mdv2011.0
+ Revision: 600999
- update to new version 0.37

* Sun Nov 07 2010 Götz Waschk <waschk@mandriva.org> 0.36-1mdv2011.0
+ Revision: 594480
- update to new version 0.36

* Mon Oct 18 2010 Götz Waschk <waschk@mandriva.org> 0.35-1mdv2011.0
+ Revision: 586585
- update to new version 0.35

* Fri Oct 08 2010 Götz Waschk <waschk@mandriva.org> 0.34-1mdv2011.0
+ Revision: 584136
- update to new version 0.34

* Sun Sep 12 2010 Götz Waschk <waschk@mandriva.org> 0.33-1mdv2011.0
+ Revision: 577633
- update to new version 0.33

* Sat Aug 28 2010 Götz Waschk <waschk@mandriva.org> 0.32-1mdv2011.0
+ Revision: 573778
- update to new version 0.32

* Wed Aug 25 2010 Emmanuel Andry <eandry@mandriva.org> 0.31-1mdv2011.0
+ Revision: 573339
- New version 0.31

* Thu Aug 05 2010 Emmanuel Andry <eandry@mandriva.org> 0.30-1mdv2011.0
+ Revision: 566395
- New version 0.30

* Mon Jul 19 2010 Götz Waschk <waschk@mandriva.org> 0.29-1mdv2011.0
+ Revision: 554908
- update to new version 0.29

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 0.28-1mdv2011.0
+ Revision: 550342
- update build deps
- update to new version 0.28

* Sat Apr 24 2010 Emmanuel Andry <eandry@mandriva.org> 0.23-1mdv2010.1
+ Revision: 538492
- New version 0.23

* Wed Mar 17 2010 Emmanuel Andry <eandry@mandriva.org> 0.22-1mdv2010.1
+ Revision: 523611
- New version 0.22

* Mon Dec 28 2009 Götz Waschk <waschk@mandriva.org> 0.21-1mdv2010.1
+ Revision: 482953
- update to new version 0.21

* Sun Dec 13 2009 Götz Waschk <waschk@mandriva.org> 0.20-1mdv2010.1
+ Revision: 478107
- update to new version 0.20

* Sun Nov 22 2009 Götz Waschk <waschk@mandriva.org> 0.19-1mdv2010.1
+ Revision: 469082
- update to new version 0.19

* Sun Sep 27 2009 Emmanuel Andry <eandry@mandriva.org> 0.18-1mdv2010.0
+ Revision: 449966
- New version 0.18

* Wed Aug 26 2009 Emmanuel Andry <eandry@mandriva.org> 0.17-1mdv2010.0
+ Revision: 421562
- New version 0.17

* Wed Aug 19 2009 Emmanuel Andry <eandry@mandriva.org> 0.16-1mdv2010.0
+ Revision: 418003
- New version 0.16

* Fri Aug 07 2009 Götz Waschk <waschk@mandriva.org> 0.15-1mdv2010.0
+ Revision: 411134
- import obexd

