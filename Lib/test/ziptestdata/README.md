# Test data for `test_zipfile`

In this directory you can find test executables, that were created manually
from header.sh and the `testdata_module_inside_zip.py` file.

You can also find here a script `gen_perm_files.py` to generate test files
with various permission combinations.

You must have infozip's zip utility installed (`apt install zip` on Debian).

## Purpose

These are used to test executable files with an appended zipfile, in a scenario
where the executable is _not_ a Python interpreter itself so our automatic
zipimport machinery (that'd look for `__main__.py`) is not being used.

## Updating the test executables

If you update header.sh or the testdata_module_inside_zip.py file, rerun the
commands below.  These are expected to be rarely changed, if ever.


### Standard old format (2.0) zip file

```
zip -0 zip2.zip testdata_module_inside_zip.py
cat header.sh zip2.zip >exe_with_zip
rm zip2.zip
```

### Modern format (4.5) zip64 file

Redirecting from stdin forces infozip's zip tool to create a zip64.

```
zip -0 <testdata_module_inside_zip.py >zip64.zip
cat header.sh zip64.zip >exe_with_z64
rm zip64.zip
```

## Regeneration of ../permissions.zip file

If you would like to regenerate zipfile `../zip_permissions.zip` rerun commands
bellow.  Sudo is needed to read files without read permission.  Date changes
are just for cosmetic purposes.

```
mkdir zip_permissions
pushd zip_permissions > /dev/null
python ../gen_perm_files.py

now=$(date)
sudo date "+%F %T" --utc --set="2020-05-05 20:20:00"
touch file_permission_*
sudo date --set="$now"

sudo zip -qr ../../zip_permissions.zip .
sudo chown "$USER:$USER" ../../zip_permissions.zip
chmod 0644 ../../zip_permissions.zip
rm -f file_permission_*
popd > /dev/null
rmdir zip_permissions
```
