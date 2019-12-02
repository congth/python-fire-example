import fire

def hello(name = "World"):
    return "Xin chao %s!" % name

if __name__ == '__main__':
    fire.Fire(hello)
