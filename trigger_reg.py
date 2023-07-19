import tkinter as tk

def calculate_result():
    # 从输入框中获取每个位的值
    bit_values = []
    for entry, bit_range in zip(bit_entries, bit_ranges):
        start_bit = bit_range[0]
        end_bit = bit_range[1]
        value = int(entry.get(), 2)
        bit_values.extend([(value >> (end_bit - i)) & 1 for i in range(end_bit, start_bit - 1, -1)])
    
    # 将位值按照第2列的bit位组合成一个整数
    result = sum(bit_values[i] << (15 - i) for i in range(len(bit_values)))
    
    # 显示结果
    result_label.config(text="结果: 0x{:04X}".format(result))

    # 将输入和计算结果写入日志文件
    with open('log.txt', 'a') as log_file:
        log_file.write("输入: {}\n".format(' '.join([entry.get() for entry in bit_entries])))
        log_file.write("结果: 0x{:04X}\n".format(result))

def reset_bits():
    # 将输入框中的位值重置为0
    for entry in bit_entries:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "0")

# 创建窗口
window = tk.Tk()
window.title("位值计算器")

# 创建位值输入框、标签和位范围
bit_entries = []
bit_labels = []
bit_ranges = [
    (15, 15),  # [15]
    (14, 12),  # [14:12]
    (11, 10),  # [11:10]
    (9, 9),    # [9]
    (8, 8),    # [8]
    (7, 6),    # [7:6]
    (5, 5),    # [5]
    (4, 4),    # [4]
    (3, 3),    # [3]
    (2, 0)     # [2:0]
]

for i, bit_range in enumerate(bit_ranges):
    start_bit = bit_range[0]
    end_bit = bit_range[1]
    bit_label = tk.Label(window, text="[{}:{}]".format(start_bit, end_bit))
    bit_label.grid(row=i, column=0)
    bit_labels.append(bit_label)
    
    bit_entry = tk.Entry(window, width=5)
    bit_entry.insert(tk.END, "0")
    bit_entry.grid(row=i, column=1)
    bit_entries.append(bit_entry)

# 创建计算按钮
calculate_button = tk.Button(window, text="计算", command=calculate_result)
calculate_button.grid(row=len(bit_ranges), column=0, columnspan=2)

# 创建结果标签
result_label = tk.Label(window, text="结果: ")
result_label.grid(row=len(bit_ranges) + 1, column=0, columnspan=2)

# 创建重置按钮
reset_button = tk.Button(window, text="重置", command=reset_bits)
reset_button.grid(row=len(bit_ranges) + 2, column=0, columnspan=2)

# 运行窗口主循环
window.mainloop()
