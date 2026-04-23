import tkinter as tk
from tkinter import ttk
from PIL import Image
import urllib.request
import os

def main():
    app = Application()
    app.mainloop()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("hololive OCG Stream Overlay")

        player1_lbl = tk.Label(self, text="Player 1", height=2)
        player1_lbl.grid(row=0, column=0)
        player1_frame = Player(self, player_side="left")
        player1_frame.grid(row=1, column=0)

        player2_lbl = tk.Label(self, text="Player 2", height=2)
        player2_lbl.grid(row=0, column=1)
        player2_frame = Player(self, player_side="right")
        player2_frame.grid(row=1, column=1)

        # New Game
        self.new_game_btn = tk.Button(self, text="New Game", command=lambda: [player1_frame.new_game(), player2_frame.new_game()], height=2)
        self.new_game_btn.grid(row=2, column=0, columnspan=2, sticky="ew")

class Player(ttk.Frame):
    life = 5
    holopower = 0

    def __init__(self, parent, player_side):
        super().__init__(parent)

        self.player_side = player_side

        # Player Key Card 01
        self.lbl_key_card_01 = ttk.Label(self, text="Input Key Card 01 ID (e.g. hBP02-013)")
        self.lbl_key_card_01.grid(row=0, column=0)
        self.entry_key_card_01 = ttk.Entry(self)
        self.entry_key_card_01.grid(row=0, column=1, columnspan=2)
        self.entry_key_card_01.bind("<Return>", self.save_key_card_01)
        self.entry_btn_key_card_01 = ttk.Button(self, text="Load Key Card 01", command=self.save_key_card_01)
        self.entry_btn_key_card_01.grid(row=0, column=3, columnspan=2, sticky="ew")

        # Player Key Card 02
        self.lbl_key_card_02 = ttk.Label(self, text="Input Key Card 02 ID (e.g. hBP02-027)")
        self.lbl_key_card_02.grid(row=1, column=0)
        self.entry_key_card_02 = ttk.Entry(self)
        self.entry_key_card_02.grid(row=1, column=1, columnspan=2)
        self.entry_key_card_02.bind("<Return>", self.save_key_card_02)
        self.entry_btn_key_card_02 = ttk.Button(self, text="Load Key Card 02", command=self.save_key_card_02)
        self.entry_btn_key_card_02.grid(row=1, column=3, sticky="ew")

        # Player Oshi
        self.lbl_oshi = ttk.Label(self, text="Input Oshi Card ID (e.g. hBP02-001)")
        self.lbl_oshi.grid(row=2, column=0)
        self.entry_oshi = ttk.Entry(self)
        self.entry_oshi.grid(row=2, column=1, columnspan=2)
        self.entry_oshi.bind("<Return>", self.save_oshi)
        self.entry_btn_oshi = ttk.Button(self, text="Load Oshi", command=self.save_oshi)
        self.entry_btn_oshi.grid(row=2, column=3, sticky="ew")

        # Add 1 Life
        self.entry_btn_add_life = tk.Button(self, text="+1 Life", command=self.add_life, height=2, width=30)
        self.entry_btn_add_life.grid(row=3, column=0, columnspan=2, sticky="ew")

        # Lose 1 Life
        self.entry_btn_lose_life = tk.Button(self, text="-1 Life", command=self.lose_life, height=2, width=30)
        self.entry_btn_lose_life.grid(row=4, column=0, columnspan=2, sticky="ew")

        # Add 1 holo Power
        self.entry_btn_add_hp = tk.Button(self, text="+1 holo Power", command=self.add_hp, height=2, width=30)
        self.entry_btn_add_hp.grid(row=3, column=2, columnspan=2, sticky="ew")

        # Subtract 1 holo Power
        self.entry_btn_remove_hp = tk.Button(self, text="-1 holo Power", command=self.remove_hp, height=2, width=30)
        self.entry_btn_remove_hp.grid(row=4, column=2, columnspan=2, sticky="ew")

        # Toggle SP Skill Marker
        self.entry_btn_sp_skill = tk.Button(self, text="SP Oshi Skill Toggle", command=self.toggle_sp, height=2)
        self.entry_btn_sp_skill.grid(row=7, column=0, columnspan=4, sticky="ew")

        # Creating the Image for the Stream Overlay
        # Size and BG
        self.canvas = tk.Canvas(self, bg="#ffffff", width=698, height=254)
        self.background = tk.PhotoImage(file=f"./Images/player_{self.player_side}/bg.png")
        self.playerbg = self.canvas.create_image(0, 0, anchor="nw", image=self.background)
        # Place default cards
        self.set_oshi = tk.PhotoImage(file="./Images/default_oshi.png")
        self.playersetoshi = self.canvas.create_image(0, 6, anchor="nw", image=self.set_oshi)
        self.set_key_card_01 = tk.PhotoImage(file="./Images/default_key_card.png")
        self.playersetkey_01 = self.canvas.create_image(172, 101, anchor="nw", image=self.set_key_card_01)
        self.set_key_card_02 = tk.PhotoImage(file="./Images/default_key_card.png")
        self.playersetkey_02 = self.canvas.create_image(122, 143, anchor="nw", image=self.set_key_card_02)
        # Set starting life
        self.life_img = tk.PhotoImage(file=f"./Images/player_{self.player_side}/life_0{self.life}.png")
        self.set_life = self.canvas.create_image(0, 0, anchor="nw", image=self.life_img)
        # Place SP Skill Marker
        self.sp_marker = tk.PhotoImage(file=f"./Images/player_{self.player_side}/sp_marker.png")
        self.set_sp_marker = self.canvas.create_image(0, 0, anchor="nw", image=self.sp_marker)
        # Place holo Power Counter
        self.holopower_img = tk.PhotoImage(file=f"./Images/player_{self.player_side}/hp_00.png")
        self.set_holopower = self.canvas.create_image(0, 0, anchor="nw", image=self.holopower_img)
        # Place Outlines on top
        self.outlines = tk.PhotoImage(file=f"./Images/player_{self.player_side}/outlines.png")
        self.set_outlines = self.canvas.create_image(0, 0, anchor="nw", image=self.outlines)
        # Finish Canvas
        self.canvas.grid(row=8, column=0, columnspan=4)

    def save_oshi(self, event=None):
        try:
            card_code = str(self.entry_oshi.get())

            if len(card_code) > 0:
                card_code = f"{card_code[0].lower()}{card_code[1:3].upper()}{card_code[3:5]}-{card_code[6:9]}"
                set_code = str(card_code[:5])
                set_id = str(card_code[3:5])

                osr_card = f"https://hololive-official-cardgame.com/wp-content/images/cardlist/{set_code}/{card_code}_OSR.png"
                oc_card = f"https://hololive-official-cardgame.com/wp-content/images/cardlist/{set_code}/{card_code}_OC.png"
                pr_card = f"https://hololive-official-cardgame.com/wp-content/images/cardlist/hPR/{card_code}_P.png"
                hy_url = f"https://hololive-official-cardgame.com/wp-content/images/cardlist/hY{set_id}/{card_code}_OC.png"

                list_of_urls = []
                list_of_urls.extend((osr_card, oc_card, hy_url, pr_card))

                for url in list_of_urls:
                    try:
                        urllib.request.urlretrieve(url, f"./Images/player_{self.player_side}.png")
                        break
                    except:
                        continue

                # Grab Oshi Color for BG
                card = Image.open(f"./Images/player_{self.player_side}.png").convert("RGBA").resize((400, 559))
                color = card.getpixel((384, 518))
                rgb = color[0:3]
                def from_rgb(rgb):
                    """translates a rgb tuple of int to a tkinter friendly color code
                    """
                    return "#%02x%02x%02x" % rgb
                self.canvas.configure(bg=from_rgb(rgb))

                # Apply Mask and save Oshi
                card = Image.open(f"./Images/player_{self.player_side}.png").convert("RGBA").resize((245, 342))
                mask = Image.open("./Images/Oshi_Card_Mask.png").convert("L").resize((245, 342))
                card_rgba = card.copy()
                card_rgba.putalpha(mask)
                card_rgba.save(f"./Images/player_{self.player_side}/player_{self.player_side}_oshi.png")
                os.remove(f"./Images/player_{self.player_side}.png")

                self.oshi_img = tk.PhotoImage(file=f"./Images/player_{self.player_side}/player_{self.player_side}_oshi.png")
                self.canvas.imgref = self.oshi_img
                self.canvas.itemconfig(self.playersetoshi, image=self.oshi_img)

        except:
            self.oshi_img = tk.PhotoImage(file="./Images/default_oshi.png")
            self.canvas.imgref = self.oshi_img
            self.canvas.itemconfig(self.playersetoshi, image=self.oshi_img)

    def save_key_card_01(self, event=None):
        try:
            card_code = str(self.entry_key_card_01.get())

            if len(card_code) > 0:
                card_code = f"{card_code[0].lower()}{card_code[1:3].upper()}{card_code[3:5]}-{card_code[6:9]}"
                set_code = str(card_code[:5])
                set_id = str(card_code[3:5])

                rr_card = f"https://hololive-official-cardgame.com/wp-content/images/cardlist/{set_code}/{card_code}_RR.png"
                r_card = f"https://hololive-official-cardgame.com/wp-content/images/cardlist/{set_code}/{card_code}_R.png"
                u_card = f"https://hololive-official-cardgame.com/wp-content/images/cardlist/{set_code}/{card_code}_U.png"
                c_card = f"https://hololive-official-cardgame.com/wp-content/images/cardlist/{set_code}/{card_code}_C.png"

                list_of_urls = []
                list_of_urls.extend((rr_card, r_card, u_card, c_card))

                for url in list_of_urls:
                    try:
                        urllib.request.urlretrieve(url, f"./Images/player_{self.player_side}.png")
                        break
                    except:
                        continue

                card = Image.open(f"./Images/player_{self.player_side}.png").convert("RGBA").resize((65, 90))
                card = card.rotate(10, expand=True)
                card.save(f"./Images/player_{self.player_side}/player_{self.player_side}_key_01.png")
                os.remove(f"./Images/player_{self.player_side}.png")

                self.key_01_img = tk.PhotoImage(file=f"./Images/player_{self.player_side}/player_{self.player_side}_key_01.png")
                self.canvas.imgref = self.key_01_img
                self.canvas.itemconfig(self.playersetkey_01, image=self.key_01_img)

        except:
            self.key_01_img = tk.PhotoImage(file="./Images/default_key_card.png")
            self.canvas.imgref = self.key_01_img
            self.canvas.itemconfig(self.playersetkey_01, image=self.key_01_img)

    def save_key_card_02(self, event=None):
        try:
            card_code = str(self.entry_key_card_02.get())

            if len(card_code) > 0:
                card_code = f"{card_code[0].lower()}{card_code[1:3].upper()}{card_code[3:5]}-{card_code[6:9]}"
                set_code = str(card_code[:5])
                set_id = str(card_code[3:5])

                rr_card = f"https://hololive-official-cardgame.com/wp-content/images/cardlist/{set_code}/{card_code}_RR.png"
                r_card = f"https://hololive-official-cardgame.com/wp-content/images/cardlist/{set_code}/{card_code}_R.png"
                u_card = f"https://hololive-official-cardgame.com/wp-content/images/cardlist/{set_code}/{card_code}_U.png"
                c_card = f"https://hololive-official-cardgame.com/wp-content/images/cardlist/{set_code}/{card_code}_C.png"

                list_of_urls = []
                list_of_urls.extend((rr_card, r_card, u_card, c_card))

                for url in list_of_urls:
                    try:
                        urllib.request.urlretrieve(url, f"./Images/player_{self.player_side}.png")
                        break
                    except:
                        continue

                card = Image.open(f"./Images/player_{self.player_side}.png").convert("RGBA").resize((65, 90))
                card = card.rotate(10, expand=True)
                card.save(f"./Images/player_{self.player_side}/player_{self.player_side}_key_02.png")
                os.remove(f"./Images/player_{self.player_side}.png")

                self.key_02_img = tk.PhotoImage(file=f"./Images/player_{self.player_side}/player_{self.player_side}_key_02.png")
                self.canvas.imgref = self.key_02_img
                self.canvas.itemconfig(self.playersetkey_02, image=self.key_02_img)

        except:
            self.key_02_img = tk.PhotoImage(file="./Images/default_key_card.png")
            self.canvas.imgref = self.key_02_img
            self.canvas.itemconfig(self.playersetkey_02, image=self.key_02_img)

    def add_life(self):
        self.life += 1
        if self.life > 6:
            self.life = 6
        self.new_img_life = tk.PhotoImage(file=f"./Images/player_{self.player_side}/life_0{self.life}.png")
        self.canvas.imgref = self.new_img_life
        self.canvas.itemconfig(self.set_life, image=self.new_img_life)

    def lose_life(self):
        self.life -= 1
        if self.life < 0:
            self.life = 0
        self.new_img_life = tk.PhotoImage(file=f"./Images/player_{self.player_side}/life_0{self.life}.png")
        self.canvas.imgref = self.new_img_life
        self.canvas.itemconfig(self.set_life, image=self.new_img_life)

    def add_hp(self):
        self.holopower += 1
        if self.holopower > 9:
            self.holopower = 9
        self.new_img_hp = tk.PhotoImage(file=f"./Images/player_{self.player_side}/hp_0{self.holopower}.png")
        self.canvas.imgref = self.new_img_hp
        self.canvas.itemconfig(self.set_holopower, image=self.new_img_hp)

    def remove_hp(self):
        self.holopower -= 1
        if self.holopower < 0:
            self.holopower = 0
        self.new_img_hp = tk.PhotoImage(file=f"./Images/player_{self.player_side}/hp_0{self.holopower}.png")
        self.canvas.imgref = self.new_img_hp
        self.canvas.itemconfig(self.set_holopower, image=self.new_img_hp)

    def toggle_sp(self):
        state = self.canvas.itemcget(self.set_sp_marker, 'state')
        if state == "hidden":
            self.canvas.itemconfig(self.set_sp_marker, state="normal")
        else:
            self.canvas.itemconfig(self.set_sp_marker, state="hidden")

    def new_game(self):
        # Set SP SKill to default
        self.canvas.itemconfig(self.set_sp_marker, state="normal")
        # Set starting life
        self.life = 5
        self.reset_img_life = tk.PhotoImage(file=f"./Images/player_{self.player_side}/life_0{self.life}.png")
        self.canvas.imgref = self.reset_img_life
        self.canvas.itemconfig(self.set_life, image=self.reset_img_life)
        # Set starting holo Power
        self.holopower = 0
        self.reset_img_hp = tk.PhotoImage(file=f"./Images/player_{self.player_side}/hp_0{self.holopower}.png")
        self.canvas.imgref = self.reset_img_hp
        self.canvas.itemconfig(self.set_holopower, image=self.reset_img_hp)

if __name__ == "__main__":
    main()
