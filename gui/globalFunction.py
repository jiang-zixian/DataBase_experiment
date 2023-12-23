from PyQt5.QtWidgets import QMessageBox


#显示提示框
def show_msg_box(title,msg):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle(title)
    msg_box.setText(msg)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()
    #返回选择结果
    return msg_box.clickedButton().text()