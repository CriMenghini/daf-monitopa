import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import createClass from 'create-react-class';
import BoardHashtag from './Board';
import Hashtag  from './Hashtag';
import SearchBar from './SearchBar';
import Menu from './Menu';
import { Container, Row, Col } from 'reactstrap';
import VisualisationGrid from './GridVisualisation';
import TopUsers from './TopUsers';
import ChooseTopic from './TopicButton';
import '../node_modules/bootstrap-italia/dist/css/bootstrap-italia.min.css';
import '../node_modules/bootstrap-italia/dist/css/italia-icon-font.css';
import numTweet from './data/numberTweet_hashtag.js';
import Retweet from './data/TopRetweet.js';
var _ = require('lodash');



const API = 'http://127.0.0.1:5000/api_dati_tweet';


var App =  createClass({


          getInitialState: function (){
                        return {sentence: 'inserire qui hashtag',
                                numtweet: numTweet,
                                numretweet: Retweet,
                                sentiment: [{ x: 1, y: 5},{ x: 2, y: 4}, { x: 3, y: 4}],
                                unique: [{ x: 12, y: _.random(1, 5) },{ x: 2, y: _.random(1, 10) },{ x: 3, y: _.random(2, 10) },{ x: 4, y: _.random(2, 20) },{ x: 5, y: _.random(2, 15) }],
                                streampos: [{ a: new Date(1982, 1, 1), b: 105 },
                { a: new Date(1987, 1, 1), b: 257 },
                { a: new Date(1993, 1, 1), b: 35 },
                { a: new Date(1997, 1, 1), b: 15 },
                { a: new Date(2001, 1, 1), b: 150 },
                { a: new Date(2005, 1, 1), b: 305 },
                { a: new Date(2011, 1, 1), b: 270 },
                { a: new Date(2015, 1, 1), b: 470 }
              ],
                                streamneg: [{ a: new Date(1982, 1, 1), b: 105 },
                { a: new Date(1987, 1, 1), b: 257 },
                { a: new Date(1993, 1, 1), b: 35 },
                { a: new Date(1997, 1, 1), b: 15 },
                { a: new Date(2001, 1, 1), b: 150 },
                { a: new Date(2005, 1, 1), b: 305 },
                { a: new Date(2011, 1, 1), b: 270 },
                { a: new Date(2015, 1, 1), b: 470 }
              ],
              streamneu: [{ a: new Date(1982, 1, 1), b: 105 },
                { a: new Date(1987, 1, 1), b: 257 },
                { a: new Date(1993, 1, 1), b: 35 },
                { a: new Date(1997, 1, 1), b: 15 },
                { a: new Date(2001, 1, 1), b: 150 },
                { a: new Date(2005, 1, 1), b: 305 },
                { a: new Date(2011, 1, 1), b: 270 },
                { a: new Date(2015, 1, 1), b: 470 }
              ],


                                DataSet:[{'x': 1, 'y': 100, 'label': 'RT @GianninoilGreco: . . . Ma il biglietto poi l\'ha fatto la #Meli? "Emigrerò" ✈️\n#lariachetirala7 #MaratonaMentana #elezioni2018 #M5S http…\nAutore: Danilo\nFollowers: 128'}, {'x': 2, 'y': 108, 'label': "RT @Penelopy2000: Il #M5S in #Campania prende tutto\nL'impero #DeLuca sconfitto\nAi campani non piacciono le fritture di pesce\n\n#elezioni2018…\nAutore: Penelope S.\nFollowers: 4843"}, {'x': 3, 'y': 50, 'label': 'RT @danilosantini65: Il vero vincitore di queste #elezioni2018 è @matteosalvinimi che ha riportato un partito dal 3% al 18% .Il #m5s era il…\nAutore: Danilo\nFollowers: 2675'}, {'x': 4, 'y': 23, 'label': 'RT @ErmannoKilgore: #lariachetira #elezioni2018 \n😂😂😂molto divertente,\nper i Media nazionali le elezioni le hanno vinte #M5S e #Salvini! Ben…\nAutore: Kilgore\nFollowers: 11571'}, {'x': 5, 'y': 22, 'label': 'RT @nogarin: Non ho analizzato il voto a #Roma e #Torino, ma quello a #Livorno sì. Nel 2014, quando sono stato eletto, il #M5S era a 13.459…\nAutore: Filippo Nogarin\nFollowers: 14070'}, {'x': 6, 'y': 4, 'label': 'RT @AJG_Official: Madonna come esulta gigino #M5S #Elezioni2018 https://t.co/Fnu09fViTJ\nAutore: AverageJuventinoGuy\nFollowers: 1850'}, {'x': 7, 'y': 3, 'label': 'Ci facciano il piacere, lor signori del #M5S, di smettere di dire che il Rosatellum è stato fatto per non farli str… https://t.co/D9teQGP68I\nAutore: Raid\nFollowers: 1301'}, {'x': 8, 'y': 2, 'label': 'RT @diggita: Elezioni, cosa succede dopo il voto? I vari possibili scenari https://t.co/rlxUuUohvX #Politica #elezioni2018 #lega #m5s https…\nAutore: diggita\nFollowers: 38976'}, {'x': 9, 'y': 2, 'label': 'RT @nedopaglianti: Meditate gente, meditate...\n#M5s in calo nelle grandi città che amministra: perde consensi a #Roma, #Torino, #Livorno ht…\nAutore: Nedo Paglianti\nFollowers: 5490'}, {'x': 10, 'y': 2, 'label': "RT @UnicronPlanetM: #M5S Ora! M5S Livorno\nSeguite i primi attimi dell'evento in Piazza del Popolo insieme a noi! #Livorno c'è! Buon Voto a…\nAutore: UnicronPlanetMode\nFollowers: 1135"}]
              }},



        handleSubmit: function(event) {
                            event.preventDefault();

                            fetch('http://127.0.0.1:5000/api_dati_tweet', {method: 'post',
                                        headers: {'Content-Type':'application/json'},
                                        body: JSON.stringify({"selectedHashtag": this.state.sentence})})

                                        .then(response => {
                                          return response.json();}
                                        )
                                        .then(data => this.setState({numtweet: data.numTweet,
                                                                     numretweet: data.NumRetweet,
                                                                     percent: data.numTweet,
                                                                     sentiment: data.Sentiment,
                                                                     unique: data.Unique,
                                                                     streampos: data.StreamPos,
                                                                     streamneg: data.StreamNeg,
                                                                     streamneu: data.StreamNeu,
                                                                     DataSet: data.dataSet}))
                                        },

        handleClick: function (event){
                            this.setState({sentence: event.target.value,
                                           percent: this.state.numtweet})
                                      },

        render() {

            return (<div className='App'>
                        <div className='Title'>
                          <h1 className='title-name'>What is our opinion?</h1>

                        </div>


                       <div className='Sidebar' id='mySidebar'>
                            <div className='Sidebar-hashtag'>
                              <SearchBar { ...this.props } { ...this.state} funzioneSubmit={this.handleSubmit} funzioneClick={this.handleClick}/>
                              <br/>
                            </div>
                       </div>

                       <div className='Visualisation'>

                                <br/>
                                <VisualisationGrid { ...this.props } { ...this.state} funzioneSubmit={this.handleSubmit} funzioneClick={this.handleClick}/>


                       </div>

                    </div>     ) }




                                });

export default App;





