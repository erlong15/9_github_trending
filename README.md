# Анализ топовых новинок на github
Поиск топовых новинок за последнюю неделю.
Уточнение количества issues  у каждого

# Как запустить
Для запуска требуется python  версии 3.4 и выше

Для использования скрипта необходимо установить необходимые библиотеки.


```
pip install -r requrements.txt
```

На вход подается количество реопзиториев, по умолчанию 5
```
python3 github_trending.py -h
usage: github_trending.py [-h] [-c COUNT]

github trends watcher.

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        How much repos do you want to see (default: 5)
```

# Пример запуска

```
python3 github_trending.py 

    Repository: jennybc/docker-why
    URL: https://api.github.com/repos/jennybc/docker-why
    Description: Notes about why an R user would use Docker
    Issues: 0 
    

    Repository: ladyleet/women-tech-speakers-organizers
    URL: https://api.github.com/repos/ladyleet/women-tech-speakers-organizers
    Description: A list of women tech speakers & organizers. Add yourself or others by submitting a PR! PS if you do add someone, make sure to tell them! :) #fempire
    Issues: 8 
    

    Repository: unroll-io/react-email-editor
    URL: https://api.github.com/repos/unroll-io/react-email-editor
    Description: Drag-n-Drop Email Editor Component for React.js
    Issues: 0 
    

    Repository: jawache/smile-to-unlock
    URL: https://api.github.com/repos/jawache/smile-to-unlock
    Description: Want to give away free content on your site? How about asking for a smile in return 😁
    Issues: 0 
    

    Repository: jaychang0917/SimpleApiClient
    URL: https://api.github.com/repos/jaychang0917/SimpleApiClient
    Description: A retrofit extension written in kotlin
    Issues: 0 

```


# Цели проекта

Тренировочный код для проекта - [DEVMAN.org](https://devman.org)
