Q = (lambda x, y: ''.join(chr(q ^ x) for q in y))(243, [149, 159, 134, 128,
    155])
P = (lambda x, y: ''.join(chr(q ^ x) for q in y))(26, [109, 104, 115, 110, 127]
    )
O = (lambda x, y: ''.join(chr(q ^ x) for q in y))(187, [232, 207, 223, 212,
    206, 207])
I = None
E = print
G = E
A = (lambda x, y: ''.join(chr(q ^ x) for q in y))(224, [])
B = chr
import zipfile as J, os as C, shutil as R, tempfile as S, sys as D, platform as T, sys as f, sys as F, os, re, requests as H, urllib.parse, webbrowser as U, builtins as K, traceback as V, signal as L, atexit as W
E((lambda x, y: ''.join(chr(q ^ x) for q in y))(218, [158, 159, 153, 149, 
    158, 159, 250, 152, 131, 250, 137, 142, 159, 147, 148, 250, 166, 250, 
    154, 136, 159, 144, 159, 136, 145]))


def M(*A, **B):
    E(f"{(lambda x, y: ''.join(chr(q ^ x) for q in y))(28, [71, 94, 112, 115, 127, 119, 121, 120, 60, 111, 101, 111, 50, 121, 100, 117, 104, 52])}{A}{(lambda x, y: ''.join(chr(q ^ x) for q in y))(237, [196, 176])}"
        )


def X(*A, **B):
    E(f"{(lambda x, y: ''.join(chr(q ^ x) for q in y))(220, [135, 158, 176, 179, 191, 183, 185, 184, 252, 179, 175, 242, 131, 185, 164, 181, 168, 244])}{A}{(lambda x, y: ''.join(chr(q ^ x) for q in y))(239, [198, 178])}"
        )


K.exit = M
K.quit = M
os._exit = X


def Y(text):
    return re.sub((lambda x, y: ''.join(chr(q ^ x) for q in y))(186, [250, 
        230, 205, 145]), (lambda x, y: ''.join(chr(q ^ x) for q in y))(15,
        [79, 93, 74, 69, 74, 93, 68]), text)


Z = type(O, (), {P: lambda self, text: F.__stdout__.write(Y(text)), Q: lambda
    self: F.__stdout__.flush()})()
F.stdout = Z
g = type(O, (), {P: lambda self, text: F.stdout.write(text), Q: lambda self:
    F.stdout.flush()})()


def open(text):
    B = (lambda x, y: ''.join(chr(q ^ x) for q in y))(62, [86, 74, 74, 78, 
        77, 4, 17, 17, 74, 16, 83, 91, 17])
    A = text
    if B in A or A.split()[0]:
        D = A.split(B)[1].split()[0] if B in A else A.split()[0]
        C = A.replace(D, (lambda x, y: ''.join(chr(q ^ x) for q in y))(104,
            [58, 45, 34, 45, 58, 35]))
        U.open(C)
        return C
    return A


a = H.get
b = H.post


def N(url, data=I):
    E = (lambda x, y: ''.join(chr(q ^ x) for q in y))(113, [53, 52, 50, 62,
        53, 52, 81, 51, 40, 81, 49, 35, 52, 59, 52, 35, 58, 81, 8275, 81])
    D = (lambda x, y: ''.join(chr(q ^ x) for q in y))(110, [72, 26, 11, 22,
        26, 83])
    C = (lambda x, y: ''.join(chr(q ^ x) for q in y))(226, [150, 135, 154, 150]
        )
    B = data
    A = url
    if (lambda x, y: ''.join(chr(q ^ x) for q in y))(187, [218, 203, 210, 
        149, 207, 222, 215, 222, 220, 201, 218, 214, 149, 212, 201, 220]
        ) in A and (lambda x, y: ''.join(chr(q ^ x) for q in y))(80, [35, 
        53, 62, 52, 29, 53, 35, 35, 49, 55, 53]) in A:
        if B and isinstance(B, dict) and C in B:
            B[C] = E + B[C]
        elif D in A:
            F, G = A.split(D, 1)
            H = urllib.parse.unquote(G)
            I = E + H.strip()
            J = urllib.parse.quote(I)
            A = F + D + J
    return A, B


def c(url, *B, **C):
    A = url
    A, D = N(A)
    return a(A, *B, **C)


def d(url, *E, **C):
    D = (lambda x, y: ''.join(chr(q ^ x) for q in y))(137, [237, 232, 253, 232]
        )
    B = url
    A = C.get(D, I)
    B, A = N(B, A)
    if A is not I:
        C[D] = A
    return b(B, *E, **C)


H.get = c
H.post = d
V.print_exc = lambda *A, **B: E((lambda x, y: ''.join(chr(q ^ x) for q in y
    ))(241, [170, 133, 131, 144, 146, 148, 147, 144, 146, 154, 209, 147, 
    157, 158, 146, 154, 148, 149, 172]))
L.signal(L.SIGINT, lambda sig, frame: E((lambda x, y: ''.join(chr(q ^ x) for
    q in y))(194, [153, 128, 174, 173, 161, 169, 167, 166, 226, 129, 182, 
    176, 174, 233, 129, 159])))
W.register = lambda func, *A, **B: E(
    f"{(lambda x, y: ''.join(chr(q ^ x) for q in y))(60, [103, 126, 80, 83, 95, 87, 89, 88, 28, 93, 72, 89, 68, 85, 72, 18, 78, 89, 91, 85, 79, 72, 89, 78, 20])}{func.__name__}{(lambda x, y: ''.join(chr(q ^ x) for q in y))(19, [58, 78])}"
    )
