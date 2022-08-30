
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

month = morph.parse('устройство')[0]
month.inflect({'gent'})

for i in range(100):
    print (f'%s %s' % (i, month.make_agree_with_number(i).word))

# gent = butyavka.inflect({'gent'})
#
# print (butyavka)
# print (butyavka.make_agree_with_number(1).word)
# print (butyavka.make_agree_with_number(2).word)
# print (butyavka.make_agree_with_number(3).word)
# print (butyavka.make_agree_with_number(4).word)
# print (butyavka.make_agree_with_number(5).word)
# print (butyavka.make_agree_with_number(6).word)
# print (butyavka.make_agree_with_number(7).word)
# print (butyavka.make_agree_with_number(8).word)
# print (butyavka.make_agree_with_number(9).word)
# print (butyavka.make_agree_with_number(10).word)
# print (butyavka.make_agree_with_number(11).word)
# print (butyavka.make_agree_with_number(22).word)
# print (butyavka.make_agree_with_number(29).word)
