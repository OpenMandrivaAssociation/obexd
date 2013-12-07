Summary:	D-Bus service for Obex Client access
Name:		obexd
Version:	0.48
Release:	5
Group:		Communications
License:	GPLv2+
Url:		http://www.bluez.org/
Source0:	http://www.kernel.org/pub/linux/bluetooth/obexd-%{version}.tar.xz
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libical)
BuildRequires:	pkgconfig(openobex)

%description
obexd contains obex-client, a D-Bus service to allow sending files
using the Obex Push protocol, common on mobile phones and
other Bluetooth-equipped devices.

%prep
%setup -q

%build
%configure2_5x --disable-server
%make

%install
%makeinstall_std

%files
%doc README AUTHORS doc/client-api.txt
%{_libexecdir}/obex-client
%{_datadir}/dbus-1/services/obex-client.service

