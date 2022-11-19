from argon2 import PasswordHasher

ph=PasswordHasher(time_cost=3, # number of iterations
    memory_cost=64 * 1024, # 64mb
    parallelism=4, # how many parallel threads to use
    hash_len=32, # the size of the derived key
    salt_len=16)

def pwd_hshr(pwd):
    #hashing password(making it unreadable) 
    hash=ph.hash(pwd)
    return hash

def check(hash,pwd):
    try:
        ver=ph.verify(hash,pwd)
        if ver:
            return 1
    except:
        return 0
