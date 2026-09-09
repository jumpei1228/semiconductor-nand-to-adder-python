"""
NANDゲートから全加算器を作る｜Pythonで論理回路を組み立てる

元記事: https://semiconductor.yurufuwa.work/learn/nand-to-adder-python
ゆるふわ半導体 (semiconductor.yurufuwa.work) の解説記事から抜粋したコードです。
"""

def NAND(a, b):
    return 0 if (a and b) else 1

def NOT(a):
    return NAND(a, a)

def AND(a, b):
    return NOT(NAND(a, b))

def OR(a, b):
    return NAND(NOT(a), NOT(b))   # ド・モルガンの法則

def XOR(a, b):
    c = NAND(a, b)
    return NAND(NAND(a, c), NAND(b, c))

for a in (0, 1):
    for b in (0, 1):
        print(a, b, "| AND", AND(a, b), " OR", OR(a, b), " XOR", XOR(a, b))

def half_adder(a, b):
    s = XOR(a, b)     # 和（繰り上がりを除いた桁）
    c = AND(a, b)     # 繰り上がり
    return s, c

print(half_adder(1, 1))   # (0, 1) = 「0、繰り上がり1」

def full_adder(a, b, cin):
    s1, c1 = half_adder(a, b)
    s2, c2 = half_adder(s1, cin)
    return s2, OR(c1, c2)     # 和, 繰り上がり

# 全パターンを検証
for a in (0, 1):
    for b in (0, 1):
        for cin in (0, 1):
            s, cout = full_adder(a, b, cin)
            assert (cout * 2 + s) == (a + b + cin)   # 2進の足し算と一致
print("全加算器: 全8パターンOK ✅")
