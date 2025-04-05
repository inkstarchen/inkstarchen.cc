import numpy as np
import matplotlib.pyplot as plt

# 生成一个示例时域信号
N = 1000  # 信号长度
T = 1.0 / 800.0  # 采样间隔
t = np.linspace(0.0, N*T, N, endpoint=False)

# 生成一个包含多个频率成分的信号
time_signal = (0.5 * np.sin(50.0 * 2.0 * np.pi * t) + \
              0.8 * np.sin(80.0 * 2.0 * np.pi * t) + \
              0.3 * np.sin(120.0 * 2.0 * np.pi * t))

# 对时域信号进行傅里叶变换，得到频域信号
freq_signal = np.fft.fft(time_signal)

# 获取频率轴
freqs = np.fft.fftfreq(N, d=T)

# 定义要保留的频率范围（例如，只保留 40Hz 到 90Hz 之间的频率）
f_low = 20  # 最低频率
f_high = 60  # 最高频率

# 创建一个掩码，只保留指定频率范围内的信号
mask = np.logical_and(np.abs(freqs) >= f_low, np.abs(freqs) <= f_high)

# 对频域信号进行滤波
filtered_freq_signal = freq_signal * mask

# 对滤波后的频域信号进行逆傅里叶变换，得到时域信号
filtered_time_signal = np.fft.ifft(filtered_freq_signal)

# 取实部（由于数值误差，逆傅里叶变换的结果可能包含非常小的虚部）
filtered_time_signal = np.real(filtered_time_signal)



# 绘制原始时域信号
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, time_signal)
plt.title('original_time_signal')
plt.xlabel('Time [s]')
plt.ylabel('amplitude')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(freqs, np.abs(filtered_freq_signal))
plt.title(f'过滤后的频域信号（{f_low}Hz - {f_high}Hz）')
plt.xlabel('频率 [Hz]')
plt.ylabel('幅度')
plt.xlim(-150, 150)  # 限制频率范围以便观察
plt.grid()

plt.tight_layout()
plt.show()

# 绘制滤波后的时域信号
plt.subplot(2, 1, 2)
plt.plot(t, filtered_time_signal)
plt.title(f'filtered_signal（{f_low}Hz - {f_high}Hz）')
plt.xlabel('Time[s]')
plt.ylabel('amplitude')
plt.grid()

plt.tight_layout()
plt.show()