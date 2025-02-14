import tkinter
import customtkinter
import pprint
import tkinter.messagebox
from sys import exit
from random import sample
from PIL import Image, ImageTk, ImageDraw

WIDTH = 1920
HEIGHT = 1080

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

COLORS = {"blue": (0, 0, 255, 100),  # RGBA
         "red": (255, 0, 0, 100),
         "darkgreen": (0, 100, 0, 100),
         "cyan": (0, 255, 255, 100),
         "yellow": (255, 255, 0, 100),
         "orange": (255, 69, 0, 100),
         "pink": (255, 0, 255, 100),
         "brown": (139, 69, 19, 100),
         "lime": (0, 255, 0, 100),
         "hotpink": (255, 105, 180, 100)
         }

TERRS = {"1": [(366, 72), "white", (2, 7, 8, 110), True, 15],
        # координаты центра, принадлежность, соседи, можеть ли быть стартовой, стоимость
        "2": [(587, 49), "white", (1, 3, 7, 8), False, 15],
        "3": [(664, 113), "white", (2, 4, 8, 9, 13, 14), False, 15],
        "4": [(792, 57), "white", (3, 5, 9, 10), True, 15],
        "5": [(885, 114), "white", (4, 6, 9, 10, 11), False, 15],
        "6": [(1014, 167), "white", (5, 10, 11, 21, 22), False, 15],
        "7": [(430, 155), "white", (1, 2, 8, 12, 109, 110), False, 15],
        "8": [(544, 128), "white", (1, 2, 3, 7, 12, 13), False, 15],
        "9": [(753, 152), "white", (3, 4, 5, 10, 13, 14), False, 15],
        "10": [(802, 171), "white", (4, 5, 6, 9, 11, 14, 15), False, 15],
        "11": [(920, 224), "white", (5, 6, 10, 15, 20, 21, 22), False, 15],
        "12": [(476, 214), "white", (7, 8, 13, 16, 109), False, 10],
        "13": [(588, 196), "white", (3, 8, 9, 12, 14, 16, 17, 18), False, 10],
        "14": [(706, 214), "white", (3, 9, 10, 11, 13, 15, 17, 18), False, 10],
        "15": [(820, 252), "white", (10, 11, 14, 18, 19, 20, 21), False, 10],
        "16": [(546, 269), "white", (12, 13, 17, 23, 101, 102, 109), False, 10],
        "17": [(579, 300), "white", (13, 14, 16, 18, 23, 24, 101), False, 10],
        "18": [(709, 312), "white", (13, 14, 15, 17, 19, 23, 24), False, 10],
        "19": [(800, 340), "white", (15, 18, 20, 24, 26, 27), False, 10],
        "20": [(904, 316), "white", (11, 15, 19, 21, 22, 27, 28), False, 10],
        "21": [(1005, 288), "white", (6, 11, 15, 20, 22, 28), False, 15],
        "22": [(1061, 322), "white", (6, 11, 20, 21, 28, 29), True, 15],
        "23": [(579, 380), "white", (16, 17, 18, 24, 100, 101), False, 5],
        "24": [(736, 367), "white", (17, 18, 19, 23, 25, 26, 100), False, 5],
        "25": [(712, 460), "white", (24, 26, 30, 38, 39, 100), False, 5],
        "26": [(838, 389), "white", (19, 24, 25, 27, 30), False, 10],
        "27": [(903, 385), "white", (19, 20, 26, 28, 30, 31), False, 10],
        "28": [(988, 381), "white", (20, 21, 22, 27, 29, 32, 31), False, 10],
        "29": [(1091, 379), "white", (22, 28, 31, 32, 33), False, 15],
        "30": [(817, 462), "white", (25, 26, 27, 31, 37, 38, 39), False, 10],
        "31": [(981, 468), "white", (27, 28, 29, 30, 32, 35, 36, 37), False, 10],
        "32": [(1110, 453), "white", (28, 29, 31, 33, 34, 35), False, 15],
        "33": [(1196, 460), "white", (29, 32, 35, 34), False, 15],
        "34": [(1241, 526), "white", (32, 33, 35, 47, 48), True, 15],
        "35": [(1113, 589), "white", (31, 32, 33, 34, 36, 46, 47), False, 15],
        "36": [(1000, 582), "white", (31, 35, 37, 42, 43, 45, 46), False, 10],
        "37": [(909, 513), "white", (30, 31, 36, 38, 42), False, 10],
        "38": [(777, 555), "white", (25, 30, 37, 39, 40, 41, 42, 43), False, 10],
        "39": [(757, 519), "white", (25, 30, 38, 40, 59, 100), False, 5],
        "40": [(786, 607), "white", (38, 39, 41, 58, 59, 64), False, 10],
        "41": [(859, 605), "white", (38, 40, 42, 43, 57, 58), False, 10],
        "42": [(894, 557), "white", (36, 37, 38, 41, 43), False, 10],
        "43": [(935, 615), "white", (36, 38, 41, 42, 44, 45, 57, 58), False, 10],
        "44": [(900, 677), "white", (41, 43, 45, 50, 57, 58), False, 10],
        "45": [(1019, 634), "white", (36, 43, 44, 46, 47, 50), False, 10],
        "46": [(1067, 583), "white", (35, 36, 43, 45, 47), False, 10],
        "47": [(1133, 672), "white", (34, 35, 45, 46, 48, 49, 50), False, 15],
        "48": [(1231, 639), "white", (34, 47, 49, 50), False, 15],
        "49": [(1174, 765), "white", (47, 48, 50, 51, 52), False, 15],
        "50": [(992, 714), "white", (44, 45, 47, 48, 49, 51, 56, 57), False, 15],
        "51": [(996, 746), "white", (49, 50, 52, 56, 57), False, 15],
        "52": [(1095, 867), "white", (49, 51, 53, 56), True, 15],
        "53": [(1044, 909), "white", (52, 54, 56, 72), False, 15],
        "54": [(952, 874), "white", (53, 55, 56, 71, 72), False, 15],
        "55": [(858, 813), "white", (54, 56, 57, 65, 71, 72), False, 15],
        "56": [(945, 807), "white", (50, 51, 52, 53, 54, 55, 57), False, 15],
        "57": [(905, 731), "white", (41, 43, 44, 50, 51, 55, 56, 58, 64, 65, 71), False, 10],
        "58": [(832, 674), "white", (40, 41, 43, 44, 57, 64, 65), False, 10],
        "59": [(673, 635), "white", (39, 40, 60, 62, 63, 64, 100), False, 5],
        "60": [(550, 591), "white", (59, 61, 62, 63, 97, 99, 100), False, 5],
        "61": [(491, 606), "white", (60, 62, 87, 96, 97, 99), False, 5],
        "62": [(488, 670), "white", (59, 60, 61, 63, 78, 86, 87), False, 10],
        "63": [(534, 721), "white", (59, 60, 62, 64, 66, 67, 77, 78, 86), False, 10],
        "64": [(720, 714), "white", (40, 57, 58, 59, 63, 65, 66), False, 10],
        "65": [(785, 784), "white", (55, 57, 58, 64, 66, 69, 70, 71), False, 10],
        "66": [(657, 782), "white", (63, 64, 65, 67, 68, 69), False, 10],
        "67": [(574, 837), "white", (63, 66, 68, 69, 77, 78), False, 10],
        "68": [(634, 899), "white", (66, 67, 69, 70, 75, 77), False, 10],
        "69": [(655, 848), "white", (65, 66, 67, 68, 70, 75), False, 10],
        "70": [(722, 905), "white", (65, 68, 69, 71, 72, 73, 74, 75), False, 15],
        "71": [(805, 875), "white", (54, 55, 57, 65, 70, 72, 73), False, 15],
        "72": [(843, 973), "white", (53, 54, 55, 71, 73), False, 15],
        "73": [(745, 992), "white", (70, 71, 72, 74), True, 15],
        "74": [(640, 1013), "white", (70, 73, 75, 76), False, 15],
        "75": [(645, 964), "white", (68, 69, 70, 74, 76, 77), False, 15],
        "76": [(521, 1030), "white", (74, 75, 77, 111), False, 15],
        "77": [(512, 908), "white", (63, 67, 68, 75, 76, 78, 111), False, 15],
        "78": [(430, 805), "white", (62, 63, 67, 77, 79, 80, 86, 111), False, 15],
        "79": [(355, 822), "white", (78, 80, 81, 82, 85, 86), False, 15],
        "80": [(333, 905), "white", (78, 79, 81, 111), False, 15],
        "81": [(251, 882), "white", (79, 80, 82), False, 15],
        "82": [(207, 812), "white", (79, 81, 83, 84, 85), True, 15],
        "83": [(156, 776), "white", (82, 84, 85, 89, 90, 93), False, 15],
        "84": [(232, 712), "white", (82, 83, 85, 86, 88, 89, 90, 93), False, 15],
        "85": [(257, 754), "white", (79, 82, 83, 84, 86), False, 15],
        "86": [(353, 741), "white", (62, 63, 78, 79, 84, 85, 87, 88), False, 10],
        "87": [(374, 612), "white", (61, 62, 86, 88, 96, 97), False, 10],
        "88": [(322, 617), "white", (84, 86, 87, 89, 95, 96), False, 10],
        "89": [(235, 612), "white", (83, 84, 88, 90, 93, 94, 95, 96), False, 10],
        "90": [(130, 690), "white", (83, 84, 89, 91, 93), False, 15],
        "91": [(61, 579), "white", (90, 92, 93), True, 15],
        "92": [(102, 522), "white", (89, 91, 93, 94, 105), False, 15],
        "93": [(141, 609), "white", (83, 84, 89, 90, 91, 92, 94), False, 15],
        "94": [(176, 515), "white", (89, 92, 93, 95, 104, 105), False, 15],
        "95": [(263, 518), "white", (88, 89, 94, 96, 98, 103, 104), False, 10],
        "96": [(332, 573), "white", (61, 87, 88, 89, 95, 97, 98), False, 10],
        "97": [(438, 545), "white", (60, 61, 87, 96, 98, 99), False, 5],
        "98": [(360, 494), "white", (95, 96, 97, 99, 101, 102, 103), False, 10],
        "99": [(474, 503), "white", (60, 61, 97, 98, 100, 101, 102), False, 5],
        "100": [(583, 508), "white", (23, 24, 25, 39, 59, 60, 99, 101), False, 5],
        "101": [(517, 420), "white", (16, 17, 23, 98, 99, 100, 102), False, 5],
        "102": [(435, 371), "white", (16, 98, 99, 101, 103, 108, 109), False, 10],
        "103": [(343, 420), "white", (95, 98, 102, 104, 108), False, 10],
        "104": [(247, 425), "white", (94, 95, 103, 105, 106, 108), False, 15],
        "105": [(174, 421), "white", (92, 94, 104, 106), False, 15],
        "106": [(176, 356), "white", (104, 105, 107, 108), True, 15],
        "107": [(219, 206), "white", (106, 108, 109, 110), False, 15],
        "108": [(323, 326), "white", (102, 103, 104, 106, 107, 109, 110), False, 15],
        "109": [(429, 263), "white", (7, 12, 16, 102, 107, 108, 110), False, 15],
        "110": [(244, 144), "white", (1, 7, 107, 108, 109), False, 15],
        "111": [(375, 979), "white", (76, 77, 78, 80), True, 15]
        }


