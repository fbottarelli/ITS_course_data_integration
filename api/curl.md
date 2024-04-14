### Esempi con Curl

#### uselseless fact
- https://uselessfacts.jsph.pl/
```
cd ITS...
```
uselsess fact simple
```bash
curl -X GET https://uselessfacts.jsph.pl/api/v2/facts/random
curl -X GET https://uselessfacts.jsph.pl/api/v2/today
```
parametri da cambiare
```bash
curl -X GET https://uselessfacts.jsph.pl/api/v2/facts/random?language=de
```

aggiugiamo l'header per specificare il formato della risposta che vogliamo
```bash
curl -H "Accept: application/json" -X GET https://uselessfacts.jsph.pl/api/v2/facts/random
```
Salviamo la risposta in un file
```bash
curl -H "Accept: application/json" -X GET https://uselessfacts.jsph.pl/api/v2/facts/random > useless.json
```

Altri esempi di comandi CURL
```bash
curl -X POST [URL]
curl -X PUT [URL]
curl -X DELETE [URL]
```

#### pokemonAPI
- https://pokeapi.co/
```bash
curl -X GET https://pokeapi.co/api/v2/pokemon/ditto
```
```bash
curl -H "Accept: application/json" -X GET https://pokeapi.co/api/v2/pokemon/ditto
```


#### NasaAPI
- https://api.nasa.gov/
```bash
curl -X GET https://api.nasa.gov/planetary/apod?api_key=${NASA_KEY}
```

### SpotifyAPI


### OpenMeteoAPI

```bash
curl -X GET "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"
```

```bash
curl -X GET "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=52.52&longitude=13.41&hourly=pm10,pm2_5"
```
