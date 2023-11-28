# AutoGen UI с системой двух агентов, копирайтер, маркетолог

Система из двух автономных агентов. Один - копирайтер, другой - маркетолог, развернутые на веб-интерфейсе(форке от [victordibia/autogen-ui](https://github.com/victordibia/autogen-ui) для контроля.
Используется материал для обучения маркетолога:
[Как_использовать_более_чем_100_психологических_секретов_рекламного.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/b99708e6-831d-4012-bac7-8a7c9bc63eb6/910f8be2-1e64-4397-894a-73051455f2f1/%D0%9A%D0%B0%D0%BA_%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C_%D0%B1%D0%BE%D0%BB%D0%B5%D0%B5_%D1%87%D0%B5%D0%BC_100_%D0%BF%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D1%85_%D1%81%D0%B5%D0%BA%D1%80%D0%B5%D1%82%D0%BE%D0%B2_%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE.pdf)

## Задача
Копирайтер пишет текст рекламы на тему продукта которого укажет пользователь, 
маркетолог должен проанализировать и дать список рекомендаций на основе книги выше, 
на основе него копирайтер перерабатывает текст. Так 3-4 цикла.
Сравниваем первый вариант и последний.

![AutoGen UI Screenshot](docs/images/autogenuiscreen.png)

Экспериментальная UI для работы с [AutoGen](https://github.com/microsoft/autogen) агентами, основанными на [AutoGen](https://github.com/microsoft/autogen) библиотеке. UI сделан на Next.js и web api построена на FastApi.

## Почему AutoGen UI?

AutoGen - это фреймворк, который позволяет разрабатывать приложения LLM с использованием нескольких агентов, которые могут взаимодействовать друг с другом для решения сложных задач. Пользовательский интерфейс может помочь в разработке таких приложений, обеспечивая быстрое прототипирование, тестирование и отладку агентов/потоков агентов (определение, компоновка и т.д.), проверяя поведение агентов и результаты работы агентов.

> **Note:** Это начальная стадия работы.

Обратите внимание, что вам придется настроить OPENAI_API_KEY или общую конфигурацию llm, используя переменную окружения.
Также смотрите эту статью о том, как Autogen поддерживает несколько [llm providers](https://microsoft.github.io/autogen/docs/FAQ/#set-your-api-endpoints)

```bash
export OPENAI_API_KEY=<your key>
```

## Приступая к работе

Установить из исходного кода

```bash
git clone https://github.com/shamemask/autogen-ui-promt.git
cd autogenui
pip install -e .
```

Запустить ui сервер.

```bash
autogenui # or with --port 8081
```
8081
Open http://localhost:8081 в вашем браузере.

Чтобы изменить исходные файлы, внесите изменения в исходные файлы интерфейса и запустите "npm run build", чтобы перестроить интерфейс.

## ССылки

- [AutoGen](https://arxiv.org/abs/2308.08155).

```
@inproceedings{wu2023autogen,
      title={AutoGen: Включение приложений LLM следующего поколения с помощью многоагентной платформы взаимодействия},
      author={Цинъюнь Ву и Гаган Бансал, и Цзею Чжан, и Иран Ву, и Шаокун Чжан, и Эркан Чжу, и Бэйбинь Ли, и Ли Цзян, и Сяоюнь Чжан, и Чи Ван},
      year={2023},
      eprint={2308.08155},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```
