#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Exception
Summary:	Test::Exception - Convenience routines for testing exception based code
Summary(pl):	Test::Exception - wygodne funkcje do testowania kodu bazuj±cego na wyj±tkach
Name:		perl-Test-Exception
Version:	0.15
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-IO-String
BuildRequires:	perl-Pod-Coverage
BuildRequires:	perl-Sub-Uplevel
BuildRequires:	perl-Test-Builder-Tester
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a few convenience methods for testing exception
based code.  It is built with Test::Builder and plays happily with
Test::More and friends.

%description -l pl
Ten modu³ udostêpnia kilka wygodnych metod do testowania kodu
bazuj±cego na wyj±tkach. Jest budowany z u¿yciem Test::Builder, dzia³a
sprawnie z Test::More i przyleg³o¶ciami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
