
from sqlalchemy import *
import os
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *
_get = os.environ.get

def start() -> scoped_session:
  
    dburl = _get("CLEARDB_DATABASE_URL")
    engine = create_engine(dburl)
    infb.metadata.bind = engine
    infb.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


infb = declarative_base()
SESSION = start()


class Pdb(infb):
    __tablename__ = "pdb"
    id = Column(Integer, primary_key=True)
    infx = Column(String(14))
    var = Column(String(14))
    value = Column(UnicodeText)

    def __init__(self, infx, var, value):
        self.infx = str(infx)
        self.var = str(var)
        self.value = value


class BotUsers(infb):
    __tablename__ = "botusers"
    infx_id = Column(String(14), primary_key=True)

    def __init__(self, infx_id):
        self.infx_id = infx_id


class infxChats(infb):
    __tablename__ = "infxTg"
    infx_id = Column(String(14), primary_key=True)

    def __init__(self, infx_id):
        self.infx_id = infx_id


class GMute(infb):
    __tablename__ = "gmute"
    infx = Column(String(14), primary_key=True)
    sender = Column(String(14), primary_key=True)

    def __init__(self, infx, sender):
        self.infx = str(infx)
        self.sender = str(sender)


class GBan(infb):
    __tablename__ = "gban"
    infx = Column(String(14), primary_key=True)
    sender = Column(String(14), primary_key=True)
    reason = Column(UnicodeText)

    def __init__(self, infx, sender, reason=""):
        self.infx = str(infx)
        self.sender = str(sender)
        self.reason = reason


class Mute(infb):
    __tablename__ = "mute"
    infx = Column(String(14), primary_key=True)
    sender = Column(String(14), primary_key=True)
    chat_id = Column(String(14), primary_key=True)
    

    def __init__(self, infx, sender, chat_id):
        self.infx = str(infx)
        self.sender = str(sender)
        self.chat_id = str(chat_id)
        


class Notes(infb):
    __tablename__ = "notes"
    infx = Column(String(14), primary_key=True)
    chat_id = Column(String(14), primary_key=True)
    keyword = Column(String(255), primary_key=True)
    reply = Column(UnicodeText)
    f_mesg_id = Column(Numeric)
    
    def __init__(self, infx, chat_id, keyword, reply, f_mesg_id):
        self.infx = str(infx)
        self.chat_id = str(chat_id)
        self.keyword = keyword
        self.reply = reply
        self.f_mesg_id = f_mesg_id


class PMPermit(infb):
    __tablename__ = "pmpermit"
    id = Column(Integer, primary_key=True)
    infx = Column(String(14))
    chat_id = Column(String(14))
    reason = Column(String(127))

    def __init__(self, infx, chat_id, reason=""):
        self.infx = str(infx)
        self.chat_id = chat_id
        self.reason = reason
        


class Welcome(infb):
    __tablename__ = "welcome"
    infx = Column(String(14), primary_key=True)
    chat_id = Column(String(14), primary_key=True)
    cust_wc = Column(UnicodeText)
    cl_wc = Column(Boolean, default=False)
    prev_wc = Column(BigInteger)
    mf_id = Column(UnicodeText)

    def __init__(self, infx, chat_id, cust_wc, cl_wc, prev_wc, mf_id=None):
        self.infx = str(infx)
        self.chat_id = chat_id
        self.cust_wc = cust_wc
        self.cl_wc = cl_wc
        self.prev_wc = prev_wc
        self.mf_id = mf_id

class Filters(infb):
    __tablename__ = "filters"
    id = Column(Integer, primary_key=True)
    infx = Column(String(14))
    chat_id = Column(String(14))
    keyword = Column(UnicodeText)
    reply = Column(UnicodeText)
    snip_type = Column(Numeric)
    media_id = Column(UnicodeText)
    media_access_hash = Column(UnicodeText)
    media_file_reference = Column(LargeBinary)

    def __init__(
        self,
        infx, 
        chat_id,
        keyword, reply, snip_type,
        media_id=None, media_access_hash=None, media_file_reference=None
    ):
        self.infx = infx
        self.chat_id = chat_id
        self.keyword = keyword
        self.reply = reply
        self.snip_type = snip_type
        self.media_id = media_id
        self.media_access_hash = media_access_hash
        self.media_file_reference = media_file_reference