class MainMenu:
   def __init__(self):
       self.btn_new_game = customtkinter.CTkButton(master=root,
                                                   text="Новая игра",
                                                   font=('Play', 50, 'bold'),
                                                   border_width=2,
                                                   corner_radius=20,
                                                   border_spacing=20,
                                                   command=self.amount_of_commands)
       self.btn_new_game.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
       self.btn_change_map = customtkinter.CTkButton(master=root,
                                                     text="Выбор карты",
                                                     font=('Play', 50, 'bold'),
                                                     border_width=2,
                                                     corner_radius=20,
                                                     border_spacing=20,
                                                     command=self.change_map)
       self.btn_change_map.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
       self.btn_exit_game = customtkinter.CTkButton(master=root,
                                                    text="Выход",
                                                    font=('Play', 50, 'bold'),
                                                    border_width=2,
                                                    corner_radius=20,
                                                    border_spacing=20,
                                                    command=exit)
       self.btn_exit_game.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

   def change_map(self):
       pass

   def amount_of_commands(self):
       dialog = customtkinter.CTkToplevel()
       dialog.geometry("800x300+100+100")
       dialog.title('Количество команд')
       dialog.attributes('-topmost', 1)
       dialog.iconbitmap('infoboy/icon2.ico')
       lbl = customtkinter.CTkLabel(master=dialog,
                                    text="Введите количество команд:",
                                    font=('Play', 30, 'bold'))
       lbl.place(relx=0.05, rely=0.1, anchor=tkinter.W)
       ent = customtkinter.CTkEntry(master=dialog,
                                    width=100,
                                    font=('Play', 30, 'bold'),
                                    border_width=2,
                                    corner_radius=10)
       ent.place(relx=0.65, rely=0.1, anchor=tkinter.W)

       lbl1 = customtkinter.CTkLabel(master=dialog,
                                     text="Введите количество раундов:",
                                     font=('Play', 30, 'bold'))
       lbl1.place(relx=0.05, rely=0.35, anchor=tkinter.W)
       ent1 = customtkinter.CTkEntry(master=dialog, width=100,
                                     font=('Play', 30, 'bold'),
                                     border_width=2,
                                     corner_radius=10)
       ent1.place(relx=0.65, rely=0.35, anchor=tkinter.W)

       btn = customtkinter.CTkButton(master=dialog,
                                     text="Далее",
                                     font=('Play', 30, 'bold'),
                                     command=lambda: (mp.set_amount_of_commands(int(ent.get().strip())),
                                                      self.points_per_round(int(ent1.get().strip())),
                                                      dialog.destroy()))

       # btn = customtkinter.CTkButton(master=dialog,
       #                               text="Далее",
       #                               font=('Play', 30, 'bold'),
       #                               command=lambda: (mp.run(int(ent.get().strip())),
       #                                       dialog.destroy(), self.btn_change_map.destroy(),
       #                                       self.btn_exit_game.destroy(),
       #                                       self.btn_new_game.destroy()) if ent.get().strip().isdigit() and int(
       #                          ent.get()) < 11
       #                          else (tkinter.messagebox.showerror(title="Ошибка количества команд",
       #                                                             message="Введите количество команд"),
       #                                ent.delete(0, len(ent.get()))))
       btn.place(x=50, y=200)

   def points_per_round(self, amount_of_rounds):
       dialog = customtkinter.CTkToplevel()
       dialog.geometry(f"400x{amount_of_rounds * 100 + 50}+400+10")
       dialog.title('Очки за раунды')
       dialog.attributes('-topmost', 1)
       dialog.iconbitmap('infoboy/icon2.ico')
       ent_rounds_points = []
       for i in range(amount_of_rounds):
           ent_rounds_points.append(customtkinter.CTkEntry(master=dialog, width=100,
                                                           font=('Play', 30, 'bold'),
                                                           border_width=2,
                                                           corner_radius=10))

       for i in range(amount_of_rounds):
           customtkinter.CTkLabel(master=dialog,
                                  text=f"{i + 1} Раунд",
                                  font=('Play', 30, 'bold')).place(relx=0.1,
                                                                   rely=int(i) * (10 / (
                                                                               amount_of_rounds + 1)) / 10 + 0.05,
                                                                   anchor=tkinter.W)
           ent_rounds_points[i].place(relx=0.65,
                                      rely=int(i) * (10 / (amount_of_rounds + 1)) / 10 + 0.05,
                                      anchor=tkinter.W)
       btn = customtkinter.CTkButton(master=dialog,
                                     text="Далее",
                                     font=('Play', 30, 'bold'),
                                     command=lambda: (mp.run(),
                                                      mp.set_points_per_round(
                                                          [int(j.get().strip()) for j in ent_rounds_points]),
                                                      dialog.destroy(),
                                                      self.btn_change_map.destroy(),
                                                      self.btn_exit_game.destroy(),
                                                      self.btn_new_game.destroy()))
       btn.place(relx=0.5, rely=0.95, anchor=tkinter.CENTER)


