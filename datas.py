import sqlite3



tbase = sqlite3.connect('vis.db')
tc = tbase.cursor()


def state_0(userid,balance):
    with tbase:
        tc.execute('INSERT OR IGNORE INTO users(userid,balance) VALUES(?, ?)', (userid,balance,))




def state_5(userid, scale, safety, safety_balance, date):
    with tbase:
        tc.execute('INSERT OR IGNORE INTO settings(userid, scale, safety, safety_balance, date) VALUES(?, ?, ?, ?, ?)', (userid,scale,safety,safety_balance,date,))






def state_6(userid):
    with tbase:
        tc.execute('UPDATE settings SET scale = scale + 0.5 WHERE userid = ?', (userid,))

def state_666(userid):
    with tbase:
        tc.execute('UPDATE settings SET scale = scale - 0.5 WHERE userid = ?', (userid,))

def state_safety(userid, yes):
    with tbase:
        tc.execute('UPDATE settings SET safety = ? WHERE userid = ?', (yes,userid,))

def state_safetys(userid, no):
    with tbase:
        tc.execute('UPDATE settings SET safety = ? WHERE userid = ?', (no,userid,))





def state_safets(date,safety_balance, userid):
    with tbase:
        tc.execute('UPDATE settings SET date = ?, safety_balance = ? WHERE userid = ?', (date,safety_balance,userid,))

def state_565(balance,userid):
    with tbase:
        tc.execute('UPDATE users SET balance = balance + ? WHERE userid = ?', (balance,userid,))

def state_55555(msgids,rands):
    with tbase:
        tc.execute('INSERT INTO targets(msgids,rands) VALUES(?, ?)', (msgids,rands,))

def state_deletes(rands):
    with tbase:
        tc.execute('DELETE FROM targets WHERE msgids = ?', (rands,))

def state_tryttttt(userid):
    with tbase:
        tc.execute('UPDATE users SET try_text_balance = try_text_balance - 1 WHERE userid = ?', (userid,))

def state_tryttttt_(userid):
    with tbase:
        tc.execute('UPDATE users SET try_balance = try_balance - 1 WHERE userid = ?', (userid,))







def tests():
    with tbase:
        s = tc.execute('SELECT * FROM settings').fetchall()
        print(s)

def state_times(useri):
    with tbase:
        tc.execute('UPDATE users SET try_balance = 19 WHERE userid = ?', (useri,))

def state_times_safety(useri):
    with tbase:
        tc.execute('UPDATE settings SET safety_balance = 0 WHERE userid = ?', (useri,))


def state_nudify(useri):
    with tbase:
        tc.execute('UPDATE users SET nudify_content = 5 WHERE userid = ?', (useri,))

def state_nudify_(useri):
    with tbase:
        tc.execute('UPDATE users SET nudify_content = nudify_content - 1 WHERE userid = ?', (useri,))

def state_pic_balance(userid):
    with tbase:
        tc.execute('UPDATE users SET try_pic_balance = try_pic_balance - 1 WHERE userid = ?', (userid,))





def state_balance_99(userid):
    with tbase:
        tc.execute('UPDATE users SET balance_99 = 0 WHERE userid = ?', (userid,))







def state_15(userid):
    with tbase:
        tc.execute('UPDATE users SET try_balance = try_balance + 15 WHERE userid = ?', (userid,))