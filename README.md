Task
----
1. Create an HPCCM recipe targeting Docker that builds and installs Python from
source and use the v3.6.5 release. Use ubuntu:16.04 as base image. Check with:
```bash
docker run mypythoncontainer:latest python3 --version
```
If all goes well, this should output:
```bash
Python 3.6.5
```

2. Get deb-package from attachments, try to install, find an issue and create
fixed deb-package.

Solution
--------
- Install HPCCM
```bash
pip install hpccm
```
- Convert hpccmrecipe to Dockerfile:
```bash
hpccm --recipe recipe.py --format docker > Dockerfile
```
- Build an image from Dockerfile:
```bash
docker build -t test_hpccm -f Dockerfile .
```
- Run bash in container:
```bash
docker run --rm -it --entrypoint bash test_hpccm:latest
```
- Copy .deb package into container
```bash
docker cp ./test1.deb CONTAINER_ID:/test1.deb
```
- Info of .deb package:
```bash
dpkg-deb --info test1.deb
```
- Unarchive .deb package into folder:
```bash
dpkg-deb -R test1.deb nv-test-script/
```
- Change control file (remove dependency):
```bash
sed -i '/python2/d' nv-test-script/DEBIAN/control
```
- Create .deb package from folder:
```bash
dpkg-deb -b nv-test-script nv-test-script.deb
```
- Install dpkg package:
```bash
dpkg -i nv-test-script.deb
```
Optional
--------
1. If it is needed, we can include shebang to specify a path to interpreter, then call it with script.py
2. If we do not want to use .py ext, the just remove it in deb pckage (nv-test-script/usr/local/bin/nv-test-script.py)
