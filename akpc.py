import os as s
def close():
    """This shutdown your computer in ten seconds"""
    s.system("shutdown -s -t 10")
def cancel():
    """This cancel your computer shutdown"""
    s.system("shutdown -a")
