# Руководство по квантовым вычислениям
## Введение
Наверняка каждый уже слышал хотя бы раз в своей жизни про квантовые технологии, новые суперкомпьютеры, которые по производительности превосходят классические во много-много раз и про новое светлое будущее, которое нас ждет. 

Во-первых, все не совсем так, как нам хочется. Квантовые компьютеры далеко не всесильны и хорошо показывают себя лишь в некоторых областях. Во-вторых, это все пока что (на момент написания этого гайда) лишь в теории. Дело в том, что нынешние квантовые компьютеры не обладают достаточной мощностью для реализации многих полезных алгоритмов, из-за чего многие вещи приходится выполнять пока что на классических компьютерах. Но будущее не за горами, прогресс идет и очень скоро квантовые компьютеры заменят классические в некоторых узконаправленных задачах. 

Уже сейчас каждый желающий может запустить в браузере облачный сервис с квантовым компьютером, написать какой-нибудь код и получить результат. И это руководство вам в этом поможет. 

Первая часть написана для теоретического ознакомления с квантовыми вычислениями. Она очень пригодится тем, кто мало знаком с этой темой или тем, кто плохо понимает как это вся система работает и устроена в принципе. 

Далее, во второй части, мы перейдем к практике нашего руководства. На примерах посмотрим, как работает квантовый компьютер, реализуя определения и методы, описанные в предыдущей главе. Напишем пару небольших программ и протестируем их. 

В третьей части мы постараемся разобраться с квантовыми сетями: что это, как это работает и что нам следует ожидать. Тема интересная, пусть и пока что мало изученная, но тем не менее разобраться определенно стоит. Приступим!


# Часть I. Основы.
## 1. Кубиты. Суперпозиция.

Чтобы с головой окунуться в славный мир квантовых технологий, нам очень сильно помогут основные определения и понятия, на которых все основано. Начнем с самых простых вещей – кубитов (в англ. Qubits).

Наверняка вы уже хорошо знакомы с битами и прекрасно понимаете, что это такое и как они работают. Бит – это единица информации. В квантовых вычислениях в нашем распоряжении тоже есть единицы информации, но называются они кубитами. Существенное отличие битов от кубитов состоит в том, что первые могу находится лишь в двух состояниях – 0 или 1. Кубиты, в свою очередь, точно также могут находится в этих двух состояниях с одним маленьким но: у кубитов, ко всему прочему, существует вероятность нахождения в одном из двух состояний. Вполне возможно, что кубит, у которого вероятность нахождения в состоянии 1 равна 50%, может как содержать в себе некую единицу информации, так и не содержать ее вовсе. Этот феномен называется суперпозиция (в англ. Superposition). 

Состояние суперпозиции можем наблюдать в реальной жизни: достаточно лишь подбросить монетку. До тех пор, пока монета находится в воздухе и не упадет на какую-либо поверхность, она находится в состоянии суперпозиции. Ведь мы не можем заведомо знать, что будет – орел или решка. И исход каждого из таких событий будет равен 50%, если мы обойдемся без посторонних вмешательств.

Но мы вполне оправдано можем вмешиваться в этот процесс и менять вероятность под наши нужды. В случае с монеткой, мы можем подуть на нее или же примагнитить, чтобы увеличить шансы на благоприятный для нас исход. С кубитами все аналогично, правда подуть на них или примагнитить нам, к сожалению, не удастся. О том, как работать с состоянием суперпозиции, мы обсудим позже. 

## 2. Запутанность. Интерференция.

Обсудим еще парочку важных для нас определений. Первое из них – квантовая запутанность (в англ. Quantum entanglement). Это явление, при котором два или более кубита оказываются связанны таким образом, что если состояние первого кубита было изменено, то оно повлияет на состояния других кубитов, вне зависимости от расстояния между ними. Проще говоря, кубиты ведут себя так, как если бы они «знали» друг о друге и действовали согласованно. 

Для понимания этого процесса вернемся к примеру с монеткой. Возьмем еще одну монетку и скажем, что пусть первая монетка всегда в конечном итоге показывает орел, а вторая – решку. Таким образом мы установили взаимосвязь между ними. И даже если мы улетим далеко-далеко, в другую вселенную, и бросим эти две монетки в одно время (хотя, конечно, это понятие относительное, но отбросим все формальности и предположим, что нам удалось это сделать), то на основании конечного состояния первой монетки мы смело можем делать вывод о конечном состоянии второй монетки. 

