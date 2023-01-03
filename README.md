# mytest

This is a test repository to play about with Conan 2.

Install conan2 with

```python
pip install conan --pre
```

My conan2 default profile is

```
[settings]
arch=x86_64
build_type=Release
compiler=msvc
compiler.cppstd=17
compiler.runtime=dynamic
compiler.runtime_type=Release
compiler.version=193
os=Windows
```

To (re)configure the code: From the cpp folder

```
conan install --build=missing -o "*:shared=True"
conan create --build=missing -o "*:shared=True"
```
