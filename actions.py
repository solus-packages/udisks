#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure("--disable-static \
                         --enable-introspection \
                         --with-udevdir=/lib/udev")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR() )

    pisitools.dodoc("AUTHORS", "COPYING")