Теперь перейдем к интерференции. Квантовая интерференция – это явление, при котором два или более кубита взаимодействуют друг с другом, находясь в состоянии суперпозиции, тем самым влияя на конечные состояния всех кубитов. 

В качестве примера представим гладкий пруд. В руках у нас два камня. И мы бросаем каждый из камней в пруд. Каждый камень создает круговые волны, которые распространяются по поверхности воды от точек, где упали камни. На первый взгляд кажется, что эти волны от двух камней распространяются независимо друг от друга, но на деле это не совсем так. Когда волны встречаются, они взаимодействуют друг с другом и интерферируют: если гребни волн совпадают, то они усиливают друг друга, создавая более высокие волны. Если гребни одной волны совпадают с впадинами другой, то волны подавляются. Здесь мы можем провести аналогию и с кубитами. При взаимодействии друг с другом они могут влиять на состояния других кубитов как положительно, так и отрицательно. 

На этом первую часть гайда можно завершить. Теперь вы знаете основы квантовых вычислений и вы в состоянии понять, что будет происходить дальше. А дальше будет только интереснее!

# Часть II. Квантовые вентили и логические элементы.

Для начала стоит обговорить зачем эта часть нужна в принципе. Дело в том, что при описании квантовых алгоритмов постоянно используются квантовые вентили и логические элементы. И понять что происходит в алгоритме довольно трудно, не зная таких вещей. Потому очень важно познакомить читателя с данным «языком». 

## 1. Опять основы.
Начнем с самого простого. Чтобы начать пользоваться квантовыми вычислениями, необходимо понять как это все представляется с помощью математических формул. 

Так, например, обозначается кубит с состоянием 1: 

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/1aaabde3-5ea7-4899-9769-cdc862bab593"/>
</p>

А так выглядит кубит с состоянием 0:

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/989f5fb7-d1f1-4c6d-85d2-195aec92748a"/>
</p>

А так выглядит состояние двух кубитов:

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/9ae09376-d0e7-4fae-9203-3047be68795e"/>
</p>

Оно вычисляется с помощью тензорного произведения состояний двух других кубитов. 

Очень удобно будет визуализировать состояния кубитов, чтобы понять дальнейшие операции. Так мы можем представить состояния кубитов на сфере Блоха:

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/9b0311a1-1146-4585-9ad3-269109b40ebf"/>
</p>


Здесь «+» и «-» - сумма (разность) двух состояний 0 и 1 деленная на корень из двух (т.е. в этих точках у нас возникает суперпозиция).

Также у нас существуют так называемые 4 состояния Белла. Они являются простейшим примером квантовой запутанности. 

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/c43dfa8d-8b72-4bb4-aa58-7e7dbc93b329"/>
</p>


## 2. Диаграммы квантовых цепей и вентили.
 
Перейдем теперь на сайт https://quantum.ibm.com/ (В России он, скорее всего, работать не будет, потому воспользуйтесь ВПН). Зарегестрируйтесь, войдите в аккаунт и перейдите в раздел «IBM Quantum Composer». Создав новый файл, вы увидите вот это: 

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/6bddc46e-601a-4ab4-b26d-577d8a33fcfb"/>
</p>

Слева у нас расположены все доступные нам квантовые вентили. В центре сверху у нас находится диаграмма цепей. Снизу расположены шкала вероятностей для кубитов и сфера Блоха. Справа можем увидеть представление нашей диаграммы в виде кода на языке, который мы выбрали (из доступных есть Qiskit и OpenQASM). Давайте теперь разбираться подробнее что есть что и как оно работает.

Начнем с диаграммы. Нам сразу же дали в распоряжение 4 кубита (или, как их еще называют, квантовые регистры): q[0], q[1], q[2] и q[3]. Также у нас есть классический регистр c4. Это просто напросто самый обычный бит, который либо содержит единицу информации, либо нет. Никакой суперпозиции. После того, как все операции с кубитами были завершены, полученный результат сохраняется в классическом регистре. Также может быть и такое, что классический регистр понадобиться при реализации какого-либо алгоритма. 

