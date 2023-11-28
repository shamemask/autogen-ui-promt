# AutoGen UI

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
