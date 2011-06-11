Summary:	Wifi and Bluetooth hardware switch GUI
Name:		acerhkgui
Version:	0.6
Release:	1
License:	GPL v2
Group:		Networking
Source0:	http://dl.sourceforge.net/acerhkgui/%{name}-%{version}.zip
# Source0-md5:	1aeb6918fb5c1583bc1585538f797234
URL:		http://sourceforge.net/projects/acerhkgui/
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AcerHK GUI enables the user to pass commands to the wireless
and bluetooth radios on Acer (TM) tablets that utilize the
AcerHK driver. It requires the acerhk.ko modules to be
installed.

%prep
%setup -q -n %{name}
sed -e -e '1s|env python|python|' -e "s|~/bin/acerhkgui/|%{_datadir}/%{name}/|" -i acerhkgui

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

install acerhkgui $RPM_BUILD_ROOT%{_bindir}
cp -a *.glade *.png $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a acerhkgui.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -a AcerHK.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*.png