class Locks(infb):
    __tablename__ = "locks"
    infx = Column(String(14), primary_key=True)
    chat_id = Column(String(14), primary_key=True)
    # Booleans are for "is this locked", _NOT_ "is this allowed"
    bots = Column(Boolean, default=False)
    commands = Column(Boolean, default=False)
    email = Column(Boolean, default=False)
    forward = Column(Boolean, default=False)
    url = Column(Boolean, default=False)


    def __init__(self, infx, chat_id):
        self.infx = str(infx) # ensure string
        self.chat_id = str(chat_id)  # ensure string  
        self.bots = False
        self.commands = False
        self.email = False
        self.forward = False
        self.url = False


Pdb.__table__.create(checkfirst=True)
Mute.__table__.create(checkfirst=True)
BotUsers.__table__.create(checkfirst=True)
infxChats.__table__.create(checkfirst=True)
GMute.__table__.create(checkfirst=True)
GBan.__table__.create(checkfirst=True)
Notes.__table__.create(checkfirst=True)
PMPermit.__table__.create(checkfirst=True)
Welcome.__table__.create(checkfirst=True)
Filters.__table__.create(checkfirst=True)
Locks.__table__.create(checkfirst=True)

def pget(infx, var):
    try:
        return SESSION.query(Pdb).filter(
            Pdb.infx == str(infx),
            Pdb.var == str(var)).first().value
    except BaseException:
        return None
    finally:
        SESSION.close()


def pset(infx, var, value):
    if SESSION.query(Pdb).filter(
            Pdb.infx == str(infx),
            Pdb.var == str(var)).one_or_none():
        pdel(infx, var)
    adder = Pdb(str(infx), str(var), value)
    SESSION.add(adder)
    SESSION.commit()


def pdel(infx, var):
    rem = SESSION.query(Pdb).filter(
        Pdb.infx == str(infx),
        Pdb.var == str(var)).delete(
        synchronize_session="fetch")
    if rem:
        SESSION.commit()


def add_welcome(infx, chat_id, cust_wc, cl_wc, prev_wc, mf_id):
    add_wc = Welcome(infx, chat_id, cust_wc, cl_wc, prev_wc, mf_id)
    SESSION.add(add_wc)
    SESSION.commit()


def remove_welcome(infx, chat_id):
    rm_wc = SESSION.query(Welcome).get((str(infx), str(chat_id)))
    if rm_wc:
        SESSION.delete(rm_wc)
        SESSION.commit()


def upd_prev_welcome(infx, chat_id, prev_wc):
    _update = SESSION.query(Welcome).get((str(infx), str(chat_id)))
    _update.prev_wc = prev_wc
    SESSION.commit()


def get_welcome(infx, chat_id):
    try:
        return SESSION.query(Welcome).get((str(infx), str(chat_id)))
    except Exception as e:
        infxlog.error(str(e))
        return
    finally:
        SESSION.close()


def clean_welcome(infx, chat_id, cl_wc):
    clnn = SESSION.query(Welcome).get((str(infx), str(chat_id)))
    clnn.cl_wc = cl_wc
    SESSION.commit()


def approve(infx, chat_id, reason):
    adder = PMPermit(str(infx), str(chat_id), str(reason))
    SESSION.add(adder)
    SESSION.commit()