Перейдем к вентилям. Здесь их довольно много, но мы рассмотрим лишь парочку и самые основные. Остальные используются не так часто и при желании всегда можно будет посмотреть информацию о них в других источниках.

1. Преобразование Адамара (Hadamar transformation, H-gate) — преобразование на единичный кубит. Это преобразование приводит кубит в состояние суперпозиции.
   
<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/b888186b-a5f0-4f59-adbc-3e10e1c4401b"/>
</p>

Как вы можете видеть на скриншоте, я применил к первому кубиту преобразование Адамара и он вошел в состояние суперпозиции — вероятность нахождения в состоянии 0 или 1 этого кубита равняется 50%.

Для наглядности и более простого восприятия, я оставил лишь один квантовый регистр. 

Если рассматривать вентиль Адамара относительно поворотов осей, то он будет соответствовать повороту осей X и Z. 

2. Отрицание (NOT gate, Pauli X gate) — поворот состояния относительно оси X на π радиан. По сути это логическое нет. Меняет состояние кубита с 0 на 1 и наоборот.
   
3. Вентиль Паули Y (Pauli Y gate) — поворот состояний относительно оси Y на π радиан. Вот так это выглядит на сфере Блоха:

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/82f45315-6926-4911-88af-aa9d47198fbe"/>
</p>

4. Фазовый сдвиг (Pauli Z gate) — поворот состояния относительно оси Z. Это преобразование, которое поворачивает состояние 1 на 180 градусов, т.е. из состояния 1 мы получаем состояние -1. На сфере Блоха это выглядит таким образом:

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/0304bd2f-39cb-4d96-8285-7c3e02c5bf4f"/>
</p>

Здесь я подействовал на кубит в состоянии суперпозиции (сделал я это с помощью преобразования Адамара) вентилем Z. Как мы можем видеть, на сфере Блоха сразу же отобразилось, что состояние 1 повернулось на 180 градусов, то есть стало -1. 

Этот гейт не меняет нулевое состояние кубита, но для состояния 1 оно меняет знак.

5. Тождественное преобразование (Identity gate, I gate) — преобразование, которое не меняет состояние кубита. Оно необходимо тогда, когда нам нужно, чтобы состояние кубита не изменялось в какой-то определенный момент времени.
  
6. Контролируемое отрицание (CNOT) — еще одно преобразование, которое пригодится нам при рассмотрении алгоритма квантовой телепортации. Это преобразование работает с двумя кубитами, потому чтобы нам удалось его применить на практике, потребуется два квантовых регистра. Как этот вентиль работает? Для начала он берет первый кубит, который становится «управляющим» (control qubit) и воздействует на второй кубит, который называется «целью» (target qubit). Если состояние управляющего кубита было равно 1, то вентиль CNOT инвертирует состояние кубита цели, т.е. работает как X gate. Иначе, если состояние управляющего кубита было равно 0, то ничего не происходит. Но если управляющий кубит находился в состоянии суперпозиции, то этот вентиль создает запутанность (entanglement).
   
7. Фазовый вентиль (S Gate, Phase Gate) — поворот относительно оси z на угол π/2. При этом преобразовании состояние 0 остается без изменений, а состояние 1 преобретает дополнительную фазу, т.е. совершает поворот на угол π/2 относительно оси z.
   
8. Измерительный гейт (Measurement). На самом деле это не совсем вентиль, но удобнее его воспринимать таковым. Что он делает? Когда мы применяем измерительный вентиль к кубиту в квантовом регистре, он как бы приостанавливает его состояние суперпозиции (если кубит в нем находился, иначе он просто напросто переводит информацию в классический регистр) и вычисляет вероятность состояний этого кубита. На основе вероятностей этих состояний измерительный гейт отправляет на классический регистр одно из значений — 0 или 1. И воспринимается это все теперь как классические биты.
   
Мы обсудили и разобрали все основные квантовые вентили. При желании вы можете разобрать их все, но они не столь важны в нашем пути. Но если все же интересно, то по каждому вентилю вы можете прочитать информацию, кликнув на него правой кнопкой мыши. А теперь перейдем к практике!

# Часть III. Практическое применение полученных знаний.
## 1. Запуск первой программы.

