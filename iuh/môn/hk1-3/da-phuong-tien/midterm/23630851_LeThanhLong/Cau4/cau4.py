import platform
import psutil
import subprocess
import os


with open("os-infor.txt", "w", encoding="utf-8") as f:
    f.write("Báo cáo hệ thống \n")
    f.write("="*30 + "\n\n")

    
    print("--- Thông tin hệ thống ---")
    f.write("--- Thông tin hệ thống ---\n")

    os_name = f"Hệ điều hành: {platform.system()} {platform.release()}"
    cpu_cores = f"Số lõi CPU: {psutil.cpu_count(logical=True)}"
    total_ram = f"Dung lượng RAM: {psutil.virtual_memory().total / (1024**3):.2f} GB"

    print(os_name)
    print(cpu_cores)
    print(total_ram)
    
    f.write(os_name + "\n")
    f.write(cpu_cores + "\n")
    f.write(total_ram + "\n\n")

   

print("\nĐã ghi báo cáo vào file 'os-infor.txt'")