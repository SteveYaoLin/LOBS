import tkinter as tk

def calculate_result():
    # 打开日志文件
    log_file = open('log.txt', 'w')

    # 计算每一行的结果，并记录到日志文件
    row_results = []
    for i, (reg_name, bit_range, entry) in enumerate(zip(reg_names, bit_ranges, bit_entries)):
        start_bit = bit_range[0]
        end_bit = bit_range[1]
        value = int(entry.get())
        row_result = value << (end_bit)
        row_results.append(row_result)
        log_file.write("输入值: bit{} = {}\n".format(start_bit, value))
        log_file.write("第{}行结果: {}\n".format(i+1, hex(row_result)))

    # 计算总体结果
    result = sum(row_results)
    log_file.write("总体结果: {}\n".format(hex(result)))

    # 关闭日志文件
    log_file.close()

    # 显示结果
    result_label.config(text="结果: {}".format(hex(result)))

def reset_bits():
    # 将输入框中的位值重置为0
    for entry in bit_entries:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "0")

# 创建窗口
window = tk.Tk()
window.title("位值计算器")

# 创建位值输入框、标签、位范围和寄存器名称
bit_entries = []
bit_labels = []
reg_names = [
    "ALTCOMPSEL 0: COMP ; 1:counter",
    "ALTCOMP",
    "CAPTID",
    "COUNTBRK",
    "COUNTCLR",
    "TRACE 11:ELACLK; 00: COMP; 01:counter",
    "COUNTSRC 0:ELACLK; 1:COMP match",
    "WATCHRST",
    "COMPSEL 0:COMP; 1:counter",
    "COMP"
]
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

for i, (reg_name, bit_range) in enumerate(zip(reg_names, bit_ranges)):
    start_bit = bit_range[0]
    end_bit = bit_range[1]
    bit_label = tk.Label(window, text="[{}:{}]".format(start_bit, end_bit))
    bit_label.grid(row=i, column=1)
    bit_labels.append(bit_label)
    
    reg_name_label = tk.Label(window, text=reg_name)
    reg_name_label.grid(row=i, column=0)

    bit_entry = tk.Entry(window, width=5)
    bit_entry.insert(tk.END, "0")
    bit_entry.grid(row=i, column=2)
    bit_entries.append(bit_entry)

# 创建计算按钮
calculate_button = tk.Button(window, text="计算", command=calculate_result)
calculate_button.grid(row=len(bit_ranges), column=0, columnspan=3)

# 创建结果标签
result_label = tk.Label(window, text="结果: ")
result_label.grid(row=len(bit_ranges) + 1, column=0, columnspan=3)

# 创建重置按钮
reset_button = tk.Button(window, text="重置", command=reset_bits)
reset_button.grid(row=len(bit_ranges) + 2, column=0, columnspan=3)

# 运行窗口主循环
window.mainloop()
