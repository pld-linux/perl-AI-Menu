%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	Menu
Summary:	AI::Menu - generate "Tree::Nary" objects from directed graphs
Summary(pl):	AI::Menu - generowanie obiektów "Tree::Nary" ze skierowanych grafów
Name:		perl-%{pdir}-%{pnam}
Version:	0.01
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8272d6782f0cb041e27ffd50cd38ce56
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An "AI::Menu::Factory" object generates "Tree::Nary" objects from
directed graphs (Graph::Directed or an object with the same methods)
or a description of the function set.

%description -l pl
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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
