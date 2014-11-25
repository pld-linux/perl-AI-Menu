%define		pdir	AI
%define		pnam	Menu
%include	/usr/lib/rpm/macros.perl
Summary:	AI::Menu - generate "Tree::Nary" objects from directed graphs
Summary(pl.UTF-8):	AI::Menu - generowanie obiektów "Tree::Nary" ze skierowanych grafów
Name:		perl-AI-Menu
Version:	0.01
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8272d6782f0cb041e27ffd50cd38ce56
URL:		http://search.cpan.org/dist/AI-Menu/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An "AI::Menu::Factory" object generates "Tree::Nary" objects from
directed graphs (Graph::Directed or an object with the same methods)
or a description of the function set.

%description -l pl.UTF-8
Obiekt AI::Menu::Factory generuje obiekty Tree::Nary ze skierowanych
grafów (Graph::Directed lub obiektu z tymi samymi metodami) lub opisu
zbioru funkcji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
