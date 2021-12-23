import zipfile
new=zipfile.ZipFile('newZip.zip','w')
new.write('2.py',compress_type=zipfile.ZIP_DEFLATED)
new.extractall('zips')
new.close()