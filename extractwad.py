import sys, os, os.path
import pywii.Common.pywii as wii

def extractwad(wad, outdir):

    wii.loadkeys("../keys")

    wad = wii.WiiWad(wad)

    if not os.path.isdir(outdir):
        os.mkdir(outdir)

    for ct in wad.tmd.get_content_records():
        data = wad.getcontent(ct.index)
        f = open(os.path.join(outdir, "%08X" % ct.cid),"wb")
        f.write(data)
        f.close()

    f = open(os.path.join(outdir, "cetk"),"wb")
    f.write(wad.tik.data)
    f.close()

    f = open(os.path.join(outdir, "tmd"),"wb")
    f.write(wad.tmd.data)
    f.close()

    f = open(os.path.join(outdir, "certs"),"wb")
    for cert in wad.certlist:
        f.write(cert.data)
        wii.falign(f,0x40)
    f.close()

    f = open(os.path.join(outdir, "footer"),"wb")
    f.write(wad.footer)
    f.close()
