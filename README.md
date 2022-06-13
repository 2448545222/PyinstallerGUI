# 软件界面预览
![Y 2W}Z)MEGX$Y4G4BYJ8KSG](https://user-images.githubusercontent.com/93512218/173412073-e25db429-3df9-4800-92c2-b7f236525443.png)

# 使用须知
要打包的py文件, 以下简称为 "main.py"
 1. **要打包的py文件路径尽量不要有中文; 如果报错请尝试更换main.oy路径为全英文!!!**
 2. **main.py 和 pyinstaller 路径为必填项!!!**
 3. 软件会在 main.py 所在目录下自动寻找 pyinstaller.exe 的路径, 所以建议使用pycharm创建虚拟环境, 在进行打包
 4. 如果 点击开始打包后没反应, 请尝试在虚拟环境终端输入 pyisntaller main.py 查看报错日志
# 环境要求
pycharm创建虚拟环境, 然后把我这些文件复制过去, 在pycharm虚拟环境终端输入下面命令, 会自动安装所需的模块
pip install -r requirements.txt
