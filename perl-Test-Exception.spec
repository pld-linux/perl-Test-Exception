#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Exception
Summary:	Test::Exception - convenience routines for testing exception based code
Summary(pl.UTF-8):	Test::Exception - wygodne funkcje do testowania kodu bazującego na wyjątkach
Name:		perl-Test-Exception
Version:	0.32
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	50e985a335842540b69ea886eeed8a7f
URL:		http://search.cpan.org/dist/Test-Exception/
%if %{with tests}
BuildRequires:	perl(Test::Builder) >= 0.70
BuildRequires:	perl-Sub-Uplevel >= 0.18
BuildRequires:	perl-Test-Builder-Tester >= 1.07
BuildRequires:	perl-Test-Harness >= 2.03
BuildRequires:	perl-Test-Simple >= 0.70
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl(Test::Builder) >= 0.70
Requires:	perl-Sub-Uplevel >= 0.18
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a few convenience methods for testing exception
based code.  It is built with Test::Builder and plays happily with
Test::More and friends.

%description -l pl.UTF-8
Ten moduł udostępnia kilka wygodnych metod do testowania kodu
bazującego na wyjątkach. Jest budowany z użyciem Test::Builder, działa
sprawnie z Test::More i przyległościami.

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
%{perl_vendorlib}/Test/Exception.pm
%{_mandir}/man3/Test::Exception.3pm*