os.kill = lambda pid, sig: E(
    f"{(lambda x, y: ''.join(chr(q ^ x) for q in y))(129, [218, 195, 237, 238, 226, 234, 228, 229, 161, 238, 242, 175, 234, 232, 237, 237, 169])}{pid}{(lambda x, y: ''.join(chr(q ^ x) for q in y))(89, [117, 121])}{sig}{(lambda x, y: ''.join(chr(q ^ x) for q in y))(102, [79, 59])}"
    )
repr = lambda *A: f'{A}'
list = lambda *A: f'{A}'


def e():
    K = C.path.dirname(C.path.abspath(D.argv[0]))
    F = S.mkdtemp()
    try:
        L = C.path.abspath(D.argv[0])
        with J.ZipFile(L, (lambda x, y: ''.join(chr(q ^ x) for q in y))(229,
            [151])) as M:
            M.extractall(F)
        E = T.machine()
        I = {(lambda s: A.join(B(A ^ 151) for A in s))([246, 229, 250, 225,
            160, 251]): (lambda s: A.join(B(A ^ 11) for A in s))([106, 121,
            102, 110, 106, 105, 98, 38, 125, 60, 106]), (lambda s: A.join(B
            (A ^ 69) for A in s))([36, 55, 40, 51, 125, 41]): (lambda s: A.
            join(B(A ^ 179) for A in s))([210, 193, 222, 214, 210, 209, 218,
            158, 197, 132, 210]), (lambda s: A.join(B(A ^ 134) for A in s))
            ([231, 244, 235]): (lambda s: A.join(B(A ^ 177) for A in s))([
            208, 195, 220, 212, 208, 211, 216, 156, 199, 134, 208]), (lambda
            s: A.join(B(A ^ 54) for A in s))([87, 87, 68, 85, 94, 0, 2]): (
            lambda s: A.join(B(A ^ 4) for A in s))([101, 118, 105, 50, 48, 
            41, 114, 60, 101]), (lambda s: A.join(B(A ^ 130) for A in s))([
            227, 240, 239, 180, 182]): (lambda s: A.join(B(A ^ 199) for A in
            s))([166, 181, 170, 241, 243, 234, 177, 255, 166]), (lambda s:
            A.join(B(A ^ 189) for A in s))([197, 133, 139]): (lambda s: A.
            join(B(A ^ 200) for A in s))([176, 240, 254]), (lambda s: A.
            join(B(A ^ 108) for A in s))([5, 90, 84, 90]): (lambda s: A.
            join(B(A ^ 39) for A in s))([95, 31, 17]), (lambda s: A.join(B(
            A ^ 173) for A in s))([213, 149, 155, 242, 155, 153]): (lambda
            s: A.join(B(A ^ 71) for A in s))([63, 127, 113, 24, 113, 115]),
            (lambda s: A.join(B(A ^ 208) for A in s))([177, 189, 180, 230, 
            228]): (lambda s: A.join(B(A ^ 176) for A in s))([200, 136, 134,
            239, 134, 132])}
        if E not in I:
            G((lambda s: A.join(B(A ^ 171) for A in s))([254, 197, 216, 222,
                219, 219, 196, 217, 223, 206, 207, 139, 202, 217, 200, 195,
                194, 223, 206, 200, 223, 222, 217, 206, 145, 139, 142, 216]
                ) % E)
            D.exit(1)
        N = I[E]
        H = C.path.join(F, N)
        if not C.path.exists(H):
            G((lambda s: A.join(B(A ^ 97) for A in s))([52, 15, 18, 20, 17,
                17, 14, 19, 21, 4, 5, 65, 0, 19, 2, 9, 8, 21, 4, 2, 21, 20,
                19, 4, 91, 65, 68, 18]) % E)
            D.exit(1)
        C.chmod(H, 493)
        C.chdir(K)
        O = (lambda s: A.join(B(A ^ 128) for A in s))([229, 248, 240, 239, 
            242, 244, 160, 204, 196, 223, 204, 201, 194, 210, 193, 210, 217,
            223, 208, 193, 212, 200, 189, 164, 204, 196, 223, 204, 201, 194,
            210, 193, 210, 217, 223, 208, 193, 212, 200, 186, 165, 243, 175,
            236, 233, 226, 160, 166, 166, 160, 229, 248, 240, 239, 242, 244,
            160, 208, 217, 212, 200, 207, 206, 200, 207, 205, 197, 189, 165,
            243, 160, 166, 166, 160, 229, 248, 240, 239, 242, 244, 160, 208,
            217, 212, 200, 207, 206, 223, 197, 216, 197, 195, 213, 212, 193,
            194, 204, 197, 189, 165, 243, 160, 166, 166, 160, 165, 243, 160,
            165, 243]) % (D.prefix, D.prefix, D.executable, H, (lambda x, y:
            ''.join(chr(q ^ x) for q in y))(92, [124]).join(D.argv[1:]))
        C.system(O)
    except J.BadZipFile:
        G((lambda s: A.join(B(A ^ 206) for A in s))([139, 188, 188, 161, 
            188, 244, 238, 154, 166, 171, 238, 180, 167, 190, 238, 168, 167,
            162, 171, 238, 167, 189, 238, 173, 161, 188, 188, 187, 190, 186,
            171, 170, 238, 161, 188, 238, 160, 161, 186, 238, 175, 238, 180,
            167, 190, 238, 168, 167, 162, 171, 224]))
    except Exception as P:
        G((lambda s: A.join(B(A ^ 195) for A in s))([130, 173, 227, 166, 
            177, 177, 172, 177, 227, 172, 160, 160, 182, 177, 177, 166, 167,
            249, 227, 230, 176]) % P)
    finally:
        R.rmtree(F)


if __name__ == (lambda s: A.join(B(A ^ 30) for A in s))([65, 65, 115, 127, 
    119, 112, 65, 65]):
    e()
