#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Exception
Summary:	Test::Exception - convenience routines for testing exception based code
Summary(pl):	Test::Exception - wygodne funkcje do testowania kodu bazuj±cego na wyj±tkach
Name:		perl-Test-Exception
Version:	0.24
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	63013cbd55f9a8e2b8ce02f927fec32d
URL:		http://search.cpan.org/dist/Test-Exception/
%if %{with tests}
BuildRequires:	perl(Test::Builder) >= 0.33
BuildRequires:	perl-Sub-Uplevel >= 0.13
BuildRequires:	perl-Test-Builder-Tester >= 1.04
BuildRequires:	perl-Test-Harness >= 2.03
BuildRequires:	perl-Test-Simple >= 0.44
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl(Test::Builder) >= 0.33
Requires:	perl-Sub-Uplevel >= 0.13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
