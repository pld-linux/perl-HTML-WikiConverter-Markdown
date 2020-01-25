#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	WikiConverter-Markdown
Summary:	HTML::WikiConverter::Markdown - Convert HTML to Markdown markup
Summary(pl.UTF-8):	HTML::WikiConverter::Markdown - konwertowanie HTML-a do znaczników Markdown
Name:		perl-HTML-WikiConverter-Markdown
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b3db779cd034cdf2da2164b63a857f03
URL:		http://search.cpan.org/dist/HTML-WikiConverter-Markdown/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Tagset
BuildRequires:	perl-HTML-WikiConverter >= 0.67
BuildRequires:	perl-Params-Validate
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains rules for converting HTML into Markdown markup.
You should not use this module directly; HTML::WikiConverter is the
entry point for html->wiki conversion.

%description -l pl.UTF-8
Ten moduł zawiera reguły do konwersji HTML-a do znaczników Markdown.
Nie należy używać go bezpośrednio - punktem wejściowym do konwersji
HTML->Wiki jest HTML::WikiConverter.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/WikiConverter/Markdown.pm
%{_mandir}/man3/HTML::WikiConverter::Markdown.3pm*
