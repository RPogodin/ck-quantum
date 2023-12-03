# Руководство по квантовым вычислениям
# Введение
Наверняка каждый уже слышал хотя бы раз в своей жизни про квантовые технологии, новые суперкомпьютеры, которые по производительности превосходят классические во много-много раз и про новое светлое будущее, которое нас ждет.

Во-первых, все не совсем так, как нам хочется. Квантовые компьютеры далеко не всесильны и хорошо показывают себя лишь в некоторых областях. Во-вторых, это все пока что лишь в теории. Дело в том, что нынешние квантовые компьютеры не обладают достаточной мощностью для реализации многих полезных алгоритмов, из-за чего многие вещи приходится выполнять пока что на классических компьютерах. Но будущее не за горами, прогресс идет и очень скоро квантовые компьютеры заменят классические в некоторых узконаправленных задачах. 

Уже сейчас каждый желающий может запустить в браузере облачный сервис с квантовым компьютером, написать какой-нибудь код и получить результат. И это руководство вам в этом поможет. 

Первая глава написана для теоретического ознакомления с квантовыми вычислениями. Она очень пригодится тем, кто не знает каких-либо определений, связанных с этой темой или тем, кто плохо понимает как это вся система работает и устроена в принципе. 

Далее, во второй главе, мы перейдем к практической части нашего руководства. На примерах посмотрим, как работает квантовый компьютер, реализуя определения и методы, описанные в предыдущей главе. Напишем пару небольших программ и протестируем их. 

В третьей главе будут описаны практические применения квантовых вычислений. Рассмотрим различные подходы и методы программирования на квантовых компьютерах. Под конец в качестве эксперимента разработаем свою маленькую криптосистему и взломаем ее с использованием одного из квантовых алгоритмов.


# Глава I. Основы.
# Часть 1. Кубиты. Суперпозиция.
Чтобы с головой окунуться в славный мир квантовых технологий, нам очень сильно помогут основные определения и понятия, на которых все основано. Начнем с самых простых вещей – кубитов.

Наверняка вы уже хорошо знакомы с битами и прекрасно понимаете, что это такое и как они работают. Бит – это единица информации. В квантовых вычислениях в нашем распоряжении тоже есть единицы информации, но называются они кубитами. Существенное отличие битов от кубитов состоит в том, что первые могу находится лишь в двух состояниях – 0 или 1. Кубиты, в свою очередь, точно также могут находится в этих двух состояниях с одним маленьким но: у кубитов, ко всему прочему, существует вероятность нахождения в одном из двух состояний. Вполне возможно, что кубит, у которого вероятность нахождения в состоянии 1 равна 50%, может как содержать в себе некую единицу информации, так и не содержать ее вовсе. Этот феномен называется суперпозиция. 

Состояние суперпозиции можем наблюдать в реальной жизни: достаточно лишь подбросить монетку. До тех пор, пока монета находится в воздухе и не упадет на какую-либо поверхность, она находится в состоянии суперпозиции. Ведь мы не можем заведомо знать, что будет – орел или решка. И исход каждого из таких событий будет равен 50%, если не будет посторонних вмешательств.

Но мы вполне оправданно можем вмешиваться в этот процесс и менять вероятность под наши нужды. В случае с монеткой, мы можем подуть на нее или же примагнитить, чтобы увеличить шансы на благоприятный для нас исход. С кубитами все аналогично, правда подуть на них или примагнитить нам, к сожалению, не удастся. О том, как работать с состоянием суперпозиции, обсудим позже. 



 


