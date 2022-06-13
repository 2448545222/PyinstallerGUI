import os.path
import sys

from ui_module.MainWindUi import Ui_MainWindow
from PySide6.QtWidgets import QWidget, QFileDialog, QApplication, QMessageBox, QTableWidgetItem, QHeaderView, QDialog, \
    QLabel, QVBoxLayout
from PySide6.QtCore import QSettings, Qt
from PySide6.QtGui import QTextCursor, QIcon

# 工作目录
PATH_WORK = os.path.dirname(os.path.realpath(sys.argv[0]))
# 配置文件路径
PATH_CONFIG = os.path.join(PATH_WORK, 'config', 'config.ini')
# 版本信息路径
PATH_VERSION = os.path.join(PATH_WORK, 'config', 'file_version_info.txt')


class GetInput(Ui_MainWindow):

    def __init__(self, win):
        super().__init__(win)
        win.setWindowIcon(QIcon(os.path.join(PATH_WORK, 'config', 'img.ico')))
        self.node_tit_dict = {
            0: 'LineEdit',
            1: 'CheckBox',
            2: 'TableWidget',
            3: 'TextEdit',
            4: 'Version'
        }

        self.config_list_dict = [
            # 输入框
            {'node': self.node_tit_dict[0], 'key': 'path_main', 'value': '', 'control': self.lineEdit_path_py},
            {'node': self.node_tit_dict[0], 'key': 'path_save_dir', 'value': os.path.join(PATH_WORK, "dist"),
             'control': self.lineEdit_path_save_dir},
            {'node': self.node_tit_dict[0], 'key': 'path_temp', 'value': os.path.join(PATH_WORK, "build"),
             'control': self.lineEdit_path_temp},
            {'node': self.node_tit_dict[0], 'key': 'path_UPX', 'value': '', 'control': self.lineEdit_path_UPX},
            {'node': self.node_tit_dict[0], 'key': 'path_icon', 'value': '', 'control': self.lineEdit_path_icon},
            {'node': self.node_tit_dict[0], 'key': 'path_pyinstaller', 'value': '',
             'control': self.lineEdit_path_pyinstaller},
            {'node': self.node_tit_dict[0], 'key': 'exe_name', 'value': '', 'control': self.lineEdit_exe_name},
            {'node': self.node_tit_dict[0], 'key': 'pwd', 'value': '', 'control': self.lineEdit_pwd},

            # 复选框
            {'node': self.node_tit_dict[1], 'key': 'single_file', 'value': 'false',
             'control': self.checkBox_single_file},
            {'node': self.node_tit_dict[1], 'key': 'del_cmd', 'value': 'false', 'control': self.checkBox_del_cmd},
            {'node': self.node_tit_dict[1], 'key': 'clear', 'value': 'false', 'control': self.checkBox_clear},
            {'node': self.node_tit_dict[1], 'key': 'overwrite_file', 'value': 'false',
             'control': self.checkBox_del_temp},
            {'node': self.node_tit_dict[1], 'key': 'UPX', 'value': 'false', 'control': self.checkBox_UPX},
            # 表格
            {'node': self.node_tit_dict[2], 'key': 'add_data_file', 'value': [],
             'control': self.tableWidget_add_data_file},
            {'node': self.node_tit_dict[2], 'key': 'add_binary', 'value': [], 'control': self.tableWidget_add_binary},
            # 多行文本输入框
            {'node': self.node_tit_dict[3], 'key': 'add_module', 'value': '', 'control': self.textEdit_add_module},
            {'node': self.node_tit_dict[3], 'key': 'exclude_module', 'value': '',
             'control': self.textEdit_exclude_module},
            {'node': self.node_tit_dict[3], 'key': 'p', 'value': '', 'control': self.textEdit_p},
            {'node': self.node_tit_dict[3], 'key': 'log', 'value': '', 'control': self.textEdit_log},
            # 版本信息的表格
            {'node': self.node_tit_dict[4], 'key': 'version', 'value': [], 'control': self.tableWidget_version_info},
        ]
        # 初始化进度条的 进度
        self.prog_box_val = 0
        # 因为是判断日志中出现的字符串判断打包失败, 所以初始化个状态 只弹出一次
        self.prog_box_state = True

        self.win = win
        # 初始化配置文件对象
        self.settings = QSettings(PATH_CONFIG, QSettings.IniFormat)
        # 设置表格 自适应宽度
        self.tableWidget_add_data_file.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_add_binary.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_version_info.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 设置版本信息的表格 根据内容长度自动伸缩
        self.tableWidget_version_info.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # 设置默认打包路径
        self.lineEdit_path_save_dir.setText(os.path.join(PATH_WORK, "dist"))
        self.lineEdit_path_temp.setText(os.path.join(PATH_WORK, "build"))
        # 初始化UI
        self.init_ui()
        # "选择路径\目录" 按钮绑定点击事件: 绑定self.lineEdit_path_icon
        self.btn_select_path_py.clicked.connect(lambda: self.event_btn_select_path(self.lineEdit_path_py, "py文件(*.py)"))
        self.btn_select_path_icon.clicked.connect(
            lambda: self.event_btn_select_path(self.lineEdit_path_icon, '图标文件(*.ico)'))
        self.btn_select_path_pyinstaller.clicked.connect(
            lambda: self.event_btn_select_path(self.lineEdit_path_pyinstaller, '(*.exe)'))
        self.btn_select_path_save_dir.clicked.connect(lambda: self.event_btn_select_path(self.lineEdit_path_save_dir))
        self.btn_select_path_UPX.clicked.connect(lambda: self.event_btn_select_path(self.lineEdit_path_UPX))
        self.btn_select_path_temp.clicked.connect(lambda: self.event_btn_select_path(self.lineEdit_path_temp))
        # "使用说明" 按钮绑定点击事件
        self.btn_help.clicked.connect(self.event_btn_htlp)
        # "main路径" 输入框绑定内置信号, 触发自动寻找pyinstaller的路径
        self.lineEdit_path_py.textChanged.connect(self.event_auto_pyinstaller_path)

        # "开始打包" 按钮绑定点击事件: 保存所有控件的内容写入到ini文件
        self.btn_start.clicked.connect(self.event_start_save_config)
        # "重置" 按钮绑定点击事件: 重写ini文件为配置字典的默认状态, 然后读取ini重新初始化窗口 (清空所有控件的内容)
        self.btn_reset.clicked.connect(self.event_btn_reset)

    def init_ui(self):
        '''
        读取配置文件.ini 初始化UI的值
        :return:
        '''
        # 设置 "版本信息" 表格中的 '名称' 和 '示例' 列为只读
        for row_index in range(self.tableWidget_version_info.rowCount()):
            name = self.tableWidget_version_info.item(row_index, 0)
            example = self.tableWidget_version_info.item(row_index, 2)
            name.setFlags(Qt.ItemIsSelectable)
            example.setFlags(Qt.ItemIsSelectable)
        # 如果配置文件不存在
        if not os.path.exists(PATH_CONFIG):
            return

        # 遍历配置字典
        for config_dict in self.config_list_dict:
            # 如果是输入框(单行、多行)节点
            if config_dict["node"] == self.node_tit_dict[0] or config_dict["node"] == self.node_tit_dict[3]:
                # 获取配置文件里的数据
                value = self.settings.value(f'{config_dict["node"]}/{config_dict["key"]}')
                # 更新窗体
                config_dict['control'].setText(value)

            # 如果是复选框节点
            elif config_dict["node"] == self.node_tit_dict[1]:
                val = self.settings.value(f'{config_dict["node"]}/{config_dict["key"]}')
                value = False if val == 'false' else True
                config_dict['control'].setChecked(value)
            # 如果是表格节点
            elif config_dict["node"] == self.node_tit_dict[2]:
                # 先获取到表格控件
                table = config_dict['control']
                # 读取ini文件中表格的数据列表  格式: [[列value, 列value]..]
                data_list = self.settings.value(f'{config_dict["node"]}/{config_dict["key"]}')

                # 如果表格的数据列表为空 (代表整个表格内没有数据)
                if not data_list:
                    # 遍历所有行
                    for row_index in range(table.rowCount()):
                        # 用空白的单元格对象覆盖原来的 (清空单元格)
                        table.setItem(row_index, 0, QTableWidgetItem())
                        table.setItem(row_index, 1, QTableWidgetItem())
                    continue

                # 循环设置表格内容;  value_list == [列0"资源路径"value, 列1"目标路径"value]
                for row_index, value_list in enumerate(data_list):
                    table.setItem(row_index, 0, QTableWidgetItem(value_list[0]))
                    table.setItem(row_index, 1, QTableWidgetItem(value_list[1]))
            # 如果是版本信息节点
            elif config_dict["node"] == self.node_tit_dict[4]:
                table = config_dict['control']
                data_list = self.settings.value(f'{config_dict["node"]}/{config_dict["key"]}')
                if not data_list:
                    for row_index in range(table.rowCount()):
                        table.setItem(row_index, 1, QTableWidgetItem())
                    continue
                for row_index in range(table.rowCount()):
                    table.setItem(row_index, 1, QTableWidgetItem(data_list[row_index]))

    # 槽: "选择路径" 按钮
    def event_btn_select_path(self, line_edit, suffix=''):
        """
        事件: 弹出选择文件窗口, 并更新"路径输入框"
        :param line_edit:  要更新的输入框
        :param suffix: 指定可以选择的文件后缀, 如果要选择目录则传 False
        :return: 无
        """
        # 判断是不是 点击的 选择目录 的按钮
        if suffix == '':
            path = QFileDialog.getExistingDirectory(self.win, '选择存放目录', './')
            if path:
                line_edit.setText(path.replace('/', '\\'))
        else:
            path = QFileDialog.getOpenFileName(self.win, '打开文件', './', suffix)[0]
            if path:
                line_edit.setText(path.replace('/', '\\'))

    # 槽: "开始打包" 按钮
    def event_start_save_config(self):
        '''
        事件: 1.清空日志文本框; 2.判断必填项; 3.保存配置; 4.启动子线程[拼接参数,执行打包命令,回调日志函数];
        :return:
        '''
        # 清空日志文本框
        self.textEdit_log.clear()
        self.prog_box_val = 0
        self.progressBar.setValue(self.prog_box_val)
        # 如果 "main路径" 的输入框没有值, 则弹窗
        if not self.lineEdit_path_pyinstaller.text():
            QMessageBox.warning(self.win, '错误', '请选择pyinstaller.exe的路径')
            return
        # 如果 "pyinstaller路径" 的输入框没有值, 则弹窗
        elif not self.lineEdit_path_py.text():
            QMessageBox.warning(self.win, '错误', '请选择要打包的文件')
            return
        # 如果 "UPX" 复选框被选中 并且 "UPX" 的输入框没有值, 则弹窗
        elif self.checkBox_UPX.isChecked() and not self.lineEdit_path_UPX.text():
            QMessageBox.warning(self.win, '错误', '请选择UPX路径')
            return

        # 保存配置的循环
        for config_dict in self.config_list_dict:
            # 如果是输入框节点
            if config_dict["node"] == self.node_tit_dict[0]:
                # 获取输入框的文本
                text = config_dict['control'].text()
                # 写入到ini文件
                self.settings.setValue(f'{config_dict["node"]}/{config_dict["key"]}', text)

            # 如果是复选框节点
            elif config_dict["node"] == self.node_tit_dict[1]:
                # 获取复选框的选中状态
                check = config_dict['control'].isChecked()
                self.settings.setValue(f'{config_dict["node"]}/{config_dict["key"]}', check)

            # 如果是表格节点
            elif config_dict["node"] == self.node_tit_dict[2]:
                # 获取到表格
                table = config_dict['control']
                # 每次执行前先清空列表, 作用: 每次保存配置都是获取表格数据, 追加到列表, 如果不清空, 以前的数据不会被清楚
                config_dict['value'].clear()

                # 遍历所有行
                for row_index in range(0, table.rowCount()):
                    # 获取单元格 "资源路径" 的文本
                    data_path_cell = table.item(row_index, 0)
                    # 获取单元格 "目标路径" 的文本
                    target_cell = table.item(row_index, 1)

                    # 如果 "资源路径" 列的单元格对象不为空或不为None, 则获取文本
                    data_path_cell_text = data_path_cell.text().strip() if data_path_cell else None
                    # 如果 "目标路径" 列的单元格对象不为空或不为None, 则获取文本
                    target_text = target_cell.text().strip() if target_cell else None

                    # 如果 "资源路径" 有值 并且 "目标路径" 没值
                    if data_path_cell_text and not target_text:
                        QMessageBox.warning(self.win, '错误', '"目标路径"未填写')
                        return
                    # 如果 "目标路径" 有值 并且 "资源路径" 没值
                    elif target_text and not data_path_cell_text:
                        QMessageBox.warning(self.win, '错误', '"资源路径"未填写')
                        return

                    # 数据列表内追加 [资源路径, 目标路径]
                    config_dict['value'].append([data_path_cell_text, target_text])
                # 根据配置字典的, 写入ini文件
                self.settings.setValue(f'{config_dict["node"]}/{config_dict["key"]}', config_dict['value'])

            # 如果是多行文本输入框节点
            elif config_dict["node"] == self.node_tit_dict[3]:
                text = config_dict["control"].toPlainText()
                self.settings.setValue(f'{config_dict["node"]}/{config_dict["key"]}', text)

            # 如果是 版本信息 节点
            elif config_dict["node"] == self.node_tit_dict[4]:
                # 同理上面表格节点, 上面个格式是 [ ['cell1'],['cell2'] ]; 这里是 ['cell']
                table = config_dict['control']
                config_dict['value'].clear()
                for row_index in range(self.tableWidget_version_info.rowCount()):
                    cell = table.item(row_index, 1)
                    cell_text = cell.text() if cell else ''
                    config_dict['value'].append(cell_text)
                self.settings.setValue(f'{config_dict["node"]}/{config_dict["key"]}', config_dict['value'])

        # 执行打包命令
        from function.task_thread import StartCmd
        self.cmd = StartCmd(self.win, self, PATH_VERSION)
        self.cmd.log_sig.connect(self.log)
        self.cmd.start()

    # 槽: 更新 "日志"
    def log(self, log):
        '''
        事件: 更新日志
        :param log: 子线程通过信号传递过来的一行 打包时产生的日志(子线程输出一行, 这边就更新一行)
        :return:
        '''
        # 获取原本框内的内容
        old_text = self.textEdit_log.toPlainText()
        new_log = f'{old_text}\n{log}'
        # 加上新获取到的执行结果日志
        self.textEdit_log.setText(new_log)
        # 设置光标在末尾(这样新插入文本后, 滚动条一直在最底部,看到的是最新的日志)
        self.textEdit_log.moveCursor(QTextCursor.End)
        if 'Building EXE from EXE-00.toc completed successfully' in log:
            self.progressBar.setValue(100)

        elif self.progressBar.value() < 98:
            self.prog_box_val += 1
            self.progressBar.setValue(self.prog_box_val)

        if (new_log.find('Traceback (most recent call last):') != -1 or new_log.find('Exception') != -1 or new_log.find(
                'error') != -1) and self.prog_box_state:
            self.prog_box_state = False
            QMessageBox.warning(self.win, '错误', '打包失败')

    # 槽: "重置" 按钮
    def event_btn_reset(self):
        '''
        事件: 1.根据默认配置的字典, 重新写入配置文件, 然后调用self.init_ui() 重新读取配置文件更新窗口; 2.进度条归零
        :return:
        '''
        # 遍历配置字典
        for config_dict in self.config_list_dict:
            # 如果是表格节点
            if config_dict["node"] == self.node_tit_dict[2] or config_dict["node"] == self.node_tit_dict[4]:
                # 清空数据列表
                config_dict['value'].clear()
            # 根据字典中的默认配置, 重新写入ini文件
            self.settings.setValue(f'{config_dict["node"]}/{config_dict["key"]}', config_dict["value"])
            self.progressBar.setValue(0)
            # 重新初始化界面
            self.init_ui()

    # 槽: 自动寻找pyinstaller路径
    def event_auto_pyinstaller_path(self):
        '''
        事件: 自动寻找pyinstaller的路径并在输入框显示
        :return:
        '''
        # 如果"main路径"为空
        if not self.lineEdit_path_py.text():
            return
        # 遍历某路径下所有文件 and 文件夹
        for file_all in os.walk(os.path.dirname(self.lineEdit_path_py.text())):
            # 遍历所有 文件 名
            for name in file_all[2]:
                # 如果文件名是 XXX
                if name == 'pyinstaller.exe':
                    # pyinstaller输入框内设置上 拼接的完整路径
                    self.lineEdit_path_pyinstaller.setText(os.path.join(file_all[0], name))
                    break

    def event_btn_htlp(self):
        """
        事件: 弹出窗口 显示使用说明
        :return:
        """
        h = Help()
        h.exec()


class Help(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(600, 200)
        layou = QVBoxLayout()
        label = QLabel()
        label.setText('''
        1. 路径里尽量不要有中文!!!!  尤其是"main路径"里!!!
        
        2. "添加数据文件" 和 "添加编译文件" 的 '目标路径', 多文件打包 是以打包后的 *.exe所在目录为根路径, 可以使用相对路径;
        2.1 示例: 资源路径: F:\\config\\配置.ini   目标路径: .\\config
        
        2.2 单文件打包: 实际就是把多文件打包出来的东西 压缩成单文件,运行后会解压到C盘的temp\\xx目录下 所以实际上有2个exe, 以解压后的*.exe所在目录为根路径

        3. 点击"开始打包"后, 会进行打包, 并把所有的信息保存, 下次打开还是这次打包的记录; 可以点"重置"按钮, 所有信息都会被清空
        
        3. 选择"main路径"后, 会自动寻找pyinstaller.exe的路径, 如果没找到, 请手动选择;
        
        4. 如果要使用加密打包 先安装这个模块  "pip install tinyaes"
        ''')
        layou.addWidget(label)
        self.setLayout(layou)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    q_widget = QWidget()
    get_input = GetInput(q_widget)
    q_widget.show()
    sys.exit(app.exec())
