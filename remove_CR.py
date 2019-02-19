def dos_to_unix(fname):
	with open(fname,'rb+') as fobj:
		data = fobj.read()
		data = data.replace('\r\n', '\n')
		fobj.seek(0, 0)
		fobj.truncate()
		fobj.write(data)

filename = "E:/qinxiedaoduan/ceshi2/xml/00001.xml"

dos_to_unix(filename)