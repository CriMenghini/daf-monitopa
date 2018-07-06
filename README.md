# Monitoraggio Twitter per la Pubblica Amministrazione

## Introduzione
L'applicazione consiste in una dashboard che mostra delle informazioni statistiche rispetto ad hashtag e topi dei Tweet raccolti.

La struttura del progetto può essere racchiusa nella seguente immagine:
![alt text](img/sc.png "Logo Title Text 1")

In particolare, 

1. __Collezioniamo__ i Tweet tramite un collettore definito da un insieme di hashtag/account di interesse
2. __Preprocessiamo__ i Tweet prima di salvarli in MongoDB
3. Sviluppo del backend (Flask, Python) per rispondere alle __richieste__ fatte dal client
4. Il __client__ è sviluppato utilizzando React

### 1. Collettore
L'applicazione è stata sviluppata con l'intenzione di permettere alle singole PA un collettore che faccia riferimento agli hashtag/account che si desidera monitorare. 

In [questo](https://github.com/CriMenghini/daf-monitopa/blob/production/streamer/Twitter%20Streaming.ipynb) IPython Notebook, riportiamo l'esempio di un collettore. 

__N.B.__ Nel file viene mostrato anche come inserire il singolo tweet nel DB. Rispetto la figura, di cui sopra, non viene compiuta la fase di preprocessing.

*Al momento il prototipo dell'applicazione fa riferimeto ad un insieme statico di Tweet collezionati in breve tempo per sviluppare l'applicazione stessa.*

### 2. Pre-processing

La fase di preprocessing del singolo Tweet consiste nel definirlo come un oggetto con delle proprietà. Nella fattispecie, una volta collezionato, il Tweet ha delle proprietà fisse (come l'autore, l'id, etc..) e alcune variabili (ad esempio il numero di retweet). Pertanto, seppur ancora assente la connessione tra dati e DB, l'applicazione è stata sviluppata in modo che la transizione ad un sistema di storage sia il più smooth possibile.

Al termine della face di preprocessing all'interno del DB viene conservato un oggetto come quello che segue:

```			        
{'changable_attributes': {'list_user_retweet': [], 
							   'num_retweet': 0},
 'data_retweet': 'Tue Mar 06 12:05:00 +0000 2018',
 'data_tweet': 'Tue Mar 06 12:05:00 +0000 2018',
 'id_retweet': 970993648392220672,
 'id_tweet': 970993648392220672,
 'is_a_retweet': False,
 'list_hashtags': ['aria','5marzo'],
 'vectorized_text': [12195,12356],
 'num_retweet': 0,
 'padding': array([12195,     0]),
 'sentiment': 'negative',
 'tweet_text': "Qualità dell'#aria: i dati rilevati il #5marzo in #Toscana https://t.co/cbJg98X2ID #ambiente #inquinamento #smog",
 'user_info': {'followers_count': 5781, 'name': 'ARPAT'},
 'user_tweet_id': 461049017}
```

Per l'aggiornamento di alcune proprietà, si esegue una query per verificare se il Tweet è già nel DB e richiede quindi l'update. La classe è definita [qui](https://github.com/CriMenghini/daf-monitopa/blob/production/src/classes.py) con il nome `Tweet`.

### 3. Responses
Tramite interfaccia l'utente può compiere delle scelte e decidere cosa visualizzare. In base alle sue scelte, il server effettua delle operazioni. 

In primo luogo distinguiamo le due tipologie di analisi che l'utente può fare:

* In base all'__hashtag__
* Rispetto al __topic__

#### Hashtag
L'analisi tramite hashtag consiste nel visualizzare dei grafici relativi esclusivamente all'hashtag individuato.

Anche gli [hashtag](https://github.com/CriMenghini/daf-monitopa/blob/production/src/classes.py) vengono definiti come oggetti dalle seguenti proprietà (`Hashtag`):

```
{'hashtag': 'renzi',
 'lista_tweet': ([<__main__.Tweet at 0x11fe98c18>,
   <__main__.Tweet at 0x11fe96588>,
   <__main__.Tweet at 0x11fe96e10>],
  [970540855307198466,
   970729807272136705,
   970956245535510528]),
 'lista_user': [(3398885945, 'Mon Mar 05 06:05:46 +0000 2018'),
  (1566553698, 'Mon Mar 05 18:36:35 +0000 2018'),
  (3096871079, 'Tue Mar 06 09:36:23 +0000 2018')]
 
```


__N.B.__ I numeri mostrati dalla dashboard non rappresentano la totalità dei Tweet postati contenenti l'hashtag di interesse. Pertanto, per trarre conclusioni bisogna essere cauti. Certamente, le informazioni che si visualizzano possono dare un'idea di come un certo argomento è affrontato su Twitter.

#### Topic

## Development information
### Backend
The backend of the application is developed using Flask. 
### Frontend
The visualization uses React and has been built with [Create React App](https://github.com/facebook/create-react-app).

## Use the app
### Requirements
* `pip install tweet-preprocessor`

### Run the app
To see the visualization first clone this repository. Then
 
* In one terminal just run 

	> `ipython server.py` 
* In another terminal place yourself in `web-ui` and then run
	> `npm i` and `npm start` (you should see a dashboard at localhost:3000)