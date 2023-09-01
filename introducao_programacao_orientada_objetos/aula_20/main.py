from log import LogFileMixin, LogPrintMixin
from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

galaxy_s.ligar()
iphone.desligar()

import logging

# Configurar o logger
logging.basicConfig(filename='meu_arquivo_de_log.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Exemplos de mensagens de log
logging.debug('Esta é uma mensagem de depuração')
logging.info('Esta é uma mensagem informativa')
logging.warning('Este é um aviso')
logging.error('Este é um erro')
logging.critical('Este é um erro crítico')

# Fechar o logger
logging.shutdown()


# Mixins
# lp = LogFileMixin()
# lp.log_error('Qualquer coisa')
# lp.log_success('Qualquer coisa')
# lf = LogFileMixin()
# lf.log_error('Qualquer coisa')
# lf.log_success('Qualquer coisa')