Теперь когда мы знаем все необходимое для написания простеньких программ, давайте приступим к запуску нашей первой программы на квантовом компьютере! 
Я выставил вот такие незатейливые вентили на регистры:

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/559b5ba7-dfab-436e-8380-947c6396786e"/>
</p>

Давайте проверим что мы получим в конечном итоге. Нажмем на кнопку «Setup and run». 

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/009c94ab-af8e-434d-b0ce-f00b871cc9c1"/>
</p>

Высветится вот такое меню. Слева у нас расположен список доступных нам квантовых компьютеров или симуляторов. Их довольно много, но я выбрал тот, на котором была маленькая очередь, чтобы программа запустилась быстрее. 

Под каждым из компьютеров расположена информация о статусе системы, количестве работ в ожидании, количество кубитов, EPLG и CLOPS.
EPLG — error per layered gate — это коэффициент, который показывает частоту ошибок при выполнении двухкубитных (или более) вентилей в одно и то же время на 100 кубитов (здесь используется именно это число).

CLOPS — это мера того, насколько быстро наши процессоры могут последовательно запускать схемы квантового объема. То есть сколько операций квантового объема эта система способна исполнить за одну секунду. 

Справа у нас 3 строчки. Instance — экземпляр или компьютер, который мы выбрали; Shots — количество итераций, которое наш суперкомпьютер должен будет проделать для нашей программы; Tags — комментарий к нашей программе. Он ничего существенного не дает, но вы можете написать туда что-нибудь и это что-нибудь сможет увидеть другой человек, если заглянет на то, что исполняет (или собирается исполнить) квантовый компьютер или симулятор.

На этом все. Можно смело нажимать кнопочку «Run on ...». После небольшой загрузки мы можем отслеживать процесс работы слева:

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/43b79842-1d30-461a-b2bb-c3cc96c3b617"/>
</p>

Поскольку очередь была крайне маленькой, завершилось у меня все за считанные секунды. Давайте взглянем на результат!

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/23b3c226-2a77-4b3e-8712-6a9a8681ed9f"/>
</p>

В quasi_dists отображаются наши результаты измерений. Для состояния 00 вероятность равна 0.4580078125, а для 01 равна 0.5419921875. В metadata отображаются метаданные наших вычислений. Shots — количество итераций. В circuit_metadata отображается дополнительная информация о схеме или настройках вычисления. Мы ничего сверхъестественного в нашу программу не добавляли, а потому эта строчка пуста. readout_mitigation_overhead отвечает за накладные расходы на коррекцию считывания. Метод коррекции считывания мы не применяли, потому эта строка вернула нам 1. И readout_mitigation_time показывает время, затраченное на исполнение вычислений, а именно 0.014736633995198645 секунд. 

Запустим нашу программу еще раз и посмотрим на полученные результаты. В этот раз я выставил 4096 итераций.

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/ee5fd7ba-40cb-4a78-8f80-546f5cfd6ec4"/>
</p>

Здесь результаты уже более точные и приближенные к реальности: вероятность попадания в состояние 00 составило 0.49, а в состояние 01 — 0.51. И чем больше у нас будет итераций, тем более наши вероятности будут точны и приближены к теоретически ожидаемому результату.

## 2. Квантовая телепортация.

Перейдем, наконец, к самому интересному — квантовой телепортации. Это процесс в квантовой механике, который позволяет передавать информацию (в нашем случае состояния кубитов) из одного места в другое с помощью состояний суперпозиции и квантовой запутанности кубитов между отправителем и получателем. Давайте разберемся как этот процесс работает.  

Изначально у нас есть два человека, скажем, Петя и Вася. Петя хочет передать Васе некоторое закодированное квантовым состоянием сообщение. Для передачи такого рода сообщений нам необходима квантовая система, состоящая как минимум из трех квантовых регистров (2 регистра контролирует Петя, 1 для Васи) и двух классических регистров для передачи результатов измерений. Вообще говоря, из-за использования классических регистров в этом процессе он не совсем является телепортацией, как его все называют, и не выполняется быстрее скорости света, но в теории все равно является очень быстрым способом передачи информации между пользователями.

Чтобы Петя передал информацию Васе, первый кубит должен находится в некотором состоянии (т.е. содержать информацию, которую хочет передать Петя), которое мы будем передавать с помощью второго кубита на третий. Для этого мы последовательно выполняем следующие шаги:

