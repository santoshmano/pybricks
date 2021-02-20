

def nueronyms(txt):
	"""
	r - replace
	s - start
	e - end
	"""
	for r in range(len(txt)-2, 1, -1):
		s = 1
		e = s + r
		while e < len(txt):
			print(txt[0:s]+str(r)+txt[e:len(txt)])
			e = e+1
			s = s+1

nueronyms("nailed")
nueronyms("xa")
nueronyms("xav")
nueronyms("xavie")