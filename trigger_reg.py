import tkinter as tk

def calculate_result():
    # 从输入框中获取每个位的值
    bit_values = [int(entry.get()) for entry in bit_entries]
    
    # 将位值按照第2列的bit位组合成一个整数
    result = sum(bit_values[i] << (15 - i) for i in range(len(bit_values)))
    
    # 显示结果
    result_label.config(text="结果: 0x{:04X}".format(result))

def reset_bits():
    # 将输入框中的位值重置为0
    for entry in bit_entries:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "0")

# 创建窗口
window = tk.Tk()
window.title("位值计算器")

# 创建位值输入框和标签
bit_entries = []
bit_labels = []
for i in range(16):
    bit_label = tk.Label(window, text="[{}]".format(15 - i))
    bit_label.grid(row=i, column=0)
    bit_labels.append(bit_label)
    
    bit_entry = tk.Entry(window, width=5)
    bit_entry.insert(tk.END, "0")
    bit_entry.grid(row=i, column=1)
    bit_entries.append(bit_entry)

# 创建计算按钮
calculate_button = tk.Button(window, text="计算", command=calculate_result)
calculate_button.grid(row=16, column=0, columnspan=2)

# 创建结果标签
result_label = tk.Label(window, text="结果: ")
result_label.grid(row=17, column=0, columnspan=2)

# 创建重置按钮
reset_button = tk.Button(window, text="重置", command=reset_bits)
reset_button.grid(row=18, column=0, columnspan=2)

# 运行窗口主循环
window.mainloop()
