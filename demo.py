
from rivescript import rivescript

rs = rivescript.RiveScript()

rs.load_directory('rive-files')
rs.sort_replies()

while True:
    pergunta = raw_input('Pergunta: ')
    print 'Resposta: '+rs.reply("bel",pergunta)
