import os
import webbrowser


class Utils():

    def openCreate(self, task_create):
        url = f"https://helpdesk.efko.ru/tasks/view?code={task_create}"
        webbrowser.open(url)


    def openUser(self, isui):
        url = f"https://helpdesk.efko.ru/tasks/user?code={isui}"
        webbrowser.open(url)


    def editUser(self, isui):
        url = f"https://helpdesk.efko.ru/user/edit/correct-data?code={isui}"
        webbrowser.open(url)


    def ping(self, items):
        if len(items) <= 0:
            return
        item = items[0]
        pc_name = item.text(0).split(' - ')[0]
        response = os.system("start cmd /c ping " + pc_name + " -t -4")


    def openC(self, items):
        #items = self.ui.pc_name.selectedItems()
        if len(items) <= 0:
            return
        item = items[0]
        pc_name = item.text(0).split(' - ')[0]
        response = os.system("start explorer \\\\" + pc_name + "\\c$")


    def openDir(self, items, login):
        #items = self.ui.pc_name.selectedItems()
        if len(items) <= 0:
            return
        item = items[0]
        pc_name = item.text(0).split(' - ')[0]
        response = os.system("start explorer \\\\" + pc_name + "\\c$\\users\\" + login)