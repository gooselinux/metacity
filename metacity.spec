%define _default_patch_fuzz 999

Summary: Unobtrusive window manager
Name: metacity
Version: 2.28.0
Release: 20%{?dist}
URL: http://download.gnome.org/sources/metacity/
Source0: http://download.gnome.org/sources/metacity/2.28/metacity-%{version}.tar.bz2
Patch0: default-theme.patch
# http://bugzilla.gnome.org/show_bug.cgi?id=558723
Patch4: stop-spamming-xsession-errors.patch
# http://bugzilla.gnome.org/show_bug.cgi?id=135056
Patch5: dnd-keynav.patch
# http://bugzilla.gnome.org/show_bug.cgi?id=588119
Patch6: Should-set-RestartStyleHint-to-RestartIfRunning-when.patch
# http://bugzilla.gnome.org/show_bug.cgi?id=593355
Patch7: 0001-bell-increase-bell-rate-limit-from-1-s-to-1-100ms.patch
# http://bugzilla.gnome.org/show_bug.cgi?id=593356
Patch8: 0001-sound-ask-libcanberra-to-cache-alert-desktop-switch-.patch
# http://bugzilla.gnome.org/show_bug.cgi?id=593358
Patch9: 0001-tooltip-set-window-type-hint-for-self-drawn-tooltips.patch
# http://bugzilla.gnome.org/show_bug.cgi?id=336750
Patch10: screenshot-forkbomb.patch

# fedora specific patches
Patch11: workspaces.patch
Patch12: fresh-tooltips.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=600864
# https://bugzilla.redhat.com/show_bug.cgi?id=533239
Patch13: metacity-dont-do-bad-stuff-on-sigterm.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=567528
Patch14: Allow-explicit-raises-from-same-client-not-just-sa.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=445447
Patch15: Allow-applications-to-raise-windows-when-raise_on_cl.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=598995
Patch16: Dont-focus-ancestor-window-on-a-different-workspac.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=599262
Patch17: Add-XFCE-Terminal-as-a-terminal.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=599097
Patch18: For-mouse-and-sloppy-focus-return-to-mouse-mode-on.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=599248
Patch19: Add-nofocuswindows-preference-to-list-windows-that.patch
Patch119: Exclude-the-current-application-from-no_focus_window.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=599261
Patch20: Add-a-newwindowsalwaysontop-preference.patch
Patch120: Apply-new_windows_always_on_top-to-newly-raised-acti.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=577576
Patch21: Dont-warn-about-a-missing-session-file.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=530702
Patch22: cm-selection-timestamp.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=598231
Patch23: metacity-2.28-visual-bell.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=559816
Patch24: metacity-2.28-empty-keybindings.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=604319
Patch25: metacity-2.28-xioerror-unknown-display.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=604867
Patch26: metacity-2.28-IceCloseConnection.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=589227
# Translation of non-upstream strings (mostly GConf key descriptions)
Patch27: metacity-2.28.0-translation.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=599181
Patch28: Stop-confusing-GDK-s-grab-tracking.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=622517
Patch29: Allow-breaking-out-from-maximization-during-mouse.patch
# This is a bit of an upstream bug fix post 2.28 that is needed
# for correct operation of Patch29.
# (See https://bugzilla.gnome.org/show_bug.cgi?id=461927).
# If we pull in the full fix for 461927 at any point this patch
# can be dropped.
Patch30: metacity-2.28.0-unmaximize-user-rect.patch

License: GPLv2+
Group: User Interface/Desktops
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gtk2-devel >= 2.2.0
BuildRequires: pango-devel >= 1.2.0
BuildRequires: fontconfig-devel
BuildRequires: GConf2-devel >= 2.2.0
BuildRequires: desktop-file-utils >= 0.3
BuildRequires: libglade2-devel >= 2.0.0
BuildRequires: autoconf, automake, libtool
BuildRequires: intltool >= 0.35
BuildRequires: startup-notification-devel >= 0.7
BuildRequires: libtool automake autoconf gettext
BuildRequires: xorg-x11-proto-devel >= 7.0-13
BuildRequires: libSM-devel, libICE-devel, libX11-devel
BuildRequires: libXext-devel, libXinerama-devel, libXrandr-devel, libXrender-devel
BuildRequires: libXcursor-devel
BuildRequires: libXcomposite-devel, libXdamage-devel
# for gnome-keybindings.pc
BuildRequires: control-center >= 2.19.4
BuildRequires: gnome-doc-utils
BuildRequires: zenity
BuildRequires: dbus-devel
BuildRequires: libcanberra-devel

Requires: startup-notification >= 0.7
Requires: gnome-themes
# for /usr/share/control-center/keybindings, /usr/share/gnome/wm-properties
Requires: control-center-filesystem
# for /etc/gconf/schemas
Requires: GConf2
Requires: zenity