def disapprove(infx, chat_id):
    rem = SESSION.query(PMPermit).get((str(infx), str(chat_id)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def get_all_approved(infx):
    rem = SESSION.query(PMPermit).filter(PMPermit.infx == infx).all()
    SESSION.close()
    return rem


def is_approved(infx, chat_id):
    try:
        return SESSION.query(PMPermit).filter(
            PMPermit.infx == str(infx),
            PMPermit.chat_id == str(chat_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def get_note(infx, chat_id, keyword):
    try:
        return SESSION.query(Notes).get((str(infx), str(chat_id), keyword))
    finally:
        SESSION.close()


def get_notes(infx, chat_id):
    try:
        return SESSION.query(Notes).filter(
            Notes.infx == str(infx),
            Notes.chat_id == str(chat_id)).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def add_note(infx, chat_id, keyword, reply, f_mesg_id):
    to_check = get_note(infx, chat_id, keyword)
    if not to_check:
        adder = Notes(str(infx), str(chat_id), keyword, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return True
    else:
        rem = SESSION.query(Notes).get((str(infx), str(chat_id), keyword))
        SESSION.delete(rem)
        SESSION.commit()
        adder = Notes(str(infx), str(chat_id), keyword, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return False


def rm_note(infx, chat_id, keyword):
    to_check = get_note(infx, chat_id, keyword)
    if not to_check:
        return False
    else:
        rem = SESSION.query(Notes).get((str(infx), str(chat_id), keyword))
        SESSION.delete(rem)
        SESSION.commit()
        return True


def is_muted(infx, sender, chat_id):
    user = SESSION.query(Mute).get((str(infx), str(sender), str(chat_id)))
    if user:
        return True
    else:
        return False


def mute(infx, sender, chat_id):
    adder = Mute(str(infx), str(sender), str(chat_id))
    SESSION.add(adder)
    SESSION.commit()


def unmute(infx, sender, chat_id):
    rem = SESSION.query(Mute).get((str(infx), str(sender), str(chat_id)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def get_all_muted(infx):
    rem = SESSION.query(Mute).filter(Notes.infx == infx).all()
    SESSION.close()
    return rem


def is_gbanned(infx, sender):
    try:
        _infxG = SESSION.query(GBan).get((str(infx), str(sender)))
        if _infxG:
            return str(_infxG.reason)
    finally:
        SESSION.close()


def gban(infx, sender, reason):
    adder = GBan(str(infx), str(sender), str(reason))
    SESSION.add(adder)
    SESSION.commit()


def ungban(infx, sender, infx_id):
    rem = SESSION.query(GBan).get((str(infx), str(sender)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def is_gmuted(sender):
    try:
        return SESSION.query(GMute).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def gmute(infx, sender):
    adder = GMute(str(infx), str(sender))
    SESSION.add(adder)
    SESSION.commit()


def ungmute(infx, sender):
    rem = SESSION.query(GMute).get((str(infx), str(sender)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def add_infx(infx_id):
    infx = infxChats(str(infx_id))
    SESSION.add(infx)
    SESSION.commit()


def is_infx_exist(infx_id):
    try:
        infx = SESSION.query(infxChats).filter(
            infxChats.infx_id == str(infx_id)).one()
        if infx:
            return True
    except BaseException:
        return None
    finally:
        SESSION.close()


def get_infx_chats():
    try:
        infx = SESSION.query(infxChats).all()
        if infx:
            return infx
    except BaseException:
        return None
    finally:
        SESSION.close()


def add_user(infx_id: int):
    infx = BotUsers(str(infx_id))
    SESSION.add(infx)
    SESSION.commit()


def is_user_exist(infx_id):
    try:
        infx = SESSION.query(BotUsers).filter(
            BotUsers.infx_id == str(infx_id)).one()
        if infx:
            return True
    except BaseException:
        return None
    finally:
        SESSION.close()


def get_added_users():
    infx = SESSION.query(BotUsers).all()
    SESSION.close()
    return infx

def get_filter(infx, chat_id, keyword):
    try:
        return SESSION.query(Filters).get((str(infx), str(chat_id), keyword))
    except:
        return None
    finally:
        SESSION.close()


def get_all_filters(infx, chat_id):
    try:
        return SESSION.query(Filters).filter(Filters.infx == str(infx), Filters.chat_id == str(chat_id)).all()
    except:
        return None
    finally:
        SESSION.close()


def add_filter(infx, chat_id, keyword, reply, snip_type, media_id, media_access_hash, media_file_reference):
    adder = SESSION.query(Filters).get((str(infx), str(chat_id), keyword))
    if adder:
        adder.reply = reply
        adder.snip_type = snip_type
        adder.media_id = media_id
        adder.media_access_hash = media_access_hash
        adder.media_file_reference = media_file_reference
    else:
        adder = Filters(infx, chat_id, keyword, reply, snip_type, media_id,
                        media_access_hash, media_file_reference)
    SESSION.add(adder)
    SESSION.commit()


def remove_filter(infx, chat_id, keyword):
    saved_filter = SESSION.query(Filters).get((str(infx), str(chat_id), keyword))
    if saved_filter:
        SESSION.delete(saved_filter)
        SESSION.commit()


def remove_all_filters(chat_id):
    saved_filter = SESSION.query(Filters).filter(Filters.infx == str(infx), Filters.chat_id == str(chat_id))
    if saved_filter:
        saved_filter.delete()
        SESSION.commit()

def init_locks(infx, chat_id, reset=False):
    curr_restr = SESSION.query(Locks).get(str(infx), str(chat_id))
    if reset:
        SESSION.delete(curr_restr)
        SESSION.flush()
    restr = Locks(str(infx), str(chat_id))
    SESSION.add(restr)
    SESSION.commit()
    return restr


def update_lock(infx, chat_id, lock_type, locked):
    curr_perm = SESSION.query(Locks).get((str(infx), str(chat_id)))
    if not curr_perm:
        curr_perm = init_locks(infx, chat_id)
    if lock_type == "bots":
        curr_perm.bots = locked
    elif lock_type == "commands":
        curr_perm.commands = locked
    elif lock_type == "email":
        curr_perm.email = locked
    elif lock_type == "forward":
        curr_perm.forward = locked
    elif lock_type == "url":
        curr_perm.url = locked
    SESSION.add(curr_perm)
    SESSION.commit()


def is_locked(infx, chat_id, lock_type):
    curr_perm = SESSION.query(Locks).get((str(infx), str(chat_id)))
    SESSION.close()
    if not curr_perm:
        return False
    elif lock_type == "bots":
        return curr_perm.bots
    elif lock_type == "commands":
        return curr_perm.commands
    elif lock_type == "email":
        return curr_perm.email
    elif lock_type == "forward":
        return curr_perm.forward
    elif lock_type == "url":
        return curr_perm.url


def get_locks(infx, chat_id):
    try:
        return SESSION.query(Locks).get((str(infx), str(chat_id)))
    finally:
        SESSION.close()

class pdb(object):
    Asudo=Bsudo=Csudo=Dsudo=Osudo=None
    Api_id = _get("Api_id")
    Api_hash = _get("Api_hash")
    Bf_uname = _get("Bot_username")
    Omega = _get("Bot_token")
    Alpha = pget("alpha", "session")
    Beta = pget("beta", "session")
    Gaama = pget("gaama", "session")
    Delta = pget("delta", "session")
    Asstt = pget("omega", "assistant")
    Botlog_chat = int(_get("Botlog_chat"))
    Ytapi = pget("omega", "ytapi")
    Gdtoken = pget("omega", "gdtoken")
    if pget("alpha", "sudo"): Asudo = pget("alpha", "sudo")
    if pget("beta", "sudo"): Bsudo = pget("beta", "sudo")
    if pget("gaama", "sudo"): Csudo = pget("gaama", "sudo")
    if pget("delta", "sudo"): Dsudo = pget("delta", "sudo")
    if pget("omega", "sudo"): Osudo = pget("omega", "sudo")
    Dldir="./User_Drive"
    
