# Задание 3.1 Запрос на SPARQL

## Вариант 4.

Cписок фильмов в том же жанре, вышедших на той же киностудии

```
#Movies that have same genre, production company as Recommended movie (Green Mile)
SELECT DISTINCT ?movie ?movieLabel WHERE {
  {
    SELECT ?movie WHERE {
      ?movie wdt:P31 wd:Q11424.
      wd:Q208263 wdt:P136 ?sameGenre;
        wdt:P272 ?sameStudio.
      ?movie wdt:P136 ?genre.
      FILTER(?sameGenre = ?genre)
      ?movie wdt:P272 ?studio.
      FILTER(?sameStudio = ?studio)
    }
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
```

[Try it yourself](https://query.wikidata.org/#%23Movies%20that%20have%20same%20genre%2C%20productio%20company%20as%20Recommended%20movie%20%28Green%20Mile%29%0ASELECT%20DISTINCT%20%3Fmovie%20%3FmovieLabel%20WHERE%20%7B%0A%20%20%7B%0A%20%20%20%20SELECT%20%3Fmovie%20WHERE%20%7B%0A%20%20%20%20%20%20%3Fmovie%20wdt%3AP31%20wd%3AQ11424.%0A%20%20%20%20%20%20wd%3AQ208263%20wdt%3AP136%20%3FsameGenre%3B%0A%20%20%20%20%20%20%20%20wdt%3AP272%20%3FsameStudio.%0A%20%20%20%20%20%20%3Fmovie%20wdt%3AP136%20%3Fgenre.%0A%20%20%20%20%20%20FILTER%28%3FsameGenre%20%3D%20%3Fgenre%29%0A%20%20%20%20%20%20%3Fmovie%20wdt%3AP272%20%3Fstudio.%0A%20%20%20%20%20%20FILTER%28%3FsameStudio%20%3D%20%3Fstudio%29%0A%20%20%20%20%7D%0A%20%20%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%22.%20%7D%0A%7D)
