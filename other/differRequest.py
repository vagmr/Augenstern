import pkg_resources
from colorama import init, Fore
from tkinter import Tk, filedialog

init()  # 初始化 colorama 库

# 提示用户选择 requirements.txt 文件
root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title="选择 requirements.txt 文件")

# 读取 requirements.txt 文件，获取依赖库信息
with open(file_path, 'r') as file:
    requirements = [line.strip() for line in file]

# 获取本机已安装的库信息
installed_packages = [pkg.key for pkg in pkg_resources.working_set]

# 创建两个列表，用于存储不同的库和版本
missing_packages = []
version_mismatch = []

# 检查每个依赖库
for requirement in requirements:
    try:
        pkg_resources.get_distribution(requirement)
    except pkg_resources.DistributionNotFound:
        missing_packages.append(requirement)
        continue

    installed_version = pkg_resources.get_distribution(requirement).version
    required_version = pkg_resources.Requirement.parse(requirement).specifier

    if required_version == '*':
        continue

    if required_version != installed_version:
        version_mismatch.append((requirement, installed_version))

# 打印结果
print("已安装的库:")
for package in installed_packages:
    print(Fore.GREEN + package)

print("\nrequirements.txt 中引入的库:")
for package in requirements:
    if package in installed_packages:
        print(Fore.GREEN + package)
    else:
        print(Fore.RED + package)

print("\n未安装的库:")
for package in missing_packages:
    print(Fore.RED + package)

print("\n版本不匹配的库:")
for package, version in version_mismatch:
    print(Fore.RED + package + ' (已安装版本: ' + version + ')')
