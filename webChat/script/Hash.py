import hashlib

def hash(passwd)->str:
    """
    文字列をハッシュ化して返す
    """
    return hashlib.sha512(passwd.encode("utf-8")).hexdigest()