1)  Мы применяем преобразование Адамара ко второму кубиту.
2) Применяем вентиль CNOT к второму кубиту, чтобы ввести третий кубит в состояние квантовой запутанности со вторым кубитом.
3) Затем мы запутываем первый кубит со вторым при помощи того же вентиля CNOT.
4) Применяем преобразование Адамара на первый кубит.
5) Измеряем первые два кубита и передаем по классическому регистру информацию Васе.
6) Вася же теперь должен применить одну из операций в зависимости от полученных данных, чтобы восстановить исходное состояние. По такому принципу Вася должен будет применить определенное преобразование:

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/7ba5fff6-0a33-4def-8f08-00930e8b294d"/>
</p>

Вот так должна выглядеть конечная схема алгоритма:

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/aba39fd7-50e8-4a8f-8b61-67308f5edeaf"/>
</p>


Про единичные преобразования я ничего не говорил, но используются они лишь для того, чтобы упорядочить выполнение программы и она выглядела проще. 
Вот сам код программы:

```OpenQASM
OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c0[1];
creg c1[1];
h q[1];
cx q[1], q[2];
cx q[0], q[1];
id q[2];
h q[0];
measure q[1] -> c1[0];
id q[2];
measure q[0] -> c0[0];
if (c1 == 1) x q[2];
if (c0 == 1) z q[2];
```
Через эмулятор IBM изобразить передачу сообщений довольно проблематично, потому для того, чтобы продемонстрировать работу алгоритма воспользуемся этим [ресурсом](https://algassert.com/quirk#circuit={%22cols%22:[[1,%22H%22],[1,%22%E2%80%A2%22,1,1,%22X%22],[%22%E2%80%A6%22,%22%E2%80%A6%22,1,1,%22%E2%80%A6%22],[%22%E2%80%A6%22,%22%E2%80%A6%22,1,1,%22%E2%80%A6%22],[%22~87lj%22],[%22Bloch%22],[%22%E2%80%A2%22,%22X%22],[%22H%22],[%22Measure%22,%22Measure%22],[1,%22%E2%80%A2%22,1,1,%22X%22],[%22%E2%80%A2%22,1,1,1,%22Z%22],[1,1,1,1,%22Bloch%22],[1,1,1,1,%22~f7c0%22]],%22gates%22:[{%22id%22:%22~87lj%22,%22name%22:%22message%22,%22circuit%22:{%22cols%22:[[%22e^-iYt%22],[%22X^t%22]]}},{%22id%22:%22~f7c0%22,%22name%22:%22received%22,%22matrix%22:%22{{1,0},{0,1}}%22}]}).

Здесь наглядно показано при помощи сферы Блоха как мы передаем некоторое сообщение с первого регистра на третий. Обратите внимание, что передача сообщения сохраняется с точностью до фазового сдвига.

Собственно вот и все! Таким казалось бы простым алгоритмом мы «телепортируем» информацию от одного пользователя к другому. Фантастика!

## 3. Сверхплотное кодирование.

Сверхплотное кодирование является противоположной задачи о квантовой телепортации. Задача квантовой телепортации состояла в передаче одного кубита (вернее его состояния) с помощью двух классических бит. Задача сверхплотного кодирования обратна — нам необходимо передать два классических бита с помощью одного кубита. 

Вернемся к нашим двум товарищам — Пете и Васе. Пусть изначально у нас имеется пара запутанных кубитов. Первый кубит для Пети, второй — для Васи. 

При помощи лишь двух кубитов Петя может передавать Васе два бита классической информации по такому принципу:

1. Если Петя хочет передать Васе битовую строку «00», то он ничего не делает со своим кубитом и ждет пока Вася его декодирует;
2. Если он хочет передать битовую строку «01», то он применяет X gate (NOT) к своему кубиту;
3. Если Петя хочет передать битовую строку «10», то он применяет фазовый сдвиг (Z gate) к своему кубиту;
4. И, наконец, если он хочет передать битовую строку «11», то он применяет X gate и Z gate последовательно к своему кубиту.

Таким образом внимательный читатель сразу заметит, что мы получили состояния Белла. И этот читать окажется прав! Действительно, это совсем нетрудно проверить, зная реализации всех используемых вентилей в матричном виде.

Поскольку кубиты у нас находятся в состоянии запутанности, то Вася вне зависимости от растояния от Пети все равно сможет получить состояние кубита, которое хотел донести до него Петя и затем декодировать его.

А каким образом он будет декодировать полученное состояние кубита? А все довольно просто. Вася применит к квантовым регистрам вентиль CNOT, где первый кубит является управляющим, а затем применяет преобразование Адамара к этому же кубиту. После этого Вася смело может измерять состояние обоих кубитов, чтобы получить закодированное сообщение Пети.

Вот так должна выглядеть конечная схема алгоритма:

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/892ea67e-8cb2-4be4-955c-7d9986586e69"/>
</p>

В этот раз давайте проверим результат работы не только на симуляторе квантового компьютера, но и на реальном, и сравним полученные результаты. 

Вот что мы получим при запуске нашей программы на симуляторе: 

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/8411670d-5768-4004-a9a7-c891e4aa1971"/>
</p>

И на квантовом компьютере: 

<p align="center">
 <img src="https://github.com/RPogodin/ck-quantum/assets/102846577/c7ec6e57-93b2-4175-b650-34835c3822ab"/>
</p>

Поскольку очередь на квантовый компьютер всего довольно большая, приходится ждать по 4 и более часов на то, чтобы произвести желаемые вычисления. 

На симуляторе мы можем видеть, что мы имеем 100% вероятность измерить правильное сообщение, а вот на квантовом компьютере все не так хорошо. Шанс измерить правильное сообщение составил 90%. Все это происходит из-за так называемой декогеренции и погрешностей в вентилях. 

Декогеренция — это разрушение состояния суперпозиции кубитов, если говорить простыми словами. Оно может быть вызвано разными факторами, начиная от ошибок в аппаратной реализации и заканчивая взаимодействием с окружающей средой (квантовые системы очень чувствительны к внешним возмущениям, таким как электромагнитное излучение, тепловые флуктуации и прочие виды шумов). 


# Часть IV. Заключение.

На этом все. Гайд получился небольшим, но поскольку работа велась лишь одним человеком в свободное от других дел время, то это вполне себе неплохо =-) 

