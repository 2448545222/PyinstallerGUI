import subprocess
from shutil import rmtree
import os.path
from PySide6.QtCore import QThread, Signal


class StartCmd(QThread):
    log_sig = Signal(str)

    def __init__(self, win_obj, sf, PATH_VERSION):
        super().__init__(win_obj)
        self.sf = sf
        self.version_path = PATH_VERSION
        self.new_version_path = os.path.join(os.path.dirname(self.version_path), 'my_file_version_info.txt')

    def run(self):
        # 获取参数
        pyinstaller = self.sf.lineEdit_path_pyinstaller.text()
        save_dir = self.sf.lineEdit_path_save_dir.text()
        temp_dir = self.sf.lineEdit_path_temp.text()
        icon_dir = self.sf.lineEdit_path_icon.text()
        icon_dir = f'-i="{icon_dir}"' if icon_dir else ''

        upx_dir = self.sf.lineEdit_path_UPX.text()
        main_dir = self.sf.lineEdit_path_py.text()
        name = self.sf.lineEdit_exe_name.text().strip()
        name = f'-n="{name}"' if name else ''
        pwd = self.sf.lineEdit_pwd.text().strip()
        pwd = f'--key="{pwd}"' if pwd else ''

        add_mod = self.sf.textEdit_add_module.toPlainText().strip()
        exclude_mod = self.sf.textEdit_exclude_module.toPlainText().strip()
        p = self.sf.textEdit_p.toPlainText().strip()

        def read_table(table, par):
            add_data = []
            for row_index in range(0, table.rowCount()):
                data = table.item(row_index, 0)
                target = table.item(row_index, 1)
                if data and target:
                    if data.text().strip() and target.text().strip():
                        add_data.append(f'{par}="{data.text().strip()};{target.text().strip()}"')
            return add_data

        add_data = read_table(self.sf.tableWidget_add_data_file, '--add-data')
        add_binary = read_table(self.sf.tableWidget_add_binary, '--add-binary')

        add_data = ' '.join(add_data)
        add_binary = ' '.join(add_binary)


        add_mod = f'--hidden-import="{add_mod}"' if add_mod else ''
        exclude_mod = f'--exclude-module = "{exclude_mod}"' if exclude_mod else ''
        p = f'-p="{p}"' if p else ''

        p_upx = f'--upx-dir={upx_dir}' if self.sf.checkBox_UPX.isChecked() else '--noupx'
        p_cw = '-w' if self.sf.checkBox_del_cmd.isChecked() else '-c'
        p_clean = '--clean' if self.sf.checkBox_clear.isChecked() else ''
        p_fd = '-F' if self.sf.checkBox_single_file.isChecked() else '-D'

        if self.sf.groupBox_version_info.isChecked():
            data_dict = {}

            for row_index in range(self.sf.tableWidget_version_info.rowCount()):
                cell = self.sf.tableWidget_version_info.item(row_index, 1)
                if cell:
                    data_dict[row_index] = cell.text()
            version_info = f"""
         StringStruct('CompanyName', '{data_dict.get(0, '')}'),
         StringStruct('FileDescription', '{data_dict.get(1, '')}'),
         StringStruct('FileVersion', '{data_dict.get(2, '')}'),
         StringStruct('InternalName', '{data_dict.get(3, '')}'),
         StringStruct('LegalCopyright', '{data_dict.get(4, '')}'),
         StringStruct('OriginalFilename', '{data_dict.get(5, '')}'),
         StringStruct('ProductName', '{data_dict.get(6, '')}'),
         StringStruct('ProductVersion', '{data_dict.get(7, '')}'"""

            with open(self.version_path, 'r', encoding='utf8') as odl_f, open(self.new_version_path, 'w',
                                                                              encoding='utf8') as new_f:
                res = odl_f.read()
                res = res.replace("""StringStruct('CompanyName', ''),
        StringStruct('FileDescription', ''),
        StringStruct('FileVersion', ''),
        StringStruct('InternalName', ''),
        StringStruct('LegalCopyright', ''),
        StringStruct('OriginalFilename', ''),
        StringStruct('ProductName', ''),
        StringStruct('ProductVersion', ''""", version_info)
                new_f.write(res)
        version_file = f'--version-file="{self.new_version_path}"' if self.sf.groupBox_version_info.isChecked() else ''

        param = f'{pyinstaller} -y --distpath="{save_dir}" --workpath="{temp_dir}" --specpath="{temp_dir}" {icon_dir} {name} {pwd} {p} {add_mod} {exclude_mod} {add_data} {add_binary} {version_file} {p_upx} {p_cw} {p_clean} {p_fd} {main_dir}'

        # 执行命令
        proc = subprocess.Popen(param, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,  universal_newlines=True)

        while True:
            line = proc.stderr.readline()
            if line != '':
                # 发射执行结果
                self.log_sig.emit(line)
            if proc.poll() is not None:
                break
        # 事件: 自动删除打包时生成的"build"临时目录
        if self.sf.checkBox_del_temp.isChecked():
            rmtree(self.sf.lineEdit_path_temp.text()) if os.path.exists(self.sf.lineEdit_path_temp.text()) else None


if __name__ == '__main__':
    pass