Requires(post): GConf2 >= 2.14
Requires(post): /sbin/ldconfig
Requires(pre): GConf2 >= 2.14
Requires(preun): GConf2 >= 2.14

%description
Metacity is a window manager that integrates nicely with the GNOME desktop.
It strives to be quiet, small, stable, get on with its job, and stay out of
your attention.

%package devel
Group: Development/Libraries
Summary: Development files for metacity
Requires: gtk2-devel, libX11-devel
Requires: pkgconfig
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the files needed for compiling programs using
the metacity-private library. Note that you are not supposed to write
programs using the metacity-private library, since it is a private
API. This package exists purely for technical reasons.

%prep
%setup -q
%patch0 -p1 -b .default-theme
%patch4 -p1 -b .stop-spamming-xsession-errors
%patch5 -p1 -b .dnd-keynav
%patch6 -p1 -b .restart-if-running
%patch7 -p1 -b .bell
%patch8 -p1 -b .sound-cache
%patch9 -p1 -b .tooltip
%patch10 -p1 -b .screenshot-forkbomb
%patch11 -p1 -b .workspaces
%patch12 -p1 -b .fresh-tooltips
%patch13 -p1 -b .sigterm

%patch14 -p1 -b .raises-from-same-client
%patch15 -p1 -b .raise-on-click-stacking
%patch16 -p1 -b .focus-different-workspace
%patch17 -p1 -b .xfce-terminal
%patch18 -p1 -b .focus-on-motion
%patch19 -p1 -b .no-focus-windows
%patch119 -p1 -b .no-focus-windows-current-app
%patch20 -p1 -b .always-on-top
%patch120 -p1 -b .always-on-top-activate
%patch21 -p1 -b .missing-session
%patch22 -p1 -b .cm-selection-timestamp
%patch23 -p1 -b .visual-bell
%patch24 -p1 -b .empty-keybindings
%patch25 -p1 -b .xioerror-unknown-display
%patch26 -p1 -b .IceCloseConnection
%patch27 -p1 -b .translation
%patch28 -p1 -b .grab-tracking
%patch29 -p1 -b .mouse-unmaximize
%patch30 -p1 -b .unmaximize-user-rect

# force regeneration
rm src/metacity.schemas

autoreconf -i -f

%build
rm -rf $RPM_BUILD_ROOT

CPPFLAGS="$CPPFLAGS -I$RPM_BUILD_ROOT%{_includedir}"
export CPPFLAGS

%configure

SHOULD_HAVE_DEFINED="HAVE_SM HAVE_XINERAMA HAVE_XFREE_XINERAMA HAVE_SHAPE HAVE_RANDR HAVE_STARTUP_NOTIFICATION"

for I in $SHOULD_HAVE_DEFINED; do
  if ! grep -q "define $I" config.h; then
    echo "$I was not defined in config.h"
    grep "$I" config.h
    exit 1
  else
    echo "$I was defined as it should have been"
    grep "$I" config.h
  fi
done

make CPPFLAGS="$CPPFLAGS" LIBS="$LIBS"

%if 0
# strip unneeded translations from .mo files
cd po
grep -v ".*[.]desktop[.]in$\|.*[.]server[.]in$" POTFILES.in > POTFILES.keep
mv POTFILES.keep POTFILES.in
intltool-update --pot
for p in *.po; do
  msgmerge $p metacity.pot > $p.out
  msgfmt -o `basename $p .po`.gmo $p.out
done
%endif

%install
rm -rf $RPM_BUILD_ROOT

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

# the desktop file is not valid, I've complained on metacity-devel-list
#desktop-file-install --vendor "" --delete-original \
#	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
#	$RPM_BUILD_ROOT%{_datadir}/applications/metacity.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/metacity.schemas > /dev/null || :

