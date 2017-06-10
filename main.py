import tkinter

tk = tkinter
Button = tk.Button
Entry = tk.Entry
Label = tk.Label
Text = tk.Text

item_bg = '#EBEAE4'

class UI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('公投生成器')
        self.pack(anchor='w', fill='both', expand=1)

        self.content = content
        self.textbox = Text(text=None, bg=item_bg)
        self.textbox.place(x=5,y=5)

        copy_title = Button(text='複製標題', bg=item_bg, width=20, height=2, command=self.copy_title)
        copy = Button(text='複製公投文', bg=item_bg, width=20, height=2, command=self.copy_content)
        copy_title.place(x=454, y=350)
        copy.place(x=454, y=395)

        tip = Label(text='Tip: 用Tab轉行')
        tip.place(x=20, y=475)

        self.items = {}
        self.name = {'title': '標題',
                     'suspectID': '嫌疑犯編號：',
                     'suspect_name': '嫌疑犯名稱：',
                     'reason': '發起公投原因',
                     'edvince_link': '超連結或截圖：',
                     'edvince': '證據描述：',}

        for dy, name in enumerate(self.name):
            item = Label(text=self.name[name])

            sv = tk.StringVar()
            sv.trace('w', lambda name, index, mode, sv=sv: self.text_changed(sv))
            entry = Entry(bg=item_bg, width=50, textvariable=sv)
            entry.bind('<<Modified>>', self.text_changed)
            entry.focus_set()
            
            item.place(x=20,y=350+dy*20)
            entry.place(x=100,y=350+dy*20)

            self.items[name] = entry
        self.items['title']['state'] = 'disabled'

    def copy_title(self):
        self.clipboard_clear()
        self.clipboard_append(self.items['title'].get())

    def copy_content(self):
        self.clipboard_clear()
        self.clipboard_append(self.textbox.get(1.0, 'end'))

    def generate(self):
        title = '[內務 - 封鎖公投] 會員 {suspect_name} ID:{suspectID} {reason}'.format(**info)
        sv = tk.StringVar()
        entry = self.items['title']['textvariable'] = sv
        sv.set(title)

        content = self.content.format(**info)
        self.textbox.delete(1.0, 'end')
        self.textbox.insert('end', content)

    def text_changed(self, value=None):
        for item in self.items:
            info[item] = self.items[item].get()
        self.generate()

content = ('[內務 - 封鎖公投] 會員 {suspect_name} ID:{suspectID}\n'
            '本人根據「封鎖違反版規會員公投法」，提出以下公投：\n'
           '\n'
            '(1) 嫌疑犯會員編號：{suspectID}\n'
            '(2) 關於案情的詳盡描述，交待發起公投的原因\n'
            '{reason}\n'
            '\n'
            '(3) 相關證據，如超連結或截圖等\n'
            '{edvince_link}\n'
            '{edvince}\n'
           '\n'
            '(4) 通過封鎖公投的條件\n'
            '(1)於三小時內取得另外五名會員留言和議封鎖；\n'
            '(2a)於三小時後，贊成封鎖數目達到總票數的三分之二以上，且贊成封鎖數目不少於20\n'
            '或\n'
            '(2b)於三小時內的任何時刻，贊成封鎖數目達到總票數的三分之二以上，且贊成封鎖數目不少於50'
            '則封鎖公投獲通過，該會員需被封鎖，而公投繼續進行；否則本次公投被否決而作廢。'
            '於已成立的封鎖公投之投票期結束後，以第二個三分位數之投票選項為結果，並依據「版規及違反版規之相關罰則」決定最終刑期。'
            '其中，如果結果為「反對封鎖」，則解除對該名會員之封鎖及刪除該次犯罪記錄。'
            '\n\n'
            '請各會員盡義務，認真審視案情，作出合理判斷，''並投票（或和議）保障眾會員（包括嫌疑犯）利益。'
            '會員也可先參考《封鎖會員記錄》中的過往案例，避免雙重標準。')

info = {'suspectID': '',
        'suspect_name': '',
        'reason': '',
        'edvince_link': '',
        'edvince': ''}

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('650x524+0+0')
    main = UI(root)
    main.generate()
    