class Statistics:
   def __init__(self):
       self.window = 0
       self.commands = []

   def show_stats(self, command_points):
       self.window = customtkinter.CTkToplevel()
       self.window.geometry('500x700+700+300')
       self.window.title('Очки команд')
       self.window.iconbitmap('infoboy/icon2.ico')
       customtkinter.CTkLabel(self.window,
                              text="Очки команд на текущий раунд",
                              font=('Play', 22, 'bold')).place(relx=0.5,
                                                               rely=0.06,
                                                               anchor=tkinter.CENTER)
       customtkinter.CTkLabel(self.window,
                              text="Очки команд на текущий раунд",
                              font=('Play', 22, 'bold')).place(relx=0.5,
                                                               rely=0.06,
                                                               anchor=tkinter.CENTER)
       customtkinter.CTkLabel(self.window,
                              text="Очки команд на текущий раунд",
                              font=('Play', 22, 'bold')).place(relx=0.5,
                                                               rely=0.06,
                                                               anchor=tkinter.CENTER)
       print(mp.get_comm_coll())
       commands = mp.get_comm_coll()
       for num, color in commands.items():
           customtkinter.CTkLabel(self.window,
                                  text=f"{num}. {color.capitalize()}",
                                  font=('Play', 22, 'bold')).place(relx=0.1,
                                                                   rely=int(num) * 1.2 / 10 + 0.1,
                                                                   anchor=tkinter.W)
           customtkinter.CTkLabel(self.window,
                                  text=f"{command_points[color]}",
                                  font=('Play', 22, 'bold')).place(relx=0.5,
                                                                   rely=int(num) * 1.2 / 10 + 0.1,
                                                                   anchor=tkinter.W)
       self.window.mainloop()