%pre
if [ "$1" -gt 1 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
   gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/metacity.schemas > /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
   gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/metacity.schemas > /dev/null || :
fi

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS COPYING NEWS HACKING doc/theme-format.txt doc/metacity-theme.dtd rationales.txt
%{_bindir}/metacity
%{_bindir}/metacity-message
%{_sysconfdir}/gconf/schemas/*.schemas
%{_datadir}/metacity
%{_datadir}/themes/*
%{_datadir}/gnome-control-center/keybindings/*
%{_libdir}/lib*.so.*
%{_mandir}/man1/metacity.1.gz
%{_mandir}/man1/metacity-message.1.gz
%{_datadir}/applications/metacity.desktop
%{_datadir}/gnome/wm-properties/metacity-wm.desktop
%{_datadir}/gnome/help/creating-metacity-themes

%files devel
%defattr(-,root,root)
%{_bindir}/metacity-theme-viewer
%{_bindir}/metacity-window-demo
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man1/metacity-theme-viewer.1.gz
%{_mandir}/man1/metacity-window-demo.1.gz

%changelog
* Thu Aug 19 2010 Owen Taylor <otaylor@redhat.com> - 2.28.0-20
- Fix cases where unmaximized size wouldn't be honored when unmaximizing
  in reduced resources mode.
  Resolves: rhbz 523520

* Tue Aug 10 2010 Owen Taylor <otaylor@redhat.com> - 2.28.0-19
- Fix breaking out from maximization in reduced resources mode; bug
  discovered in testing resulted in mis-positioning in that case.
  Resolves: rhbz 523520

* Wed Jul 14 2010 Jon McCann <jmccann@redhat.com> - 2.28.0-18
- Change default theme to Slider
  Resolves: #611864

* Wed Jun 23 2010 Owen Taylor <otaylor@redhat.com> - 2.28.0-17
- Add patch to allow breaking out from maximization during mouse resize
  Resolves: rhbz 523520
- Add patches that tweak behaviors of RHEL 5.5 added GConf preferences
   - apply new_windows_always_on_top to windows that are raised
     or activated but denied focus as well.
   - exclude the current application from the effect of no_focus_windows
     preference
  Resolves: rhbz 607390

* Wed Jun 23 2010 Owen Taylor <otaylor@redhat.com> - 2.28.0-16
- Add a patch to fix confusion between windows
  Resolves: rhbz 588926
- Add translation updates
  Resolves: rhbz 589227

* Sun Jan  3 2010 Owen Taylor <otaylor@redhat.com> - 2.28.0-14
- Fix crash in _IceTransClose (rhbz 551994)
  The previous patch for rhbz 539905 didn't actually fix the
  problem; the ICE connection was still being closed twice.

* Thu Dec 17 2009 Owen Taylor <otaylor@redhat.com> - 2.28.0-13
- Fix crash in in tooltip on_style_set() (rhbz 546509)
- Fix Crash in SmcSetProperties() on exit (rhbz 539905, gnome 604867)

* Thu Dec 10 2009 Owen Taylor <otaylor@redhat.com> - 2.28.0-12
- Require gnome-themes rather than nodoka-metacity-theme (rhbz 532455, Stijn Hoop)
- Add patches for GNOME bugs
   445447 - Application-induced window raise fails when raise_on_click off (rhbz 526045)
   530702 - compiz doesn't start if metacity compositor is enabled (rhbz 537791)
   559816 - Doesn't update keybindings being disabled/cleared (rhbz 473224)
   567528 - Cannot raise windows from applications in Tcl/Tk and Java (rhbz 503522)
   577576 - Failed to read saved session file warning on new sessions (rhbz 493245)
   598231 - When Chromium rings the bell, metacity quits (rhbz 532282)
   598995 - Don't focus ancestor window on a different workspace (rhbz 237158)
   599097 - For mouse and sloppy focus, return to "mouse mode" on motion (rhbz 530261)
   599248 - Add no_focus_windows preference to list windows that shouldn't be focused (rhbz 530262)
   599261 - Add a new_windows_always_on_top preference (rhbz 530263)
   599262 - Add XFCE Terminal as a terminal
   604319 - Handle XError and XIOError for unknown displays (rhbz 537845)

* Thu Nov 26 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-11
- Fix a problem with the previous change

* Tue Nov 24 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-10
- Disable key repeat for screenshot keybinding (#506369)

* Thu Nov 05 2009 Ray Strode <rstrode@redhat.com> 2.28.0-9
- One stab at the metacity patch

* Thu Nov 05 2009 Ray Strode <rstrode@redhat.com> 2.28.0-8
- Minor clean ups to last patch based on feedback from
  Owen

* Thu Nov 05 2009 Ray Strode <rstrode@redhat.com> 2.28.0-7
- Don't do bad things on sigterm

* Wed Oct 28 2009 Matthias Clasen <mclasen@redhat.cm> - 2.28.0-6
- Make tooltips look sharper

* Wed Oct 21 2009 Matthias Clasen <mclasen@redhat.cm> - 2.28.0-4
- Make tooltips look match GTK+

* Thu Oct 15 2009 Matthias Clasen <mclasen@redhat.cm> - 2.28.0-3
- Tweak the default number of workspaces

* Tue Sep 22 2009 Matthias Clasen <mclasen@redhat.cm> - 2.28.0-1
- Update to 2.28.0

* Tue Sep  8 2009 Matthias Clasen <mclasen@redhat.cm> - 2.27.1-1
- Update to 2.27.1

* Wed Sep  2 2009 Peter Robinson <pbrobinson@gmail.com> - 2.27.0-9
- Add upstreamed patch for option to force fullscreen for sugar
- https://bugzilla.redhat.com/show_bug.cgi?id=516225

* Fri Aug 28 2009 Lennart Poettering <lpoetter@redhat.com> - 2.27.0-8
- Actually apply the patch from -7

* Fri Aug 28 2009 Lennart Poettering <lpoetter@redhat.com> - 2.27.0-7
- Apply another trivial patch related to sound events
- http://bugzilla.gnome.org/show_bug.cgi?id=593358

* Fri Aug 28 2009 Lennart Poettering <lpoetter@redhat.com> - 2.27.0-6
- Apply two trivial patches for bell/sound
- http://bugzilla.gnome.org/show_bug.cgi?id=593356
- http://bugzilla.gnome.org/show_bug.cgi?id=593355

* Sat Aug 22 2009 Owen Taylor <otaylor@redhat.com> - 2.27.0-5
- Add a fix for http://bugzilla.gnome.org/show_bug.cgi?id=588119,
  remove no-longer-needed no-lame-dialog patch

* Wed Aug  5 2009 Matthias Clasen  <mclasen@redhat.com> - 2.27.0-4
- Change the default theme to Clearlooks

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun  7 2009 Matthias Clasen  <mclasen@redhat.com> - 2.27.0-2
- Make DND work better
- Don't show a lame dialog

* Sun May 31 2009 Matthias Clasen  <mclasen@redhat.com> - 2.27.0-1
- Update to 2.27.0

* Mon Apr 27 2009 Matthias Clasen  <mclasen@redhat.com> - 2.26.0-2
- Don't drop schemas translations from po files

* Mon Mar 16 2009 Matthias Clasen  <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Wed Mar 11 2009 Matthias Clasen  <mclasen@redhat.com> - 2.25.144-6
- Fix interaction with autohide panels

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.144-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 21 2009 Matthias Clasen  <mclasen@redhat.com> - 2.25.144-4
- Don't force the bell (#486137)

* Wed Feb 18 2009 Matthias Clasen  <mclasen@redhat.com> - 2.25.144-3
- Update the theme patch to apply to the right file

* Tue Feb 10 2009 Matthias Clasen  <mclasen@redhat.com> - 2.25.144-2
- Use libcanberra to play the alert sound from the sound theme
  for the audible system bell

* Tue Feb  3 2009 Matthias Clasen  <mclasen@redhat.com> - 2.25.144-1
- Update to 2.25.144

* Mon Jan  5 2009 Matthias Clasen  <mclasen@redhat.com> - 2.25.89-1
- Update to 2.25.89

* Tue Dec 16 2008 Matthias Clasen  <mclasen@redhat.com> - 2.25.55-1
- Update to 2.25.55

* Mon Dec 15 2008 Matthias Clasen  <mclasen@redhat.com> - 2.25.34-3
- Clean _NET_SUPPORTING_WM_CHECK on shutdown
- Fix BuildRequires

* Wed Dec  3 2008 Matthias Clasen  <mclasen@redhat.com> - 2.25.34-1
- Update to 2.25.34

* Mon Nov 24 2008 Matthias Clasen  <mclasen@redhat.com> - 2.25.8-4
- Update to 2.25.8

* Sat Nov 22 2008 Matthias Clasen  <mclasen@redhat.com> - 2.25.5-4
- Tweak %%summary and %%description
- Fix BuildRequires

* Wed Nov 12 2008 Matthias Clasen  <mclasen@redhat.com> - 2.25.5-1
- Update to 2.25.5

* Fri Oct 31 2008 Soren Sandmann <sandmann@redhat.com> - 2.24.0-3
- Don't spam .xsession-errors so hard (bug 467802)

* Thu Sep 25 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-2
- Save some space

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Fri Sep 19 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.610-2
- Fix some memory leaks

* Tue Sep  9 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.610-1
- Update to 2.23.610

* Tue Sep  2 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.233-1
- Update to 2.23.233

* Fri Aug 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.144-1
- Update to 2.23.144

* Tue Jul 15 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.55-1
- Update to 2.23.55

* Tue Jun 17 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.34-1
- Update to 2.23.34

* Tue May 27 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.21-1
- Update to 2.23.21

* Mon May  5 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.13-1
- Update to 2.23.13

* Thu Apr 24 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.8-1
- Update to 2.23.8
- Drop obsolete patches

* Thu Apr 24 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-3
- Fix a possible crash in the appearance capplet with
  invalid metacity themes (launchpad #199402)

* Wed Mar 12 2008 Marco Pesenti Gritti <mpg@redhat.com> - 2.22.0-2
- Add patch to fix focus of keep-above windows
  http://bugzilla.gnome.org/show_bug.cgi?id=519188

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Wed Feb 27 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.21-1
- Update to 2.21.21

* Tue Feb 12 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.13-1
- Update to 2.21.13

* Wed Feb  6 2008 Colin Walters <walters@redhat.com> - 2.21.8.svn3554-1
- Drop random macros at top of file; spec files should be as amenable
  to static analysis as possible, easing our way into the bright future
  where our software build process isn't a horrible mismash of a
  preprocessor on shell script, with manual editing required, 
  but something scriptable.
- Update to SVN 3554, to which our patches were designed to apply
- Readd patch metacity-2.21.13-dont-move-windows.patch, which makes
  Firefox behave as those multiple-workspace users desire.

* Wed Feb  6 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.8-1
- Update to 2.21.8

* Sun Feb  3 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.5-3
- Make skip-taskbar windows appear in the ctrl-alt-tab list

* Thu Dec 20 2007 Colin Walters <walters@redhat.com> - 2.21.5-2
- Add patch for avoiding moving windows across workspaces
  This makes clicking on links in firefox do what you want.
  http://bugzilla.gnome.org/show_bug.cgi?id=482354

* Wed Dec 19 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.5-1
- Update to 2.21.5, including the new compositor

* Sun Dec 16 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.3-1
- Update to 2.21.3

* Sun Nov 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.2-1
- Update to 2.21.2

* Tue Nov 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.1-1
- Update to 2.21.1

* Sun Nov 11 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-4
- Fix a crash when the number of workspaces is 1

* Thu Oct 18 2007 Colin Walters <walters@redhat.com> - 2.20.0-3
- Add patch to fix workspace behavior when presenting normal windows

* Thu Sep 27 2007 Ray Strode <rstrode@redhat.com> - 2.20.0-2
- Drop dep on redhat-artwork, add one on nodoka

* Sun Sep 16 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Tue Sep 11 2007 Ray Strode <rstrode@redhat.com> - 2.19.55-4
- fix crash on logout (and on the subsequent login, bug 243761)

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 2.19.55-3
- Rebuild for build id

* Sun Aug 12 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.55-2
- Switch default theme to Nodoka

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.55-1
- Update to 2.19.55

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.34-3
- Update license field

* Wed Jul 25 2007 Jesse Keating <jkeating@redhat.com> - 2.19.34-2
- Rebuild for RH #249435

* Mon Jul 23 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.34-1
- Update to 2.19.34

* Fri Jul  6 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.21-3
- Require control-center-filesystem

* Thu Jul  5 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.21-2
- Fix keybindings

* Mon Jun 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.21-1
- Update to 2.19.21

* Sun Jun 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.13-2
- Clean up directory ownership

* Fri Jun 15 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.13-1
- Update to 2.19.13

* Mon Jun 11 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.8-2
- Don't ship .so.0 in the -devel package (#243689)

* Mon Jun  4 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.8-1
- Update to 2.19.8

* Sat May 19 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-1
- Update to 2.19.5

* Tue Apr  3 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-2
- Split off a devel package (#203547)
- Some spec file cleanups (#21573)

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Wed Feb 28 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.8-1
- Update to 2.17.8

* Thu Feb 22 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.5-2
- Fix a spec file typo
- Don't ship static libraries

* Wed Jan 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.5-1
- Update to 2.17.5

* Mon Nov  6 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.2-1
- Update to 2.17.2

* Fri Oct 20 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.1-1
- Update to 2.17.1

* Wed Oct 18 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-7
- Fix scripts according to packaging guidelines

* Tue Oct 17 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-6
- Add missing Requires (#203813)

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 2.16.0-5
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 25 2006 Soren Sandmann <sandmann@redhat.com> - 2.16.0-4.fc6
- Build

* Fri Sep 21 2006 Soren Sandmann <sandmann@redhat.com>
- Remove GL dependencies.
- Remove static-cm patch
- add patch to fix more CurrentTime race conditions (bug 206263)

* Thu Sep 14 2006 Ray Strode <rstrode@redhat.com> - 2.16.0-3.fc6
- remove stale ctrl-alt-delete patch

* Sat Sep  9 2006 Soren Sandmann <sandmann@redhat.com> - 2.16.0-2.fc6
- Add patch from Elijah that may fix bug 204519

* Mon Sep  4 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-1.fc6
- Update to 2.16.0

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.34-1.fc6
- Update to 2.15.34
- Require pkgconfig, since we installing a .pc file

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.21-1.fc6
- Update to 2.15.21
- Uninstall gconf schemas in %%preun

* Mon Aug 7 2006 Soren Sandmann <sandmann@redhat.com> - 2.15.13-2
- Remove leftover snapshot string.

* Mon Aug 7 2006 Soren Sandmann <sandmann@redhat.com> - 2.15.13-1
- Update to 2.15.13. Disable compositing manager.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.15.5-6.1
- rebuild

* Tue Jun 13 2006 Michael J. Knox <michael[AT]knox.net.nz> - 2.15.5-6
- remove BR on automake14, use current automake instead

* Tue Jun 6 2006 Soren Sandmann <sandmann@redhat.com> 2.15.5-5
- Update to new tarball with different intltool magic in it.

* Tue Jun 6 2006 Soren Sandmann <sandmann@redhat.com> 2.15.5-4
- Update intltool BuildRequires to 0.35

* Fri Jun 2 2006 Soren Sandmann <sandmann@redhat.com> 2.15.5-2
- Update intltool BuildRequires to 0.34.90

* Thu Jun 1 2006 Soren Sandmann <sandmann@redhat.com> 2.15.5-1
- Update metacity to a cvs snapshot, and libcm 0.0.22. (The standalone
  libcm package is being put through the package review process). 

* Tue May 30 2006 Kristian Høgsberg <krh@redhat.com> 2.15.3-4
- Bump for rawhide build.

* Mon May 29 2006 Kristian Høgsberg <krh@redhat.com> - 2.15.3-3
- Bump libGL build requires so libcm picks up the right tfp tokens.

* Thu May 18 2006 Soren Sandmann <sandmann@redhat.com> 2.15.3-2
- Update libcm to 0.0.21

* Wed May 17 2006 Matthias Clasen <mclasen@redhat.com> 2.15.3-1
- Update to 2.15.3

* Fri May 12 2006 Adam Jackson <ajackson@redhat.com> 2.15.2-2
- Update protocol dep to 7.0-13 for final EXT_tfp enums, and rebuild.

* Thu May 11 2006 Soren Sandmann <sandmann@redhat.com> 2.15.2-1
- Update to metacity 2.15.2

* Tue Apr 18 2006 Kristian Høgsberg <krh@redhat.com> 2.15.0-6
- Bump for fc5-bling build.

* Thu Apr 13 2006 Soren Sandmann <sandmann@redhat.com> 2.15.0-5
- Update to libcm 0.0.19

* Wed Apr 12 2006 Kristian Høgsberg <krh@redhat.com> 2.15.0-4
- Bump for fc5-bling rebuild.

* Thu Apr 6 2006 Soren Sandmann <sandmann@redhat.com> - 2.16.0-3
- Bump libcm to 0.0.18.

* Mon Apr  3 2006 Soren Sandmann <sandmann@redhat.com> - 2.15.0-2
- Fix leftover libcm-snapshot-date, buildrequire libXcomposite-devel >= 0.3

* Fri Mar 31 2006 Soren Sandmann <sandmann@redhat.com> - 2.15.0
- Update to 2.15.0

* Mon Mar 13 2006 Ray Strode <rstrode@redhat.com> - 2.14.0-1
- update to 2.14.0

* Mon Mar  6 2006 Ray Strode <rstrode@redhat.com> - 2.13.144-1
- update to 2.13.144
- add bling patch from HEAD

* Sun Feb 19 2006 Ray Strode <rstrode@redhat.com> - 2.13.89.0.2006.02.17-2
- disable compositor on s390 s390x and ppc64

* Fri Feb 17 2006 Ray Strode <rstrode@redhat.com> - 2.13.89.0.2006.02.17-1
- Update to latest cvs snapshot to give meaningful failure error
  messages
- Don't remove build root in install, because it triggers a
  rebuild of metacity

* Thu Feb 16 2006 Ray Strode <rstrode@redhat.com> - 2.13.89.0.2006.02.16-1
- Update to cvs snapshot to add the ability to 
  runtime enable compositor
- change %%makeinstall to make install DESTDIR=..

* Mon Feb 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.89-1
- Update to 2.13.89

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.13.55-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.13.55-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 30 2006 Matthias Clasen <mclasen@redhat.com> 2.13.55-1
- Update to 2.13.55

* Thu Jan 26 2006 Matthias Clasen <mclasen@redhat.com> 2.13.34-1
- Update to 2.13.34

* Mon Jan 16 2006 Ray Strode <rstrode@redhat.com> 2.13.21-1
- Update to 2.13.21

* Fri Jan 13 2006 Matthias Clasen <mclasen@redhat.com> 2.13.13-1
- Update to 2.13.13

* Tue Jan 03 2006 Matthias Clasen <mclasen@redhat.com> 2.13.8-1
- Update to 2.13.8

* Thu Dec 15 2005 Matthias Clasen <mclasen@redhat.com> 2.13.5-1
- Update to 2.13.5

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Dec  1 2005 Matthias Clasen <mclasen@redhat.com> 2.13.3-1
- Update to 2.13.3

* Mon Nov 21 2005 Ray Strode <rstrode@redhat.com> 2.13.2-1
- Update to 2.13.2

* Fri Nov 18 2005 Bill Nottingham <notting@redhat.com>
- remove references to obsolete X11R6 paths

* Thu Oct  6 2005 Matthias Clasen <mclasen@redhat.com> 2.12.1-1
- Update to 2.12.1

* Thu Sep  8 2005 Matthias Clasen <mclasen@redhat.com> 2.12.0-1
- Update to 2.12.0

* Thu Sep  1 2005 Ray Strode <rstrode@redhat.com> 2.11.2-3
- truncate long window titles to 512 characters (bug 164071)

* Tue Aug 16 2005 Warren Togami <wtogami@redhat.com> 2.11.2-2
- rebuild for new cairo

* Tue Aug  9 2005 Ray Strode <rstrode@redhat.com> 2.11.2-1
- Update to 2.11.2 (fixes bug 163745)

* Fri Aug  5 2005 Matthias Clasen <mclasen@redhat.com> 2.11.1-1
- New upstream version

* Mon Jul 18 2005 Matthias Clasen <mclasen@redhat.com> 2.11.0-3
- fix xcursor detection

* Wed Jul 13 2005 Matthias Clasen <mclasen@redhat.com> 2.11.0-1
- newer upstream version

* Mon May 30 2005 Warren Togami <wtogami@redhat.com> 2.10.0-2
- raise demands attention (#157271 newren)

* Sun Apr  3 2005 Ray Strode <rstrode@redhat.com> 2.10.0-1
- Update to 2.10.0

* Thu Mar 17 2005 Matthias Clasen <mclasen@redhat.com> 2.9.21-2
- Switch to Clearlooks as default theme

* Mon Feb 28 2005 Matthias Clasen <mclasen@redhat.com> 2.9.21-1
- Update to 2.9.21

* Wed Feb  9 2005 Matthias Clasen <mclasen@redhat.com> 2.9.13-1
- Update to 2.9.13

* Fri Jan 28 2005 Matthias Clasen <mclasen@redhat.com> 2.9.8-1
- Update to 2.9.8

* Sat Oct 16 2004 Havoc Pennington <hp@redhat.com> 2.8.6-2
- remove all the rerunning of autotools, intltool, etc. cruft; seemed to be breaking build

* Fri Oct 15 2004 Havoc Pennington <hp@redhat.com> 2.8.6-1
- upgrade to 2.8.6, fixes a lot of focus bugs primarily.

* Fri Oct 15 2004 Soren Sandmann <sandmann@redhat.com> - 2.8.5-3
- Kludge around right alt problem (#132379)

* Mon Oct 11 2004 Alexander Larsson <alexl@redhat.com> - 2.8.5-2
- Require startup-notification 0.7 (without this we'll crash)

* Thu Sep 23 2004 Alexander Larsson <alexl@redhat.com> - 2.8.5-1
- update to 2.8.5

* Tue Aug 31 2004 Alex Larsson <alexl@redhat.com> 2.8.4-1
- update to 2.8.4

* Tue Aug 24 2004 Warren Togami <wtogami@redhat.com> 2.8.3-1
- update to 2.8.3

* Thu Aug  5 2004 Mark McLoughlin <markmc@redhat.com> 2.8.2-1
- Update to 2.8.2
- Remove systemfont patch - upstream now

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May  6 2004 Havoc Pennington <hp@redhat.com> 2.8.1-2
- fix mangled Summary

* Thu May  6 2004 Havoc Pennington <hp@redhat.com> 2.8.1-1
- 2.8.1

* Thu Apr  1 2004 Alex Larsson <alexl@redhat.com> 2.8.0-1
- update to 2.8.0

* Wed Mar 10 2004 Mark McLoughlin <markmc@redhat.com> 2.7.1-1
- Update to 2.7.1

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 25 2004 Alexander Larsson <alexl@redhat.com> 2.7.0-1
- update to 2.7.0
- removed reduced resouces patch (its now upstream)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Oct 27 2003 Havoc Pennington <hp@redhat.com> 2.6.3-1
- 2.6.3

* Wed Oct  1 2003 Havoc Pennington <hp@redhat.com> 2.6.2-1
- 2.6.2

* Thu Sep  4 2003 Havoc Pennington <hp@redhat.com> 2.5.3-3
- put reduced resources patch back in

* Fri Aug 22 2003 Elliot Lee <sopwith@redhat.com> 2.5.3-2
- Work around libXrandr need for extra $LIBS

* Fri Aug 15 2003 Alexander Larsson <alexl@redhat.com> 2.5.3-1
- update for gnome 2.3

* Mon Jul 28 2003 Havoc Pennington <hp@redhat.com> 2.4.55-7
- rebuild

* Mon Jul 28 2003 Havoc Pennington <hp@redhat.com> 2.4.55-6
- backport the "reduced_resources" patch with wireframe

* Mon Jul 07 2003 Christopher Blizzard <blizzard@redhat.com> 2.4.55-4
- add patch to fix mouse down problems in mozilla

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 29 2003 Havoc Pennington <hp@redhat.com> 2.4.55-2
- rebuild

* Thu May 29 2003 Havoc Pennington <hp@redhat.com> 2.4.55-1
- 2.4.55

* Wed May 14 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add proper ldconfig calls for shared libs

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 21 2003 Havoc Pennington <hp@redhat.com> 2.4.34-2
- fix a crash in multihead situations, #84412

* Wed Feb  5 2003 Havoc Pennington <hp@redhat.com> 2.4.34-1
- 2.4.34
- try disabling smp_mflags and see if it fixes build

* Wed Jan 22 2003 Havoc Pennington <hp@redhat.com>
- 2.4.21.90 with a bunch o' fixes

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jan 16 2003 Havoc Pennington <hp@redhat.com>
- bind Ctrl+Alt+Del to logout, #72973

* Wed Jan 15 2003 Havoc Pennington <hp@redhat.com>
- 2.4.13.90 cvs snap with event queue lag fix

* Fri Jan 10 2003 Havoc Pennington <hp@redhat.com>
- 2.4.13

* Thu Dec 12 2002 Havoc Pennington <hp@redhat.com>
- 2.4.8

* Mon Dec  2 2002 Havoc Pennington <hp@redhat.com>
- 2.4.5.90
- add little script after configure that checks what config.h
  contains, to be sure we detected all the right features.

* Tue Oct 29 2002 Havoc Pennington <hp@redhat.com>
- 2.4.3
- remove patches that have gone upstream

* Tue Aug 27 2002 Havoc Pennington <hp@redhat.com>
- fix shaded window decorations in Bluecurve theme

* Sat Aug 24 2002 Havoc Pennington <hp@redhat.com>
- fix the mplayer-disappears-on-de-fullscreen bug

* Sat Aug 24 2002 Havoc Pennington <hp@redhat.com>
- add some fixes from CVS for #71163 #72379 #72478 #72513

* Thu Aug 22 2002 Havoc Pennington <hp@redhat.com>
- patch .schemas.in instead of .schemas so we get right default theme/fonts

* Tue Aug 20 2002 Havoc Pennington <hp@redhat.com>
- grow size of top resize, and display proper cursor on enter notify
- require latest intltool to try and fix metacity.schemas by
  regenerating it in non-UTF-8 locale

* Thu Aug 15 2002 Havoc Pennington <hp@redhat.com>
- default to Sans Bold font, fixes #70920 and matches graphic design spec

* Thu Aug 15 2002 Havoc Pennington <hp@redhat.com>
- 2.4.0.91 with raise/lower keybindings for msf, fixes to fullscreen
- more apps that probably intend to be, fix for changing number of
  workspaces, fix for moving windows in multihead

* Tue Aug 13 2002 Havoc Pennington <hp@redhat.com>
- update build requires

* Mon Aug 12 2002 Havoc Pennington <hp@redhat.com>
- upgrade to cvs snap 2.4.0.90 with pile of bugfixes from 
  this weekend
- change default theme to bluecurve and require new redhat-artwork

* Tue Aug  6 2002 Havoc Pennington <hp@redhat.com>
- 2.4.0
- themes are moved, require appropriate redhat-artwork

* Thu Aug  1 2002 Havoc Pennington <hp@redhat.com>
- munge the desktop file to be in toplevel menus and 
  not show in KDE

* Tue Jul 23 2002 Havoc Pennington <hp@redhat.com>
- don't use system font by default as metacity's 
  font is now in the system font dialog

* Tue Jul 23 2002 Havoc Pennington <hp@redhat.com>
- 2.3.987.92 cvs snap

* Fri Jul 12 2002 Havoc Pennington <hp@redhat.com>
- 2.3.987.91 cvs snap

* Mon Jun 24 2002 Havoc Pennington <hp@redhat.com>
- 2.3.987.90 cvs snap

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 16 2002 Havoc Pennington <hp@redhat.com>
- rebuild for new libraries

* Mon Jun 10 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Mon Jun 10 2002 Havoc Pennington <hp@redhat.com>
- 2.3.987
- default to redhat theme

* Fri Jun 07 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Tue Jun  4 2002 Havoc Pennington <hp@redhat.com>
- 2.3.610.90 cvs snap

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May 20 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Fri May 17 2002 Havoc Pennington <hp@redhat.com>
- 2.3.377

* Thu May  2 2002 Havoc Pennington <hp@redhat.com>
- 2.3.233

* Thu Apr 25 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment
- add gconf schemas boilerplate

* Mon Apr 15 2002 Havoc Pennington <hp@pobox.com>
- 2.3.89

* Tue Oct 30 2001 Havoc Pennington <hp@redhat.com>
- 2.3.34

* Fri Oct 13 2001 Havoc Pennington <hp@redhat.com>
- 2.3.21 

* Mon Sep 17 2001 Havoc Pennington <hp@redhat.com>
- 2.3.8
- 2.3.13

* Wed Sep  5 2001 Havoc Pennington <hp@redhat.com>
- Initial build.


