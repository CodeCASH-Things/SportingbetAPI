import datetime
import time


class utils:
    def get_data(self):
        self.now = str(datetime.datetime.now().strftime("%d/%m/%Y"))
        self.nowtime = int(datetime.datetime.now().strftime("%H"))
        self.checknow = self.now

    def send_sinal(self):
        print("Sinal enviado...")
        self.bot.send_message(chat_id=self.user_id, text=(f'''
✔️ *ENTRADA CONFIRMADA!*
🚀 Apostar após: {self.result}x 
💢 Sair em: {self.alvo}x
🔁 Fazer {self.martingales} martingale
📱 Jogo: *{self.name}*
'''))
        return

    def alert(self):
        message_id = self.bot.send_message(
            self.user_id, text='''
    ⚠️ Vamos para o %iª GALE ⚠️
            ''' % (self.entrada_atual)).message_id
        self.message_ids = message_id
        self.message_delete = True
        return

    def alert_sinal(self):
        message_id = self.bot.send_message(
            self.user_id, text='''
⚠️ ANALISANDO, FIQUE ATENTO!!!
''').message_id
        self.message_ids = message_id
        self.message_delete = True
        return

    def delet(self):
        if self.message_delete == True:
            self.bot.delete_message(chat_id=self.user_id,
                                message_id=self.message_ids)
            self.message_delete = False

    def results(self):
        if self.win_results + self.loss_results != 0:
            a = 100 / (self.win_results + self.loss_results) * self.win_results
        else:
            a = 0

        self.win_hate = (f'{a:,.2f}%')
        self.bot.send_message(chat_id=self.user_id, text=(f'''
🧮 Placar geral:  {self.win_results} ✖️ {self.loss_results} 
🎯 {self.max_hate}ª Consecutiva.
    '''))
        return

    def restart(self):
        if self.now != self.checknow:
            print('Reload')
            self.bot.send_sticker(
                self.user_id, sticker='CAACAgEAAxkBAAEBbJJjXNcB92-_4vp2v0B3Plp9FONrDwACvgEAAsFWwUVjxQN4wmmSBCoE')
            utils.get_data(self)
            self.checknowtime = self.nowtime
            utils.results(self)

            self.win_results = 0
            self.loss_results = 0
            self.max_hate = 0

            time.sleep(10)
            self.bot.send_sticker(
                self.user_id, sticker='CAACAgEAAxkBAAEBPQZi-ziImRgbjqbDkPduogMKzv0zFgACbAQAAl4ByUUIjW-sdJsr6CkE')
            utils.get_data(self)
            self.checknowtime = self.nowtime
            utils.results(self)
            return True
        else:
            return False

    def reset(self):
        self.analise_open = 0
        self.analisar = 0
        self.entrada_atual = 0

        if not utils.restart(self):
            utils.results(self)
        return

    def martingale(self):

        if self.result >= self.alvo:
            self.win_results += 1
            self.max_hate += 1
            self.bot.send_message(chat_id=self.user_id, text=(f'''
✅✅✅ GREEN {self.result}x ✅✅✅'''))

        elif self.entrada_atual < self.martingales:
            self.entrada_atual += 1
            self.message_ids = self.bot.send_message(chat_id=self.user_id, text=(f'''
⚠️ Vamos para  o {self.entrada_atual}ª Martingale.''')).message_id
            self.message_delete = True
            return

        else:
            self.loss_results += 1
            self.max_hate = 0
            self.bot.send_message(chat_id=self.user_id, text=(f'''
🚫 LOSS {self.result}x'''))
        
        utils.reset(self)
    
    def estrategy(self, finalnum):
        if self.analisar == 1:
            self.result = finalnum[0]
            utils.martingale(self)
            return
        
        elif self.analisar == 0:
            if finalnum[0] >= 0.0:
                self.analisar = 1
                self.result = finalnum[0]
                utils.send_sinal(self)
                return
            
            if finalnum[0] <= 1.5 and finalnum[1] <= 1.5 and finalnum[2] <= 1.5:
                self.analisar = 1
                self.result = finalnum[0]
                utils.send_sinal(self)
                return
            
            if finalnum[0] <= 2 and finalnum[1] <= 2 and finalnum[2] <= 2:
                self.analisar = 1
                self.result = finalnum[0]
                utils.send_sinal(self)
                return



