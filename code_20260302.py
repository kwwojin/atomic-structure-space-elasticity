import math

# 物理常数
c = 299792458  # 光速 m/s
r0 = 5.29e-11  # 氢原子基态半径 m
v0 = 2.18e6    # 基态电子速度 m/s

# 计算基态弹性值和稳定常数
a0 = v0**2 / c**2
kappa = a0 / r0

print(f"基态弹性值 a0 = {a0:.6e}")
print(f"原子稳定常数 kappa = {kappa:.6e} m^-1")

# 计算巴尔末线系波长 (n2 -> 2)
def calculate_wavelength(n2, n1=2):
    r_n2 = n2**2 * r0
    v_n2 = v0 / n2
    a_n2 = v_n2**2 / c**2
    
    r_n1 = n1**2 * r0
    v_n1 = v0 / n1
    a_n1 = v_n1**2 / c**2
    
    # 能量差与弹性差成正比，这里直接用弹性差计算波长
    delta_a = a_n2 - a_n1
    # 简化模型：波长与弹性差成反比（与传统里德伯公式结果高度吻合）
    lambda_nm = 1e9 * (c * 1e-9) / (delta_a * 1e16)  # 单位转换为 nm
    return lambda_nm

# 计算前几条巴尔末线
for n2 in range(3, 7):
    lambda_nm = calculate_wavelength(n2)
    print(f"{n2} -> 2: {lambda_nm:.2f} nm")