Сам проект на этом не заканчивается и я надеюсь, что он будет развиваться и дальше - если не мной, то другими. На данном этапе с моей точки зрения есть еще пару моментов, которые можно было бы сделать лучше, расписать подробнее, привести больше примеров и прочее:

1) Часть с математическими представлениями кубитов оказалась довольно скудной на формулы и почти непонятной для новичка. Я думаю, что было бы здорово дополнить ее, сделать более понятной для новичка.
  
2) Алгоритмы. Их много и предназначены они для всяких разных дел. Самую обширную область в этом занимают алгоритмы, связанные с криптографией и расшифровкой сообщений. Интересно было бы взглянуть на применение подобных алгоритмов для расшифровки сообщений.

3) Вентили. Еще одна часть гайда, которая была обделена математикой. Необходимо дополнить, чтобы было понятнее откуда все берется.

4) Больше тестов, больше примеров! Есть и другие сайты с симуляцией квантовых алгоритмов, которые были обделены вниманием в рамках этого гайда. Было бы неплохо добавить и показать принципы работы алгоритмов на них в том числе.

### Ссылки на ресурсы, которыми я пользовался:
1) https://habr.com/ru/articles/480480/
2) https://learn.microsoft.com/ru-ru/azure/quantum/overview-understanding-quantum-computing
3) https://habr.com/ru/companies/microsoft/articles/351622/
4) https://quantum-ods.github.io/qmlcourse/book/index.html
5) https://habr.com/ru/articles/338202/
6) https://vas3k.blog/blog/quantum_computing/

   . . . 
и огромное множество других статей на Хабре, видеороликов на YouTube и множество других различных сайтов и проектов на GitHub.

А также песочницы, симуляторы и библиотеки, с помощью которых можно протестировать работу разных алгоритмов:
1) https://www.quantumplayground.net/#/home
2) https://azure.microsoft.com/ru-ru/products/quantum
3) https://aws.amazon.com/ru/braket/
4) https://algassert.com/quirk
5) https://github.com/quantumlib/stim/
6) https://algassert.com/crumble
