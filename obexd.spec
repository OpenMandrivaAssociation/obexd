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
