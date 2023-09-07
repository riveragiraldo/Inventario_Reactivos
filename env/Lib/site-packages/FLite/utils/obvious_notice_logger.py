import logging
import os

class noticelogger(object):
    def __init__(self):
        # 获取当前目录下的banner.txt文件
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                            filename='./test.log', filemode='a')

    #获取单例
    @staticmethod
    def get_instance():
        if not hasattr(noticelogger, "_instance"):
            noticelogger._instance = noticelogger()
        return noticelogger._instance

    def red(self, message):
        logging.info("\033[1;31m{msg} \033[0m".format(msg=message))

    def green(self, message):
        logging.info("\033[1;32m{msg} \033[0m".format(msg=message))

    def yellow(self, message):
        logging.info("\033[1;33m{msg} \033[0m".format(msg=message))

    def blue(self, message):
        logging.info("\033[1;34m{msg} \033[0m".format(msg=message))

    def purple(self, message):
        logging.info("\033[1;35m{msg} \033[0m".format(msg=message))

    def cyan(self, message):
        logging.info("\033[1;36m{msg} \033[0m".format(msg=message))

    def white(self, message):
        logging.info("\033[1;37m{msg} \033[0m".format(msg=message))

    def black(self, message):
        logging.info("\033[1;30m{msg} \033[0m".format(msg=message))

    def FLiteTitle(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        banner_path = os.path.join(current_path, "banner.txt")
        with open(banner_path, "r") as f:
            txt = None
            for i, line in enumerate(f.readlines()):
                if i < 1:
                    self.red(line.strip())
                else:
                    if txt is None:
                        txt = line
                    else:
                        txt = txt + line
            self.blue(txt)


if __name__ == "__main__":
    notice_logger = noticelogger.get_instance()
    notice_logger.FLiteTitle()
    notice_logger.red("red")
    notice_logger.green("green")
    notice_logger.yellow("yellow")
    notice_logger.blue("blue")
    notice_logger.purple("purple")
    notice_logger.cyan("cyan")
    notice_logger.white("white")
    notice_logger.black("black")

    print("\033[1;31mDuring model publishing: Decryption (Blowfish) OK! \033[0m") # red
    print("\033[1;32mDuring model publishing: Decryption (Blowfish) OK! \033[0m") # green
    print("\033[1;33mDuring model publishing: Decryption (Blowfish) OK! \033[0m") # yellow
    print("\033[1;34mDuring model publishing: Decryption (Blowfish) OK! \033[0m") # blue
    print("\033[1;35mDuring model publishing: Decryption (Blowfish) OK! \033[0m") # purple
    print("\033[1;36mDuring model publishing: Decryption (Blowfish) OK! \033[0m") # cyan
    print("\033[1;37mDuring model publishing: Decryption (Blowfish) OK! \033[0m") # white
    print("\033[1;30mDuring model publishing: Decryption (Blowfish) OK! \033[0m") # black