class Map:
   def __init__(self):
       # Создание объектов на экране
       # self.canvas = tkinter.Canvas(root,
       #                              height=2000,
       #                              width=1400,
       #                              bg="#DDDDDD",
       #                              bd=0,
       #                              highlightthickness=0,
       #                              highlightbackground='#DDDDDD')
       self.amount_of_commands = 0
       # self.ent_color = tkinter.Entry(root)
       # self.ent_terr = tkinter.Entry(root)
       #
       # self.btn_coloring = tkinter.Button(root,
       #                                    text='Закрасить',
       #                                    command=self.coloring)
       self.btn_round_results = customtkinter.CTkButton(master=root,
                                                        text="Внести результаты\nраунда",
                                                        font=('Play', 40, 'bold'),
                                                        width=10,
                                                        border_width=2,
                                                        corner_radius=20,
                                                        border_spacing=20,
                                                        command=self.round_results)
       self.btn_new_commands = customtkinter.CTkButton(root,
                                                       text="Расставить команды\nзаново",
                                                       font=('Play', 40, 'bold'),
                                                       width=10,
                                                       border_width=2,
                                                       corner_radius=20,
                                                       border_spacing=20,
                                                       command=self.new_commands)

       self.btn_show_points = customtkinter.CTkButton(root,
                                                      text="Показать очки\nкоманд",
                                                      font=('Play', 40, 'bold'),
                                                      width=10,
                                                      border_width=2,
                                                      corner_radius=20,
                                                      border_spacing=20,
                                                      command=self.show_points)

       self.btn_exit_map = customtkinter.CTkButton(root,
                                                   text="Вернуться в главное\nменю",
                                                   font=('Play', 40, 'bold'),
                                                   width=10,
                                                   border_width=2,
                                                   corner_radius=20,
                                                   border_spacing=20,
                                                   command=self.back_to_menu)

       # Создание объектов для работы карты
       self.map_canvas = tkinter.Canvas(root, height=2000,
                                        width=1400,
                                        bg="#DDDDDD",
                                        bd=0,
                                        highlightthickness=0,
                                        highlightbackground='#DDDDDD')
       self.map1_image = Image.open("infoboy/map_1.png").convert("RGBA")
       self.map1_photo = ImageTk.PhotoImage(self.map1_image)
       self.canvas1_image = self.map_canvas.create_image(50, 0, anchor='nw', image=self.map1_photo)

       self.map2_image = Image.open("infoboy/map_2.png").convert("RGBA")
       self.map2_photo = ImageTk.PhotoImage(self.map2_image)
       self.canvas2_image = self.map_canvas.create_image(50, 0, anchor='nw', image=self.map2_photo)

       self.map3_image = Image.open("infoboy/map_3.png").convert("RGBA")
       self.map3_photo = ImageTk.PhotoImage(self.map3_image)
       self.canvas3_image = self.map_canvas.create_image(50, 0, anchor='nw', image=self.map3_photo)

       self.GAME_TERRS = TERRS
       self.COMMAND_POINTS = dict()
       self.POINTS_PER_ROUND = list()
       self.comm_coll = dict()
       self.current_round = -1

   def get_comm_coll(self):
       return self.comm_coll

   def set_amount_of_commands(self, amount_of_commands):
       self.amount_of_commands = amount_of_commands
       self.commands_colors(amount_of_commands)
       self.start_painting(amount_of_commands)

   def set_points_per_round(self, points_per_round):
       self.POINTS_PER_ROUND = points_per_round
       print(self.POINTS_PER_ROUND)

   def run(self):
       self.map_canvas.place(x=550, y=0)
       # self.btn_coloring.place(relx=0.5, rely=0.9)
       # self.ent_color.place(relx=0.7, rely=0.9)
       # self.ent_terr.place(relx=0.6, rely=0.9)
       self.btn_round_results.place(relx=0.15, rely=0.3, anchor=tkinter.CENTER)
       self.btn_exit_map.place(relx=0.15, rely=0.7, anchor=tkinter.CENTER)
       self.btn_new_commands.place(relx=0.15, rely=0.1, anchor=tkinter.CENTER)
       self.btn_show_points.place(relx=0.15, rely=0.5, anchor=tkinter.CENTER)
       # self.amount_of_commands = amount_of_commands
       # self.commands_colors(amount_of_commands)
       # self.start_painting(amount_of_commands)

   def update_terrs(self, results, correct_answer):
       print('\n\n\n')
       print("______________________________________________")
       pprint.pprint(results)
       print("______________________________________________")
       print(self.COMMAND_POINTS)
       print("______________________________________________")
       print(self.POINTS_PER_ROUND)
       print("______________________________________________")
       print(correct_answer)
       print("______________________________________________")
       print('\n\n\n')

       # добавляем очки за раунд в банк очков команд
       for com, value in self.COMMAND_POINTS.items():
           if correct_answer[com] == 'on':
               self.COMMAND_POINTS[com] += self.POINTS_PER_ROUND[self.current_round]
       wish_list = dict()

       # находим сумму потраченных очков каждой команды на данный ход
       for terr, params in results.items():
           for elem in params:
               if elem[0] in wish_list:
                   wish_list[elem[0]] += elem[1]
               else:
                   wish_list[elem[0]] = elem[1]

       # если команда хочет потратить больше, чем есть в банке, то обнуляем её "хотелки"
       for com, value in wish_list.items():
           if value > self.COMMAND_POINTS[com]:
               for terr, params in results.items():
                   for elem in params:
                       if elem[0] == com:
                           elem[1] = 0

       # Выводим изменённый список атак на территории с обнулёнными очками
       print("______________________________________________")
       pprint.pprint(results)
       print("______________________________________________")

       for terr, params in results.items():
           sp_attack = []
           sp_defeat = []
           for i in range(len(params)):
               if params[i][2] == "ATTACK" and any(
                       [True if self.GAME_TERRS[str(item)][1] == params[i][0] else False for item in
                        self.GAME_TERRS[terr][2]]):
                   sp_attack.append([params[i][0], params[i][1]])
               if params[i][2] == "DEFEAT" and self.GAME_TERRS[str(terr)][1] == params[i][0]:
                   sp_defeat = [params[i][0], params[i][1]]
           print('Территория', terr)
           print("ATTACK", sp_attack)
           print("DEFEAT", sp_defeat)
           print('\n\n\n')
           if all([True if [p[1] for p in sp_attack].count(points) == 1 else False for points in
                   [p[1] for p in sp_attack]]) and \
                   (len(sp_defeat) != 0 and len(sp_attack) != 0 and max([p[1] for p in sp_attack]) > sp_defeat[
                       1] + self.GAME_TERRS[terr][4] or len(sp_defeat) == 0 and len(sp_attack) != 0 and
                    self.GAME_TERRS[terr][4] < max([p[1] for p in sp_attack])):
               sp_attack.sort(key=lambda sp: sp[1])
               self.GAME_TERRS[terr][1] = sp_attack[-1][0]
       pprint.pprint(self.GAME_TERRS)

       for terr, params in results.items():
           for elem in params:
               self.COMMAND_POINTS[elem[0]] -= elem[1]

   def coloring(self):
       for terr, params in self.GAME_TERRS.items():
           if params[1] != "white":
               ImageDraw.floodfill(self.map1_image,
                                   TERRS[terr][0],
                                   COLORS[self.GAME_TERRS[terr][1]],
                                   border=None,
                                   thresh=5)
       self.map1_image.save("map_new.png")
       self.map1_image = Image.open("map_new.png").convert("RGBA")
       self.map1_photo = ImageTk.PhotoImage(self.map1_image)
       self.canvas1_image = self.map_canvas.create_image(50, 0, anchor='nw', image=self.map1_photo)

       self.map2_image = Image.open("map_2.png").convert("RGBA")
       self.map2_photo = ImageTk.PhotoImage(self.map2_image)
       self.canvas2_image = self.map_canvas.create_image(50, 0, anchor='nw', image=self.map2_photo)

       self.map3_image = Image.open("map_3.png").convert("RGBA")
       self.map3_photo = ImageTk.PhotoImage(self.map3_image)
       self.canvas3_image = self.map_canvas.create_image(50, 0, anchor='nw', image=self.map3_photo)

   def back_to_menu(self):
       self.quit_map()
       MainMenu()

   def quit_map(self):
       self.map_canvas.place_forget()
       self.btn_round_results.place_forget()
       self.btn_exit_map.place_forget()
       self.btn_new_commands.place_forget()
       self.btn_show_points.place_forget()
       self.map1_image = Image.open("map_1.png").convert("RGBA")
       self.map1_photo = ImageTk.PhotoImage(self.map1_image)
       self.canvas1_image = self.map_canvas.create_image(50, 0, anchor='nw', image=self.map1_photo)
       self.GAME_TERRS = TERRS
       self.COMMAND_POINTS = dict()
       self.comm_coll = dict()
       # self.canvas.destroy()
       # self.btn_round_results.destroy()
       # self.btn_exit_map.destroy()
       # self.btn_new_commands.destroy()
       # self.btn_show_points.destroy()

   def new_commands(self):
       self.commands_colors(self.amount_of_commands)
       self.start_painting(self.amount_of_commands)

   def show_points(self):
       stat.show_stats(self.COMMAND_POINTS)

   # !!!!!!!!!!!!!!!
   def round_results(self):
       self.current_round += 1
       RoundResults(self.amount_of_commands, self.current_round)

   # !!!!!!!!!!!!!!!

   def start_painting(self, amount_of_commands):
       k = 0
       for num, params in TERRS.items():
           if params[3] and k < amount_of_commands:
               ImageDraw.floodfill(self.map1_image, TERRS[num][0], COLORS[self.comm_coll[str(int(k) + 1)]],
                                   border=None,
                                   thresh=5)
               self.GAME_TERRS[num][1] = self.comm_coll[str(int(k) + 1)]
               k += 1
       pprint.pprint(self.GAME_TERRS)
       self.map1_image.save("map_new.png")
       self.map1_image = Image.open("map_new.png").convert("RGBA")
       self.map1_photo = ImageTk.PhotoImage(self.map1_image)
       self.canvas1_image = self.map_canvas.create_image(50, 0, anchor='nw', image=self.map1_photo)

       self.map2_image = Image.open("infoboy/map_2.png").convert("RGBA")
       self.map2_photo = ImageTk.PhotoImage(self.map2_image)
       self.canvas2_image = self.map_canvas.create_image(50, 0, anchor='nw', image=self.map2_photo)

       self.map3_image = Image.open("infoboy/map_3.png").convert("RGBA")
       self.map3_photo = ImageTk.PhotoImage(self.map3_image)
       self.canvas3_image = self.map_canvas.create_image(50, 0, anchor='nw', image=self.map3_photo)

   def commands_colors(self, amount_of_commands):
       for _col, _num in zip(sample(list(COLORS.keys()), amount_of_commands),
                             [i for i in range(1, amount_of_commands + 1)]):
           self.comm_coll[str(_num)] = _col
           self.COMMAND_POINTS[_col] = 0
       print(self.comm_coll)
       print(self.COMMAND_POINTS)


class RoundResults:
   def __init__(self, amount_of_commands, current_round):
       self.round_res = dict()
       self.command_count = 0
       self.correct_answer = dict()
       self.amount_of_commands = amount_of_commands
       self.check_var = tkinter.StringVar(value="off")
       self.results_window = customtkinter.CTkToplevel()
       self.results_window.geometry("800x400+500+300")
       self.results_window.title("Внести результаты раунда")
       self.results_window.iconbitmap('infoboy/infoboy.py')
       customtkinter.CTkLabel(master=self.results_window,
                              text=str(current_round + 1),
                              font=('Arial', 50, 'bold')).place(relx=0.05,
                                                                rely=0.1,
                                                                anchor=tkinter.CENTER)
       customtkinter.CTkLabel(master=self.results_window,
                              text="Внесите результаты раунда",
                              font=('Arial', 30, 'bold')).place(relx=0.5,
                                                                rely=0.05,
                                                                anchor=tkinter.CENTER)
       self.checkbox = customtkinter.CTkCheckBox(master=self.results_window,
                                                 text="Ответ на вопрос верен",
                                                 variable=self.check_var,
                                                 font=('Arial', 22, 'bold'),
                                                 onvalue="on",
                                                 offvalue="off")
       self.checkbox.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)
       customtkinter.CTkLabel(master=self.results_window, text="Номер территории",
                              font=('Arial', 22, 'bold')).place(relx=0.45, rely=0.4, anchor=tkinter.CENTER)
       customtkinter.CTkLabel(master=self.results_window, text="Распределение очков",
                              font=('Arial', 22, 'bold')).place(relx=0.8, rely=0.4, anchor=tkinter.CENTER)
       customtkinter.CTkLabel(master=self.results_window, text="Нападение:",
                              font=('Arial', 22, 'bold')).place(relx=0.1, rely=0.55, anchor=tkinter.W)
       customtkinter.CTkLabel(master=self.results_window, text="Защита:",
                              font=('Arial', 22, 'bold')).place(relx=0.1, rely=0.7, anchor=tkinter.W)
       customtkinter.CTkLabel(master=self.results_window, text="Название \nкоманды:",
                              font=('Arial', 22, 'bold')).place(relx=0.10, rely=0.9, anchor=tkinter.CENTER)
       self.number_attack = customtkinter.CTkEntry(master=self.results_window, width=200, font=('Arial', 22, 'bold'))
       self.number_defeat = customtkinter.CTkEntry(master=self.results_window, width=200, font=('Arial', 22, 'bold'))
       self.points_attack = customtkinter.CTkEntry(master=self.results_window, width=200, font=('Arial', 22, 'bold'))
       self.points_defeat = customtkinter.CTkEntry(master=self.results_window, width=200, font=('Arial', 22, 'bold'))
       self.command_name = customtkinter.CTkEntry(master=self.results_window, width=200, font=('Arial', 22, 'bold'))
       self.number_attack.place(relx=0.45, rely=0.55, anchor=tkinter.CENTER)
       self.number_defeat.place(relx=0.45, rely=0.7, anchor=tkinter.CENTER)
       self.points_attack.place(relx=0.8, rely=0.55, anchor=tkinter.CENTER)
       self.points_defeat.place(relx=0.8, rely=0.7, anchor=tkinter.CENTER)
       self.command_name.place(relx=0.35, rely=0.9, anchor=tkinter.CENTER)
       customtkinter.CTkButton(master=self.results_window,
                               text="Далее",
                               font=('Arial', 30, 'bold'),
                               border_width=2,
                               command=lambda: [self.entering_results(), self.change_command_count()]
                               if self.command_count < self.amount_of_commands else
                               self.results_window.destroy()).place(relx=0.7, rely=0.9, anchor=tkinter.CENTER)

   def change_command_count(self):
       self.command_count += 1

   def entering_results(self):
       if self.number_attack.get().strip() != '' and self.number_attack.get().strip() not in self.round_res:
           self.round_res[self.number_attack.get().strip()] = [
               [self.command_name.get().strip(), int(self.points_attack.get().strip()), "ATTACK", self.checkbox.get()]]
           self.correct_answer[self.command_name.get().strip()] = self.checkbox.get()
       else:
           self.round_res[self.number_attack.get().strip()].append(
               [self.command_name.get().strip(), int(self.points_attack.get().strip()), "ATTACK", self.checkbox.get()])
           self.correct_answer[self.command_name.get().strip()] = self.checkbox.get()
       if self.number_defeat.get().strip() != '' and self.number_defeat.get().strip() not in self.round_res:
           self.round_res[self.number_defeat.get().strip()] = [
               [self.command_name.get().strip(), int(self.points_defeat.get().strip()), "DEFEAT", self.checkbox.get()]]
           self.correct_answer[self.command_name.get().strip()] = self.checkbox.get()
       else:
           self.round_res[self.number_defeat.get().strip()].append(
               [self.command_name.get().strip(), int(self.points_defeat.get().strip()), "DEFEAT", self.checkbox.get()])
           self.correct_answer[self.command_name.get().strip()] = self.checkbox.get()
       self.number_defeat.delete(0, len(self.number_attack.get()))
       self.points_defeat.delete(0, len(self.points_defeat.get()))
       self.number_attack.delete(0, len(self.number_attack.get()))
       self.points_attack.delete(0, len(self.points_attack.get()))
       self.command_name.delete(0, len(self.command_name.get()))
       self.checkbox.deselect()
       if self.command_count == self.amount_of_commands - 1:
           self.results_window.destroy()
           mp.update_terrs(self.round_res, self.correct_answer)
           mp.coloring()


if __name__ == '__main__':
   root = customtkinter.CTk()
   root.geometry(str(WIDTH) + "x" + str(HEIGHT) + "+0+0")
   root.title('Инфобой v1.0')
   root.resizable(True, False)
   root.iconbitmap('infoboy/icon2.ico')

   stat = Statistics()
   mp = Map()
   main_menu = MainMenu()

   root.mainloop()
